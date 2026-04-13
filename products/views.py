from django.shortcuts import render, get_object_or_404
from products.models import Product, Category
from django.http import HttpResponse

def category_products(request, slug):
    category = get_object_or_404(Category, slug=slug)
    products = Product.objects.filter(category=category, available=True)
    return render(request, 'products/category.html', {
        'category': category,
        'products': products
    })

def home(request):
    home_products = Product.objects.all().order_by("-created_at")
    return render(request, "home.html", {"home_products": home_products})