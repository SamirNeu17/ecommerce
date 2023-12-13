from django.shortcuts import render

# Create your views here.
def product_detail(request):
    return render(request, "product-detail.html")

def shopping_cart(request):
    return render(request, "shopping-carts.html")

