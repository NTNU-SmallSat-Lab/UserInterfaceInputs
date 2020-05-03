from django.db import models

# Create your models here.

class template(models.Model):

    template=models.CharField(max_length=40)

    content=models.CharField(max_length=10000)

class option(models.Model):

    priority=models.IntegerField()

    multiple_passes=models.BooleanField()

    starttime=models.IntegerField() #UNIX time stamp