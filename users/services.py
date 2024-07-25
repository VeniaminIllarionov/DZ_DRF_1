import stripe
from config.settings import STRIPE_API_KEY

stripe.api_key = STRIPE_API_KEY


def create_stripe_product(instance):
    """Создаем stripe продукт"""

    title_product = f'{instance.course}' if instance.course else f'{instance.lesson}'
    stripe_product = stripe.Product.create(name=f"{title_product}")
    return stripe_product.get('id')


def create_price(payment_amount):
    """Создание цены для платежа"""

    return stripe.Price.create(
        currency="rub",
        unit_amount=payment_amount * 100,
        recurring={"interval": "month"},
        product_data={"name": "Payment"},
    )


def create_session(price):
    """Создание сессии для оплаты"""
    session = stripe.checkout.Session.create(
        success_url="https://127.0.0.1:8000/",
        line_items=[{"price": price.get('id'), "quantity": 1}],
        mode="subscription",
    )
    return session.get('id'), session.get('url')