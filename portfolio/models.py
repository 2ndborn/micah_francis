from django.db import models


class Portfolio(models.Model):

    title = models.CharField(max_length=25, blank=False)
    description = models.TextField(max_length=500, blank=False)
    technologies = models.TextField(max_length=250, blank=False)
    web_address = models.CharField(max_length=500, blank=False)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
