from django.db import models

class web(models.Model):
  name = models.CharField(max_length=100, default=None)
  number = models.CharField(max_length=100, default=None)
