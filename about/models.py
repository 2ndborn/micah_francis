from django.db import models

class About(models.Model):

    class Meta:
        verbose_name = 'About'

    content = models.TextField(max_length=500, blank=False)
    description = models.CharField(max_length=25, null=True, blank=False)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.content


class Education(models.Model):
    from_date = models.DateField(blank=False)
    to_date = models.DateField(blank=False)
    institution = models.CharField(max_length=100, blank=False)
    qualification = models.CharField(max_length=100, blank=False)
    location = models.CharField(max_length=25, null=True, blank=False)

    def __str__(self):
        return self.qualification


class Work_experience(models.Model):
    from_date = models.DateField(blank=False)
    to_date = models.DateField(blank=True)
    job_title = models.CharField(max_length=25, blank=False)
    company = models.CharField(max_length=25, blank=False)
    location = models.CharField(max_length=25, blank=False)

    def __str__(self):
        return self.job_title


class Achievement(models.Model):
    work_experience = models.ForeignKey(Work_experience, on_delete=models.CASCADE)
    achievement = models.TextField(max_length=250, blank=False)

    def __str__(self):
        return self.achievement


class Interest(models.Model):
    interest = models.TextField(max_length=100, null=True, blank=False)

    def __str__(self):
        return self.interest