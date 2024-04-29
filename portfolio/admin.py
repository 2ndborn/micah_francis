from django.contrib import admin
from .models import Portfolio


class PortfolioAdmin(admin.ModelAdmin):

    list_display = (
        'title',
        'description',
        'technologies',
        'web_address',
        'image',
    )

admin.site.register(Portfolio, PortfolioAdmin)