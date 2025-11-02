from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.conf import settings
from bag.contexts import bag_contents 
import stripe

from .forms import OrderForm 

# Create your views here.

def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag")
        return redirect(reverse('products'))
    
    print(f"Public key exists: {bool(stripe_public_key)}")
    print(f"Secret key exists: {bool(stripe_secret_key)}")
    
    current_bag = bag_contents(request)
    total = current_bag['grand_total']
    stripe_total = round(total * 100)
    stripe.api_key = stripe_secret_key
    
    # Create PaymentIntent
    intent = stripe.PaymentIntent.create(
        amount=stripe_total,
        currency=settings.STRIPE_CURRENCY,
    )

    
    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,  
        **current_bag,
    }

    return render(request, template, context)


