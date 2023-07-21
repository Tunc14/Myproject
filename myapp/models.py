from django.db import models

# Create your models here.
class Customer(models.Model):
    id_number= models.CharField(max_length=11, unique=True )
    tc= models.CharField( max_length=11, unique=True )
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    phone = models.CharField( max_length=11)
    city=models.CharField(max_length=100)
    distirct= models.CharField(max_length=50)
    def __str__(self):
        return self.first_name +self.last_name
    