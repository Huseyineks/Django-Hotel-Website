from django.contrib import admin
from django.urls import path
from user import views
app_name = 'user'
urlpatterns = [
     path('contact/', views.ContactView.as_view(),name='contact'),
     
]