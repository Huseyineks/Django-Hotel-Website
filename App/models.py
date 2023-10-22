from django.db import models

class AppModel(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    subject = models.CharField(max_length=50)
    message = models.TextField()
