from django.shortcuts import render, get_object_or_404, redirect
from django.db.models.functions import Lower
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse

from .models import Product, Comment
from home.models import Character
from .forms import CommentForm


def all_products(request):
    """ A view to show all products, including sorting and search queries """
    products = Product.objects.all()
    if request.user.is_authenticated:
        wishlist_ids = list(request.user.wishlist.values_list('id', flat=True))
    else:
        wishlist_ids = []
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
                messages.error(
                    request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))

            queries = (
                Q(name__icontains=query)
                | Q(description__icontains=query)
            )
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
    sorting_label = (
        f"{sort}_{direction}" if sort and direction else sort
    )
    context = {
        'products': products,
        'search_term': query,
        'current_character': character,
        'current_sorting': sorting_label,
        'wishlist_ids': wishlist_ids,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, slug):
    """
    Display individual product details
    """
    product = get_object_or_404(Product, slug=slug)
    edit_comment_id = request.GET.get('edit_comment')
    edit_comment = None
    edit_form = None

    related_products = (
        Product.objects
        .filter(character=product.character).exclude(id=product.id)
    )

    if request.method == "POST" and request.user.is_authenticated:
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = product
            comment.commenter = request.user
            comment.approved = False
            comment.save()
            return redirect('product_detail', slug=product.slug)
    else:
        form = CommentForm()
    if edit_comment_id and request.user.is_authenticated:
        try:
            edit_comment = Comment.objects.get(
                pk=edit_comment_id,
                post=product,
                commenter=request.user
            )
            edit_form = CommentForm(instance=edit_comment)
        except Comment.DoesNotExist:
            pass

    comments = product.comments.all()

    if request.user.is_authenticated:
        wishlist_ids = request.user.wishlist.values_list('id', flat=True)
    else:
        wishlist_ids = []

    context = {
        'product': product,
        'related_products': related_products,
        'wishlist_ids': wishlist_ids,
        'comments': comments,
        'comment_form': form,
        'edit_comment': edit_comment,
        'edit_form': edit_form,
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
        messages.info(request, f'Removed {product.name} from your wishlist!')
    else:
        product.wishlist.add(request.user)
        messages.info(request, f'Added {product.name} to your wishlist!')

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
        'products/wishlist.html',
        {"wishlist": wishlist}
    )


@login_required
def comment_edit(request, slug, comment_id):
    product = get_object_or_404(Product, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id, post=product)
    if comment.commenter != request.user:
        messages.error(request, "You can only edit your own comments.")
        return redirect('product_detail', slug=slug)

    if request.method == "POST":
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            messages.info(request, "Comment updated.")
            return redirect('product_detail', slug=slug)
    else:
        form = CommentForm(instance=comment)

    comments = product.comments.all()
    context = {
        'product': product,
        'related_products': Product.objects.filter(
            character=product.character).exclude(id=product.id),
        'comments': comments,
        'comment_form': CommentForm(),
        'edit_comment': comment,
        'edit_form': form,
        'wishlist_ids': request.user.wishlist.values_list('id', flat=True),
    }
    return render(request, 'products/product_detail.html', context)


@login_required
def comment_delete(request, slug, comment_id):
    product = get_object_or_404(Product, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id, post=product)
    if comment.commenter != request.user:
        messages.error(request, "You can only delete your own comments.")
    else:
        comment.delete()
        messages.info(request, "Comment deleted.")
    return redirect('product_detail', slug=slug)
