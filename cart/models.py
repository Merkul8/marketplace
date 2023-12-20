from django.db import models
from market_auth.models import Customer
from market.models import Product

class Cart(models.Model):
    """
    Cart model for adding a new product
    """
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE, verbose_name='Пользователь')
    products = models.ManyToManyField(Product, verbose_name='Название', blank=True)

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'