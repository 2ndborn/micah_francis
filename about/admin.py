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
    def get_form(self, request, achievement=None, **kwargs):
        form = super().get_form(request, achievement, **kwargs)

        # Add custom logic for the "achievement" field
        if achievement:
            # If editing an existing object, show the "remove" option
            form.base_fields['achievement'].widget.attrs['placeholder'] = 'Edit achievement'
        else:
            # If adding a new object, show the "add" option
            form.base_fields['achievement'].widget.attrs['placeholder'] = 'Add achievement'
        
        return form

    list_display = (
        'from_date',
        'to_date',
        'job_title',
        'company',
        'location',
        'achievement',
    )


class InterestAdmin(admin.ModelAdmin):
    list_display = (
        'interest',
    )
    

admin.site.register(About, AboutAdmin)
admin.site.register(Education, EducationAdmin)
admin.site.register(Work_experience, Work_experienceAdmin)
admin.site.register(Interest, InterestAdmin)