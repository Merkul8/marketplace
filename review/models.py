from django.db import models
from market_auth.models import Customer

class Review(models.Model):
    """
    Model for a created review by users
    """

    ESTIMATIONS = ( 
        (1, "1"), 
        (2, "2"), 
        (3, "3"), 
        (4, "4"), 
        (5, "5"), 
    ) 
   
    description = models.TextField(verbose_name='Отзыв', max_length=1000)
    image = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фото товара', blank=True)
    estimate = models.PositiveSmallIntegerField(choices=ESTIMATIONS, verbose_name='Оценка')
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE, verbose_name='Пользователь', default=None)

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'


