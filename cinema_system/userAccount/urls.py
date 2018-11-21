from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('register/', views.registerRequest, name='registerRequest'),
    path('thank_you/', views.activateAccount, name='activate'),
]
