from django.db import models
from market_auth.models import Customer
import uuid


class Category(models.Model):
    """
    Model of a products category
    """
    name = models.CharField(verbose_name='Категория', max_length=255)
    slug = models.SlugField(unique=True, blank=True, verbose_name='Url')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


    def __str__(self) -> str:
        return self.name


class Product(models.Model):
    """
    Model of a product 
    """
    name = models.CharField(verbose_name='Название товара', max_length=255)
    description = models.CharField(verbose_name='Краткое описание', max_length=510)
    product_code = models.UUIDField(default=uuid.uuid4, editable=False, verbose_name='Уникальный код продукта')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    product_count = models.IntegerField(verbose_name='Количество товара')
    slug = models.SlugField(unique=True, blank=True, verbose_name='Url')
    is_stock = models.BooleanField(default=True, verbose_name='В наличии')
    categories = models.ManyToManyField(Category, verbose_name='Категория')
    # Это демо-поле для поставщика, ему будут присваиваться определенные права доступа 
    seller_id = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Продавец')
    
    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

class ProductImage(models.Model):
    """
    Model for adding photos to a product
    """
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name=f'Фото товара', blank=True)

    class Meta:
        verbose_name = 'Изображение товара'
        verbose_name_plural = 'Изображения товаров'