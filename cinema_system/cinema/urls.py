from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView


urlpatterns = (
    path('', TemplateView.as_view(template_name='homepage/index.html'), name='homepage'),
    path('admin/', admin.site.urls),
    path('accounts/', include('userAccount.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    #path('movies/', include('movies.urls')),
)
