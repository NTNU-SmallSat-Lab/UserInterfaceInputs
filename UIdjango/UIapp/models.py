from django.db import models

# Create your models here.

class template(models.Model):   #Expansion of the administration panel to other topics beyond user administration

    template=models.CharField(max_length=40)

    content=models.CharField(max_length=10000)
