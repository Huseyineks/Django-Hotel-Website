from django.contrib import admin
from django.urls import path
from . import views
app_name = 'App'
urlpatterns = [
     path('', views.events,name='events'),
    path('childeren/', views.childeren,name='childeren'),
    path('adult/', views.adult,name='adult'),
]