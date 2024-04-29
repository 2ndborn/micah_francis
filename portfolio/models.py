from django.db import models


class Portfolio(models.Model):

    title = models.CharField(max_length=25, blank=False)
    description = models.TextField(max_length=500, blank=False)
    technologies = models.TextField(max_length=250, blank=False)
    web_address = models.TextField(max_length=500, blank=False)
