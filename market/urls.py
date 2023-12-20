from django.urls import path
from .views import *

urlpatterns = [
    path('', MainListView.as_view(extra_context = {'categories': Category.objects.all()}), name='home'),
    path('product/<slug:slug>', ProductDetailView.as_view(), name='product')
]