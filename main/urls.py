from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.index),
    path('users', views.auth, name='auth')
]
