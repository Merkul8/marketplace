from django.urls import path
from .views import *
from django.conf import settings



urlpatterns = [
    path('', MainListView.as_view(extra_context = {'categories': Category.objects.all()}), name='home'),
    path('product/<str:slug>', ProductDetailView.as_view(extra_context = {"STRIPE_PUBLIC_KEY": settings.PUBLIC_API_KEY}), name='product'),
    path('create_product/', create_product, name='create_product'),
    path('search/', Search.as_view(), name='search'),
    # API
    path('api/products/', ProductsListView.as_view(), name='api_products'),
    path('api/products-by-category/', ProductByCategoryView.as_view(), name='products_by_category'),
    path('api/categories/', CategoryListView.as_view(), name='category_list'),
]