from django.db import models

class Details(models.Model):
     eventname = models.CharField(max_length = 50)
     firstname = models.CharField(max_length = 50)
     lastname  = models.CharField(max_length = 50)
     info1 = models.CharField(max_length = 50)
     date = models.DateField()
