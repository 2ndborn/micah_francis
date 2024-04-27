from django.db import models

class About_me(models.Model):

    class Meta:
        verbose_name = 'About'

    content = models.TextField(max_length=500, blank=False)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.content


class Education(models.Model):
    from_date = models.DateTimeField(blank=False)
    to_date = models.DateTimeField(blank=False)
    institution = models.CharField(max_length=100, blank=False)
    qualifation = models.CharField(max_length=100, blank=False)

    def __str__(self):
        return self.qualifation


class Work_experience(models.Model):
    from_date = models.DateTimeField(blank=False)
    to_date = models.DateTimeField(blank=True)
    job_title = models.CharField(max_length=25, blank=False)
    company = models.CharField(max_length=25, blank=False)
    location = models.CharField(max_length=25, blank=False)
    achievement1 = models.TextField(max_length=25, blank=False)
    achievement2 = models.TextField(max_length=25, blank=False)
    achievement3 = models.TextField(max_length=25, blank=False)
    achievement4 = models.TextField(max_length=25, blank=False)
    achievement5 = models.TextField(max_length=25, blank=False)

    def __str__(self):
        return self.job_title

class Interest(models.Model):
    interest = models.TextField(max_length=100, null=True, blank=False)

    def __str__(self):
        return self.interest