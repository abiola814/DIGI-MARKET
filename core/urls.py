from unicodedata import category
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('shop', views.shop, name='shop'),
    path('shop/<str:category>', views.search_category, name='search_category'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('search', views.search_api, name='search'),
    path('product', views.search, name='search'),

]
