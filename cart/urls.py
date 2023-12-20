from django.urls import path
from .views import *

urlpatterns = [
    path('add_product_to_cart/<int:pk>/', add_product_to_cart, name='add_product_to_cart'),
    path('products/', get_products_from_cart, name='products_from_cart'),
]
