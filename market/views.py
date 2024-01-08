from collections import OrderedDict
from typing import Any
from django.db.models.query import QuerySet
from django.http import HttpRequest
from django.shortcuts import render, redirect
from .serializers import *
from .models import Product, Ip
from django.views.generic import ListView, DetailView
from review.forms import CreateReviewForm
from review.models import Review
from .forms import *
from itertools import chain
from django.db.models import Q
from .tasks import (
    send_mail_befor_add_review,
    send_mail_before_add_product,
)


class MainListView(ListView):
    """ Главная страница сайта с товарами """
    context_object_name = 'products'
    template_name = 'market/main.html'
    model = Product

    def get_queryset(self) -> QuerySet[Any]:
        return Product.objects.all().order_by('-views').prefetch_related('images')

# detail update create нужно сделать с помощью drf, выглядит не очень :(

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
            send_mail_befor_add_review.delay(request.user.email, request.user.username)
            return redirect('product', self.object.slug)
        else:
            form = self.form_class()
        return form
    
    # Получения IP адреса
    def get_client_ip(self, request: HttpRequest) -> str:
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR') # В REMOTE_ADDR значение айпи пользователя
        return ip
    
    def increment_views_for_product(self):
        product = self.get_object()
        ip = self.get_client_ip(self.request)
        Ip.objects.get_or_create(ip=ip)
        ip_for_add = Ip.objects.get(ip=ip)
        product.views.add(ip_for_add)
        return ip_for_add
    
    def get_reviews_by_product(self):
        product = self.get_object()
        return Review.objects.filter(product=product)

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['form'] = self.form_class
        # Отзывы для определенного товара
        context['reviews'] = self.get_reviews_by_product()
        # Получения IP адреса
        context['ip'] = self.increment_views_for_product()
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
            send_mail_before_add_product.delay(request.user.email, request.user.username)
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
        queryset = Product.objects.filter(Q(name__icontains=query) | Q(categories__name__icontains=query)).distinct()
        required_queryset = Product.objects.order_by('-views')[:10]
        if queryset.exists():
            combined_queryset = list(chain(queryset, required_queryset))
            unique_queryset = OrderedDict((product.id, product) for product in combined_queryset).values()
            return unique_queryset
        return required_queryset
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['q'] = self.request.GET.get('q')
        return context
    




