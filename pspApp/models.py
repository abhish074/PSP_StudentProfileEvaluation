from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class StudentProfileModel(models.Model):
    name = models.CharField(max_length=30)
    gre = models.IntegerField(default=0)
    paper = models.CharField(max_length=30)
    workex = models.IntegerField(default=0)
    undergrad = models.FloatField(default=0)
    quants = models.IntegerField(default=0)
    verbal = models.IntegerField(default=0)
    ielts = models.FloatField(default=0)
    toefl = models.IntegerField(default=0)

    # def __str__(self):
    #     return self.name, self.gre, self.workex
