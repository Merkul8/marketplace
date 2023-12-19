from django.shortcuts import render
from .serializers import *
from .models import Product


def main(request):
    products = Product.objects.all()
    return render(request, 'market/main.html', {'products': products})