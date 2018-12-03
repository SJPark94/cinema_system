from django.shortcuts import render
from .models import MovieInfo
# Create your views here.

def moviePage(request, title):
    movieObject = MovieInfo.objects.get(title=title)
    return render(request, 'moviePages.html', {'movie': movieObject})

def movieSort(request, modelType):
    movieResults = MovieInfo.objects.filter(modelType__exact=modelType)
    print(movieResults)
    args = {'movie': movieResults, 'modelType': modelType}
    return render(request, 'movieResults.html', {'movies': movieResults, 'modelType': modelType})
