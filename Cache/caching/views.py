from django.shortcuts import render
from django.views.decorators.cache import cache_page

# Create your views here.

@cache_page(60 * 15)  # Cache the view for 15 minutes
def home(request):
    return render(request, 'caching/home.html')

    """this is the one way views m hi likh dia then urls m path 
    now the another way is yaha normal view hi rakhenge no cache_page decorator
    or fir urls.py m likh denge path('home/', cache_page(60)(views.home), name='home')
    and also importing cache_page from django.views.decorators.cache
    """