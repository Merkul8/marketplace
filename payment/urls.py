from django.urls import path
from .views import *


urlpatterns = [
    path('buy/', BuyProductView.as_view(), name='buy'),
    path('success/', SuccessView.as_view(), name='success'),
    path('cancel/', CancelView.as_view(), name='cancel'),
]