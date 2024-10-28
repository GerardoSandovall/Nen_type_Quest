from django.urls import path
from . import views

urlpatterns = [
    path('', views.Main, name='Main'),
    path('Register/', views.Register, name='Register'),
    path('Logout/', views.Logout , name= 'Logout'),
    path('Login/', views.Login, name='Login'),
]