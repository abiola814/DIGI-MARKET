from customers.models import User
from django.contrib.auth import login
from django.shortcuts import redirect, render
from django.views.generic import CreateView
from product.models import Product
from vendor.decorators import vendor_required
from vendor.forms import ProductForm
from vendor.models import Vendor


def home(request):
    """Add a product to the vendor's product list."""
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.created_by = Vendor.objects.get(user=request.user)
            product.save()
            return redirect('vendor:root_path')
    else:
        form = ProductForm()
    return render(request, 'vendor/homes.html', {'form': form})