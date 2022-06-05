from django.db import models

class Records(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    email = models.CharField(max_length=200)
    createdAt = models.DateTimeField('date published')
