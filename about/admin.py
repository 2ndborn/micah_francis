from django.contrib import admin
from .models import About_me, Education, Work_experience, Interest
from django import forms

class About_meAdmin(admin.ModelAdmin):
    list_display = (
        'content',
        'image',
    )


class EducationAdmin(admin.ModelAdmin):
    list_display = (
        'from_date',
        'to_date',
        'institution',
        'qualification',
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
    

admin.site.register(About_me, About_meAdmin)
admin.site.register(Education, EducationAdmin)
admin.site.register(Work_experience, Work_experienceAdmin)
admin.site.register(Interest, InterestAdmin)