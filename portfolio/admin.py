from django.contrib import admin
from .models import Portfolio


class PortfolioAdmin(admin.ModelAdmin):

    list_display = (
        'title',
        'description',
        'technologies',
        'web_address',
        'github',
        'image',
        'image_description',
    )

admin.site.register(Portfolio, PortfolioAdmin)