from django import template


register = template.Library()

@register.filter(name='calc_subtotal')
def calc_subtotal(price, quantity):
    """
    Calculate subtotal by multiplying price and quantity
    Usage: {{ product.price|calc_subtotal:item.quantity }}
    """
    return price * quantity


