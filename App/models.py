from django.db import models

class AppModel(models.Model):
    name = models.CharField(max_length=50,name='Name')
    email = models.CharField(max_length=100,name='E-mail')
    subject = models.CharField(max_length=50,name='Subject')
    message = models.TextField(name='Message')
