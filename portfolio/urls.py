from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.portfolio, name='portfolio'),
    path('add_portfolio/', views.add_portfolio, name='add_portfolio'),
]