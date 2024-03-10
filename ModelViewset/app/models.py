from django.db import models

# Create your models here.

class Candidate(models.Model):
    Cname = models.CharField(max_length=200)
    Csalary = models.PositiveIntegerField()
    Caddress = models.CharField(max_length=200)
