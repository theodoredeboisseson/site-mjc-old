import stripe
from django.conf import settings

stripe.api_key = settings.STRIPE_SECRET_KEY


def charge_card(stripe_token, total):
    total_in_cent = int(total*100)
    return stripe.Charge.create(
        amount=total_in_cent,
        currency="EUR",
        description="Dummy Transaction",
        card=stripe_token,
    )
