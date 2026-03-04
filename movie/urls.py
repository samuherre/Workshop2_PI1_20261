from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('name/', views.name, name='name'),
    path('movie/', views.movie, name='movie'),
]