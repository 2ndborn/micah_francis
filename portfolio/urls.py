from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.portfolio, name='portfolio'),
    path('add_portfolio/', views.add_portfolio, name='add_portfolio'),
    path('edit_portfolio/<int:portfolio_id>/', views.edit_portfolio, name='edit_portfolio'),
    path('delete_portfolio/<int:portfolio_id>/', views.delete_portfolio, name='delete_portfolio'),
]