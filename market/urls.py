from django.urls import path
from .views import *
from .views import *

urlpatterns = [
    path('', main, name='home'),
]