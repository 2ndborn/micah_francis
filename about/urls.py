from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.about, name='about'),
    path('add_about/', views.add_about, name='add_about'),
    path('edit_about/<int:about_id>/', views.edit_about, name='edit_about'),
    path('delete_about/<int:about_id>/', views.delete_about, name='delete_about'),
    path('add_education/', views.add_education, name='add_education'),
    path('edit_education/<int:education_id>/', views.edit_education, name='edit_education'),
    path('delete_education/<int:education_id>/', views.delete_education, name='delete_education'),
    path('add_work/', views.add_work, name='add_work'),
    path('edit_work/<int:work_id>/', views.edit_work, name='edit_work'),
    path('delete_work/<int:work_id>', views.delete_work, name='delete_work'),
    path('add_interest/', views.add_interest, name='add_interest'),
    path('edit_interest/<int:interest_id>/', views.edit_interest, name='edit_interest'),
    path('delete_interest/<int:interest_id>/', views.delete_interest, name='delete_interest'),
]