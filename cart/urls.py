from django.urls import path
from .views import *

urlpatterns = [
    path('add_product_to_cart/<int:pk>/', add_product_to_cart, name='add_product_to_cart'),
    path('products/', get_products_from_cart, name='products_from_cart'),
    path('delete_product_from_cart/<int:pk>/', delete_product_from_cart, name='delete_product_from_cart'),
    path('clear_all_products/', clear_all_products, name='clear_all_products'),
]
