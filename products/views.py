from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.shortcuts import render
from django.db.models.functions import Lower 
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Product, Character

# Create your views here.
def all_products(request):
    """ A view to show all products, including sorting and search queries """
    products = Product.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET: 
        sortkey = request.GET['sort']
        sort = sortkey
        if sortkey == 'name':
            sortkey = 'lower_name'
            products = products.annotate(lower_name=Lower('name'))
            if sortkey == 'character':
                sortkey = 'character__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)
            
        if 'character' in request.GET:
            characters = request.GET['character'].split(',')
            products = products.filter(character__name__in=characters)
            characters = Character.objects.filter(name__in=characters)
            
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))
            
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)
    
def product_detail(request, slug):
    """
    Display individual product details
    """
    product = get_object_or_404(Product, slug=slug)
    
    context = {
        'product': product,
    }
    
    return render(request, 'products/product_detail.html', context)

@login_required
def add_to_wishlist(request, slug):
    """
    Allows a user to add an product to their wishlist.
        **Context**

    ``product``
        An instance of :model:`product.Product`.
    ``favourites``
        A wishlist favourite related to the product.
        **Template**
        :template:`account/wishlist.html`
    """
    product = get_object_or_404(Product, slug=slug)
    if product.wishlist.filter(id=request.user.id).exists():
        product.wishlist.remove(request.user)
        messages.success(request, messages.SUCCESS, 'Removed from your wishlist!')
    else:
        product.wishlist.add(request.user)
        product.success(request, messages.SUCCESS, 'Added to your wishlist!')
    return redirect('product_detail', slug=product.slug)


@login_required
def my_wishlist(request):
    """
    Allows a user to see their wishlist.
        **Context**

    ``Product``
        An instance of :model:`product.Product`.
    ``favourites``
        A wishlist favourite related to the product.
        **Template**
        :template:`products/wishlist.html`
    """
    wishlist = Product.objects.filter(wishlist=request.user)

    return render(
        request,
        'account/wishlist.html',
        {"wishlist": wishlist}
    )



