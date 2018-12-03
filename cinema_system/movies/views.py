from django.shortcuts import render
from .models import MovieInfo
# Create your views here.

def moviePage(request, title):
    movieObject = MovieInfo.objects.get(title=title)
    return render(request, 'moviePages.html', {'movie': movieObject})

