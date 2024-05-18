from django.contrib import admin
from .models import About, Education, Work_experience, Interest
from django import forms

class AboutAdmin(admin.ModelAdmin):
    
    list_display = (
        'content',
        'description',
        'image',
    )


class EducationAdmin(admin.ModelAdmin):

    list_display = (
        'from_date',
        'to_date',
        'institution',
        'qualification',
        'location',
    )


class Work_experienceAdmin(admin.ModelAdmin):

    list_display = (
        'from_date',
        'to_date',
        'job_title',
        'company',
        'location',
        'achievement1',
        'achievement2',
        'achievement3',
        'achievement4',
        'achievement5',
    )

    ordering = ('from_date',)


class InterestAdmin(admin.ModelAdmin):
    list_display = (
        'interest',
    )
    

admin.site.register(About, AboutAdmin)
admin.site.register(Education, EducationAdmin)
admin.site.register(Work_experience, Work_experienceAdmin)
admin.site.register(Interest, InterestAdmin)