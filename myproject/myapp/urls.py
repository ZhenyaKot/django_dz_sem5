from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('heads_and_tails/', views.heads_and_tails, name='heads_and_tails'),
    path('cube/', views.cube, name='cube'),
    path('random_choice/', views.random_choice, name='random_choice'),
    path('home/', views.home, name='home'),
    path('about_me/', views.about_me, name='about_me'),
]
