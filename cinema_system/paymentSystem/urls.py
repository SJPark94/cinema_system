from django.urls import path
from . import views

urlpatterns = [
    path('movies/<str:title>', views.selection, name="selectTicket"),
]