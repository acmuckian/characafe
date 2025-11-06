from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm
from .models import Profile
from products.models import Product

# Create your views here.
@login_required 
def profile(request):
    user_wishlist = Product.objects.filter(wishlist=request.user)
    profile = get_object_or_404(Profile, user=request.user )
    form = ProfileForm(instance=profile)
    orders = profile.orders.all()

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'orders': orders,
        'user_wishlist': user_wishlist,
    }

    return render(request, template, context)