from django.urls import path
from . import views

# Create the urls here
urlpatterns = [
    path('', views.home, name='home'),
    path('about.html', views.about, name='about'),
]
