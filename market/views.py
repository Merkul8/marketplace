from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import redirect
from .serializers import *
from .models import Product
from django.views.generic import ListView, DetailView
from review.forms import CreateReviewForm
from review.models import Review

class MainListView(ListView):
    context_object_name = 'products'
    template_name = 'market/main.html'
    model = Product

    def get_queryset(self) -> QuerySet[Any]:
        return Product.objects.all().prefetch_related('images')


class ProductDetailView(DetailView):
    model = Product
    context_object_name = 'product'
    template_name = 'market/product_detail.html'
    form_class = CreateReviewForm

    def post(self, request, *args, **kwargs):
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
        context['reviews'] = Review.objects.all().prefetch_related('product')
        product = self.get_object()
        product.views += 1
        product.save()
        return context