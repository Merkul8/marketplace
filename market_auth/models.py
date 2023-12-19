from django.db import models
from django.contrib.auth.models import AbstractUser
from payment.models import BankCard


class Customer(AbstractUser):
    bank_cards = models.ManyToManyField(BankCard, verbose_name='Банковская карта', blank=True)
    role_id = models.ForeignKey('Role', verbose_name='Категория пользователя', on_delete=models.SET_DEFAULT, default=1)


class Role(models.Model):
    name = models.CharField(max_length=255, verbose_name='Категория пользователя')

    class Meta:
        verbose_name = 'Роль'
        verbose_name_plural = 'Роли'

    def __str__(self) -> str:
        return self.name