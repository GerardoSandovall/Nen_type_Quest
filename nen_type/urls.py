from django.urls import path
from . import views

urlpatterns = [
    path('Quest/<int:Key>', views.Quest, name='Quest')
]