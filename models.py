from django.db import models

# Create your models here.
class Contactus(models.Model):
    email = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    desc = models.TextField()
    date = models.DateField()


