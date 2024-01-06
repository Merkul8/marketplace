from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from .serializers import *
from .models import Product
from django.views.generic import ListView, DetailView
from review.forms import CreateReviewForm
from review.models import Review
from .forms import *
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
import django_filters
from itertools import chain


class MainListView(ListView):
    """ Главная страница сайта с товарами """
    context_object_name = 'products'
    template_name = 'market/main.html'
    model = Product

    def get_queryset(self) -> QuerySet[Any]:
        return Product.objects.all().order_by('-views').prefetch_related('images')


class ProductDetailView(DetailView):
    """ Представление определенного товара """
    model = Product
    context_object_name = 'product'
    template_name = 'market/product_detail.html'
    form_class = CreateReviewForm

    def post(self, request, *args, **kwargs):
        """ Форма добавления отзыва """
        self.object = self.get_object()
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            review = form.save(commit=False)
            review.customer_id = request.user
            review.product = self.object
            review.save()
            return redirect('product', self.object.slug)
        else:
            form = self.form_class()
        return form
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['form'] = self.form_class
        # Показ просмотров товара, пока работает костыльно, инкеремтится даже при обновлении страницы
        product = self.get_object()
        product.views += 1
        product.save()
        # Отзывы для определенного товара
        context['reviews'] = Review.objects.filter(product=product)
        return context
    

def create_product(request):
    """ Создание товара только для продавцов(role = 'Продавец') """
    if request.method == 'POST':
        product_form = ProductForm(request.POST)
        image_form = ProductImageForm(request.POST, request.FILES)
        if product_form.is_valid() and image_form.is_valid():
            product = product_form.save()
            product.seller_id = request.user
            product.save()
            image = image_form.save(commit=False)
            image.product_id = product
            image.save()
            return redirect('home')
    else:
        product_form = ProductForm()
        image_form = ProductImageForm(request.FILES)
    return render(request, 'market/create_product.html', {'product_form': product_form, 'image_form': image_form})


class Search(ListView):
    """ Поиск товаров (Демо-версия поиска)"""
    template_name = 'market/search.html'
    context_object_name = 'products'

    def get_queryset(self) -> QuerySet[Any]:
        query = self.request.GET.get('q')
        queryset = Product.objects.filter(name__icontains=query)
        required_queryset = Product.objects.order_by('-views')[:10]
        if queryset.exists():
            return list(chain(queryset, required_queryset))
        return required_queryset
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['q'] = self.request.GET.get('q')
        return context
    

# API для микросервиса на Go

class ProductsListView(generics.ListAPIView):
    """ Представление для использования совестно с микросервисом .
    Получение всех товаров для определенного пользователя с помощью токена,
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



