from django.contrib import admin
from .models import About_me, Education, Work_experience, Interest

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
        'qualifation',
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


class InterestAdmin(admin.ModelAdmin):
    list_display = (
        'interest1',
        'interest2',
        'interest3',
        'interest4',
        'interest5',
    )


admin.site.register(About_me, About_meAdmin)
admin.site.register(Education, EducationAdmin)
admin.site.register(Work_experience, Work_experienceAdmin)
admin.site.register(Interest, InterestAdmin)