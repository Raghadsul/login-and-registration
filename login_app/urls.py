from django.urls import path     
from . import views

urlpatterns = [
    path('', views.index),
    path('process', views.register),
    path('login', views.login),
    path('success', views.index2),
    path('logout', views.logout),

]