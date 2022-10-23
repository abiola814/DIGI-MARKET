from unicodedata import category
from django.contrib import messages
from django.db.models import Q
from django.http import Http404, JsonResponse
from django.shortcuts import redirect, render
from django.views.decorators.cache import cache_page

from product.models import Product,Category

from .models import Contact


def home(request):
    products = Product.objects.all()
 
    return render(request, 'core/homes.html', {'products': products})

def shop(request):
    products = Product.objects.all()
    category = Category.objects.all()
    print(category)
    return render(request, 'core/shop.html', {'products': products,'categorys':category})

def search_category(request,category):
    d=Category.objects.get(title=category)

    products = Product.objects.filter(category=d.id)
    categorys = Category.objects.all()
    print(categorys)
    return render(request, 'core/shop.html', {'products': products,'categorys':categorys})

@cache_page(60 * 60)
def search_api(request):
    ''' Search API for autocomplete '''
    queryset = request.GET.get('query')
    if queryset:
        products = Product.objects.filter(Q(title__icontains=queryset) | Q(
            slug__icontains=queryset) | Q(description__icontains=queryset))
        jsonPayload = []
        for product in products:
            jsonPayload.append({
                'title': product.title,
                'slug': product.slug,
                # 'image': print(type(product.image)),
                'url': product.url,
                'description': product.description,
            })

        return JsonResponse({
            'status': 200,
            'data': jsonPayload
        })
    else:
        raise Http404


@cache_page(60 * 60)
def search(request):
    ''' redirect search result  '''
    queryset = request.GET.get('query')
    if queryset:
        products = Product.objects.filter(Q(title__icontains=queryset) | Q(
            slug__icontains=queryset) | Q(description__icontains=queryset))
        return render(request, 'core/search.html', {'results': products})
    else:
        raise Http404


def about(request):
    return render(request, 'core/about.html')


def contact(request):
    '''
    user contact submission form
    '''
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        subject = request.POST.get('subject')
        contact = Contact(name=name, email=email, message=message, subject=subject)
        contact.save()
        messages.success(request, 'Your message has been sent successfully')
        return redirect('contact')

    return render(request, 'core/contact.html')
