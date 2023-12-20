from .serializers import *
from .models import Product
from django.views.generic import ListView, DetailView


class MainListView(ListView):
    context_object_name = 'products'
    template_name = 'market/main.html'
    model = Product


class ProductDetailView(DetailView):
    model = Product
    context_object_name = 'product'
    template_name = 'market/product_detail.html'