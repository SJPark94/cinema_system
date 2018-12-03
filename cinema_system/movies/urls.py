from django.urls import path
from . import views
from paymentSystem.views import selection

urlpatterns = [
    path('<str:title>', views.moviePage, name='moviePage'),
    path('sort/<str:modelType>', views.movieSort, name='movieSort'),
    path('searchresult/', views.movieSearch, name='movieSearch'),
    path('book/<str:title', views.selection, name='selectTicket'),
]