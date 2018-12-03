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

def movieSearch(request):
    if request.method == 'POST':
        print("HELLO WORLD")
        searchString = request.POST.get("search", '')
        if len(searchString) == 0:
            movieObject = MovieInfo.objects.all()
            return render(request, 'homepage/index.html', {'movies': movieObject})
        else:
            searchResults = MovieInfo.objects.filter(title__icontains=searchString)
            if searchResults:
                print("YOLO")
                return render(request, 'searchResults.html', {'movies': searchResults})
            else:
                return render(request, 'nomovies.html')
    else:
        movieObject = MovieInfo.objects.all()
        return render(request, 'homepage/index.html', {'movies': movieObject})