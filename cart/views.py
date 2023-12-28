from django.shortcuts import get_object_or_404, redirect, render
from market.models import Product
from .models import Cart
from django.contrib import messages
from django.db.models import Sum


def add_product_to_cart(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == "POST":
        cart = Cart.objects.get(customer_id=request.user)
        cart.products.add(product)
        messages.success(request, 'Добавление товара в корзину выполнено!')
        return redirect('home')
    else:
        messages.error(request, 'Ошибка.')
    return render(request, 'cart/add_product_to_cart.html', {'cart': cart})


def get_products_from_cart(request):
    cart = Cart.objects.get(customer_id=request.user)
    products = cart.products.all()
    total_price = products.aggregate(Sum('price'))['price__sum']
    return render(request, 'cart/products.html', {'products': products, 'total_price': total_price})


def delete_product_from_cart(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == "POST":
        cart = Cart.objects.get(customer_id=request.user)
        cart.products.remove(product)
        messages.success(request, 'Удаление товара из корзины выполнено!')
        return redirect('products_from_cart')
    else:
        messages.error(request, 'Ошибка.')
    return render(request, 'cart/delete_product_from_cart.html', {'cart': cart})


def clear_all_products(request):
    if request.method == "POST":
        cart = Cart.objects.get(customer_id=request.user)
        cart.products.clear()
        messages.success(request, 'Удалены все товары из корзины')
        return redirect('products_from_cart')
    else:
        messages.error(request, 'Ошибка.')
    return render(request, 'cart/clear_cart.html', {'cart': cart})