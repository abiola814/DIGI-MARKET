import email
from django.contrib import messages
from django.contrib.auth import (
    authenticate, login, update_session_auth_hash, views as auth_views,
)
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.shortcuts import redirect, render
from requests import request
from order.models import OrderItem

from .decorators import customer_required
from .forms import CustomerSignUpForm, CustomerUpdateForm
from .utils import service
from .models import Customer, User


@customer_required
def customerWishlistAndFollowedStore(request):
    ''' customer wishlist and followed store.'''
    return render(request, 'customer/wishlist_and_followed_store.html')


@customer_required
def CustomerProfile(request):
    ''' customer profile '''

    order = OrderItem.objects.filter(order__customer=request.user.customer)

    context = {
        'customer': request.user.customer,
        'orders': order,
    }

    return render(request, 'customer/customer_profile.html', context)


@customer_required
def CustomerProfileUpdate(request):
    ''' Update customer profile '''
    if request.method == 'POST':
        form = CustomerUpdateForm(request.POST, request.FILES, instance=request.user.customer)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile was successfully updated!')
            return redirect('customer_profile')
    else:
        form = CustomerUpdateForm(instance=request.user.customer)
        context = {
            'form': form,
        }
        return render(request, 'customer/customer_profile_edit.html', context)


def CustomerSignUpView(request):
    ''' Sign up view for new customer account.'''
    if request.method == 'POST':
        address = request.POST.get('address')
        phone = request.POST.get('phonenumber')
        country = request.POST.get('country')
        full_name = request.POST.get("name")
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirmpassword = request.POST.get('password2')
        print(password)
        print(confirmpassword)
        if password != confirmpassword:
            messages.error(request, 'Password is not the same')
        elif User.objects.filter(email=email):
            messages.error(request, 'email exist sign In')
        else:
            user = User.objects.create_user(email=email,password=password,is_customer=True)
            customer = Customer.objects.create(user=user)
            customer.email = email
            customer.country = country
            customer.address = address
            customer.full_name = full_name
            customer.phone_number = phone
            customer.save()
            messages.success(request, 'Thanks for registering. You are now logged in.')
            users = authenticate(email=email, password=password)
            login(request, users)
            # service.send_welcome_mail(request, request.user.customer.email)
        return redirect('profile/')
    else:
        form = CustomerSignUpForm()
        return render(request, 'customer/regs.html')


@customer_required
def change_password_view(request):
    '''A form for allowing customer to change with old password '''
    if request.method == "POST":
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, "Password Change Successfully!")
            return redirect('/')
    else:
        form = PasswordChangeForm(user=request.user)
        return render(request, "customer/password_change.html", {"form": form})


class SignInView(auth_views.LoginView):
    ''' Sign in for customer '''
    form_class = AuthenticationForm
    template_name = 'customer/signin.html'
