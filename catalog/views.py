from django.shortcuts import render
from django.views import generic

# Create your views here.
from .models import Temple, God, Religion

def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_temples = Temple.objects.all().count()
    
    # The 'all()' is implied by default.    
    num_gods = God.objects.count()
    
    context = {
        'num_temples': num_temples,
        'num_gods': num_gods,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)



class TempleListView(generic.ListView):
    model = Temple
    #context_object_name = 'temple_list' 
    #queryset = Temple.objects.all()[:20] # Get 5 temples containing the title war
    #template_name = 'catalog/temple_list.html'  # Specify your own template name/location
    paginate_by= 8

class TempleDetailView(generic.DetailView):
    """
    Generic class-based detail view for a book.
    """
    model = Temple

def gods(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_temples = Temple.objects.all().count()
    
    # The 'all()' is implied by default.    
    num_gods = God.objects.count()
    
    context = {
        'num_temples': num_temples,
        'num_gods': num_gods,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)
