from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.contrib import messages
from django.urls import reverse
from products.models import Product


def view_bag(request):
    """ A view to return the shopping bag page """

    return render(request, "bag/shopping_bag.html")


def add_to_bag(request, item_id):
    """"
    add a product to the bag
    """
    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        bag[item_id] += quantity
        messages.success(
            request, f'Updated {product.name} quantity to {bag[item_id]}'
            )
    else:
        bag[item_id] = quantity
        messages.success(request, f'Added {product.name} to your bag')
    request.session['bag'] = bag
    return redirect(redirect_url)


def adjust_qty(request, item_id):
    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    bag = request.session.get('bag', {})
    if quantity > 0:
        bag[item_id] = quantity
        messages.success(
            request, f"Updated {product.name}'s quantity to {bag[item_id]}!")
    else:
        bag.pop(item_id, None)
        messages.success(request, f'Removed {product.name} from your bag')
    request.session['bag'] = bag
    return redirect(reverse('shopping_bag'))


def remove_from_bag(request, item_id):
    """ Remove the item from the shopping bag """
    try:
        product = get_object_or_404(Product, pk=item_id)
        bag = request.session.get('bag', {})

        if item_id in bag:
            bag.pop(item_id)
            request.session['bag'] = bag
            messages.success(request, f'Removed {product.name} from your bag')
            return HttpResponse(status=200)
        else:
            messages.error(request, 'Item not found in bag')
            return HttpResponse(status=404)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
