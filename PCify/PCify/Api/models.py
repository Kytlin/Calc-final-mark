from django.db import models

class Api(models.Model):
    title = models.CharField(max_length=80, blank=True, default='')
    description = models.CharField(max_length=500, blank=False, default='')
    published = models.BooleanField(default=False)