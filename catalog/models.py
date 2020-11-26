from django.db import models
import sqlite3


# Create your models here.

class Candidate(models.Model):
    name = models.CharField(max_length=10)
    introduction = models.TextField()
    area = models.CharField(max_length=15)
    party_number = models.IntegerField(default=0)
    image = models.ImageField(upload_to='images/', blank=True, null=True)

    def __str__(self):
        return self.name

class Photo(models.Model):
    post = models.ForeignKey(Candidate, on_delete=models.CASCADE, null=True)
    image = models.ImageField(upload_to='images/', blank=True, null=True)