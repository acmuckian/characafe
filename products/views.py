from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.db.models.functions import Lower 
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Product
from home.models import Character

# Create your views here.
def all_products(request):
    """ A view to show all products, including sorting and search queries """
    products = Product.objects.all()
    query = None
    character = None
    sort = None
    direction = None
   

    if request.GET: 
        if 'character' in request.GET:
            character_name = request.GET['character'].lower()
            try:
                character = Character.objects.get(name__iexact=character_name)
                products = products.filter(character=character)
            except Character.DoesNotExist:
                pass


        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))
            
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)
        
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)
            
    context = {
        'products': products,
        'search_term': query,
        'current_character': character,
        'current_sorting': f'{sort}_{direction}' if sort and direction else sort,
    }

    return render(request, 'products/products.html', context)
    
def product_detail(request, slug):
    """
    Display individual product details
    """
    product = get_object_or_404(Product, slug=slug)

    related_products = Product.objects.filter(character=product.character).exclude(id=product.id)
    if request.user.is_authenticated:
        wishlist_ids = request.user.wishlist.values_list('id', flat=True)
    else:
        wishlist_ids = []
   
    context = {
        'product': product,
        'related_products': related_products,
        'wishlist_ids': wishlist_ids,
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
        messages.success(request, f'Removed {product.name} from your wishlist!')
    else:
        product.wishlist.add(request.user)
        messages.success(request, f'Added {product.name} to your wishlist!')

    redirect_url = request.META.get('HTTP_REFERER')
    if redirect_url:
        return redirect(redirect_url)
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



