from rest_framework import serializers
from .models import Product, Category
from review.models import Review


class ProductSerializer(serializers.ModelSerializer):
    """Сериалайзер для фильтров и микросервиса"""
    class Meta:
        model = Product
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    """Сериалайзер для вывода отзывов"""
    customer_id = serializers.SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        model = Review
        fields = ('description', 'estimate', 'customer_id', )


class CategorySerializer(serializers.ModelSerializer):
    """Сериалайзер для вывода категорий"""
    class Meta:
        model = Category
        fields = ('name',)


class ProductSerializer(serializers.ModelSerializer):
    """Для вывода детальной информации о товаре и отзывах 
    прикрепленных к нему"""
    reviews = ReviewSerializer(many=True)
    categories = CategorySerializer(many=True)

    class Meta:
        model = Product
        fields = '__all__'


