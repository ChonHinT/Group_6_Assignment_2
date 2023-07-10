from django.shortcuts import get_object_or_404, render

from .models import Category, Product
from django import forms
from .forms import ProductSearchForm


def products_all(request):
    products = Product.objects.filter(is_active=True)
    return render(request, 'store/home.html', {'products': products})


def category_list(request, category_slug=None):
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.filter(category=category)
    return render(request, 'store/products/category.html', {'category': category, 'products': products})


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, in_stock=True)
    return render(request, 'store/products/single.html', {'product': product})


def search_product(request):
    form = ProductSearchForm(request.GET)
    results = []

    if form.is_valid():
        search_query = form.cleaned_data['search_query']
        results = Product.objects.filter(title__icontains=search_query)

    return render(request, 'store/search.html', {'form': form, 'results': results})
