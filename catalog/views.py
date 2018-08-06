from django.shortcuts import render

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


def temples(request):
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
