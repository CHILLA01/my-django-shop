from django.shortcuts import render
from .models import ProductModel

def product_list(request):
    products = ProductModel.objects.all() # ბაზიდან ყველა პროდუქტის წამოღება
    return render(request, 'products.html', {'products': products})
