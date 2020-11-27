import asyncio

from django.db import models
import sqlite3


# Create your models here.

class Candidate(models.Model):
    news_desc_01 = models.CharField(max_length=3000, default="")
    news_desc_02 = models.CharField(max_length=3000)
    news_desc_03 = models.CharField(max_length=3000)
    rdate = models.CharField(max_length=10)
    nom_ratio_01 = models.CharField(max_length=10)
    bor_ratio_01 = models.CharField(max_length=10)
    etc_ratio_01 = models.CharField(max_length=10)
    nom_ratio_02 = models.CharField(max_length=10)
    bor_ratio_02 = models.CharField(max_length=10)
    etc_ratio_02 = models.CharField(max_length=10)
    nom_ratio_03 = models.CharField(max_length=10)
    bor_ratio_03 = models.CharField(max_length=10)
    etc_ratio_03 = models.CharField(max_length=10)
    nom_ratio_04 = models.CharField(max_length=10)
    bor_ratio_04 = models.CharField(max_length=10)
    etc_ratio_04 = models.CharField(max_length=10)
    nom_ratio_05 = models.CharField(max_length=10)
    bor_ratio_05 = models.CharField(max_length=10)
    etc_ratio_05 = models.CharField(max_length=10)
    nom_ratio_06 = models.CharField(max_length=10)
    bor_ratio_06 = models.CharField(max_length=10)
    etc_ratio_06 = models.CharField(max_length=10)
    nom_ratio_07 = models.CharField(max_length=10)
    bor_ratio_07 = models.CharField(max_length=10)
    etc_ratio_07 = models.CharField(max_length=10)
    nom_ratio_08 = models.CharField(max_length=10)
    bor_ratio_08 = models.CharField(max_length=10)
    etc_ratio_08 = models.CharField(max_length=10)
    nom_ratio_09 = models.CharField(max_length=10)
    bor_ratio_09 = models.CharField(max_length=10)
    etc_ratio_09 = models.CharField(max_length=10)
    nom_ratio_10 = models.CharField(max_length=10)
    bor_ratio_10 = models.CharField(max_length=10)
    etc_ratio_10 = models.CharField(max_length=10)
    nom_ratio_11 = models.CharField(max_length=10)
    bor_ratio_11 = models.CharField(max_length=10)
    etc_ratio_11 = models.CharField(max_length=10)
    nom_ratio_12 = models.CharField(max_length=10)
    bor_ratio_12 = models.CharField(max_length=10)
    etc_ratio_12 = models.CharField(max_length=10)

    #    name = models.CharField(max_length=10)
    #    introduction = models.TextField()
    #    area = models.CharField(max_length=15)
    #    number = models.IntegerField(default=0)

    def __str__(self):
        return self.news_desc_01


async def test1():
    asyncio.run(test1())
