from django.urls import path
from . import views 
from .views import search_product


app_name = 'store'

urlpatterns = [
    path('', views.products_all, name='product_all'),
    path('<slug:slug>', views.product_detail, name='product_detail'),
    path('shop/<slug:category_slug>/', views.category_list, name='category_list'),
    path('search/', views.search_product, name = 'search_product'),
]
