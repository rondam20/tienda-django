from django.shortcuts import render, get_object_or_404
from .models import Product, Category

def home(request):
    products = Product.objects.filter(active=True)[:8]
    categories = Category.objects.all()
    return render(request, "shop/home.html", {"products": products, "categories": categories})

def product_list(request):
    cat = request.GET.get("cat")
    qs = Product.objects.filter(active=True)
    if cat:
        qs = qs.filter(category__slug=cat)
    return render(request, "shop/product_list.html", {
        "products": qs,
        "categories": Category.objects.all(),
        "current_cat": cat,
    })

def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, active=True)
    stock = product.stock_items.all()
    return render(request, "shop/product_detail.html", {"product": product, "stock": stock})
