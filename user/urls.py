from django.contrib import admin
from django.urls import path
from user import views
app_name = 'user'
urlpatterns = [
     path('support/', views.SupportForm,name='support'),
    
]