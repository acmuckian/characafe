from django.shortcuts import render
from django.views import generic
from .models import Character, MenuItem

# Create your views here.


def index(request):
    """ A view to return the index page """
    characters = Character.objects.all()[:6]
    menu_items = MenuItem.objects.all()[:6]

    context = {
        'characters': characters,
        'menu_list': menu_items,
    }

    return render(request, 'home/index.html', context)


class CharacterList(generic.ListView):
    model = Character
    queryset = Character.objects.all()
    template_name = "home/characters.html"
    paginate_by = 6
    context_object_name = 'characters'
    ordering = ['name', 'pk']


class MenuItemList(generic.ListView):
    model = MenuItem
    queryset = MenuItem.objects.all()
    template_name = "home/menu.html"
    paginate_by = 6
    context_object_name = 'menu_list'
