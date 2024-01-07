from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
import django_filters
from .serializers import *
from .models import Product
from review.models import Review


# API для микросервиса на Go

class ProductsBySellerListView(generics.ListAPIView):
    """ Представление для использования совестно с микросервисом .
    Получение всех товаров для определенного пользователя с помощью токена(см marketplace/urls.py),
    токен используется для взаимодействия с микросервисом """
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Product.objects.filter(seller_id=user).order_by('-pk')
    


# Endpoints for filter search

class ProductByCategoryFilter(django_filters.FilterSet):
    categories__name = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Product
        fields = ['categories__name']


class ProductByCategoryView(generics.ListAPIView):
    """ Поиск товаров по категории """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ProductByCategoryFilter


class CategoryFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Category
        fields = ['name']


class CategoryListView(generics.ListAPIView):
    """ Поиск категории для дальнейшего поиска товаров """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = CategoryFilter


class ProductsListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
