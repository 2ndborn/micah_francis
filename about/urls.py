from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.about, name='about'),
    path('add_education/', views.add_education, name='add_education'),
    path('edit_education/<int:education_id>/', views.edit_education, name='edit_education'),
    path('delete_education/<int:education_id>/', views.delete_education, name='delete_education'),
]