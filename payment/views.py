from django.views import View
from market.models import Product
from django.http import JsonResponse
import stripe
from django.views.generic import TemplateView
from cart.models import Cart
from django.db.models import Sum

# Получение session id
class BuyProductView(View):
    def post(self, request):
        cart = Cart.objects.get(customer_id=request.user)
        products = cart.products.all()
        YOUR_DOMAIN = "http://127.0.0.1:8000"
 
        line_items = []
        for product in products:
            line_items.append({
                'price_data': {
                    'currency': 'rub',
                    'unit_amount': int(product.price * 100),
                    'product_data': {
                        'name': product.name,
                    },
                },
                'quantity': 1,
            })

        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=line_items,
            metadata={
                "product_id": 1
            },
            mode='payment',
            success_url=YOUR_DOMAIN + '/payment/success/',
            cancel_url=YOUR_DOMAIN + '/payment/cancel/',
        )
        return JsonResponse({
           'id': checkout_session.id
       })

# платеж проведен успешно
class SuccessView(TemplateView):
    template_name = "payment/success.html"

# отмена платежа
class CancelView(TemplateView):
    template_name = "payment/cancel.html"

    