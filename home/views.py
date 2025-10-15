from django.shortcuts import render
from django.views import generic
from .models import Character

# Create your views here.



def index(request):
    """ A view to return the index page """
    
    return render(request, 'home/index.html')

class CharacterList(generic.ListView):
    model = Character
    queryset = Character.objects.all()
    template_name = "products/index.html"
    paginate_by = 6
    context_object_name = 'img_list'
