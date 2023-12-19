from django.db import models


class BankCard(models.Model):
    """
    Model of a user's bank card
    """
    number = models.CharField(verbose_name='Номер карты', max_length=16)
    expiry_month = models.PositiveSmallIntegerField(verbose_name='Месяц')
    expiry_year = models.PositiveSmallIntegerField(verbose_name='Год')
    firstname_surname = models.CharField(verbose_name='Фамилия и Имя', max_length=255)

    class Meta:
        verbose_name = 'Банковская карта'
        verbose_name_plural = 'Банковские карты'
