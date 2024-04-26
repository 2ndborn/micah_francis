from django.db import models

class about_me(models.Model):
    content = models.TextField(max_length=500, blank=False)
    image_url = models.URLField(max_length=1024, null=True, blank=True)