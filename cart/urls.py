from django.urls import path
from .views import *

urlpatterns = [
    path('add_product_to_cart/<int:pk>/', AddProductToCartView.as_view(), name='add_product_to_cart'),
    path('products/', ProductsFromCartView.as_view(), name='products_from_cart'),
    path('delete_product_from_cart/<int:pk>/', delete_product_from_cart, name='delete_product_from_cart'),
    path('clear_all_products/', clear_all_products, name='clear_all_products'),
]
