from django.urls import path
from .views import *


urlpatterns = [
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('register_for_seller/', register_for_seller, name='register_for_seller'),
]