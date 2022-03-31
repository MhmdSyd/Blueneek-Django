from django.db import models

# Create your models here.
class Body(models.Model):
    title = models.TextField()
    content = models.TextField()