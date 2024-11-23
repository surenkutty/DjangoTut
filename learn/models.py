from django.db import models


class Product(models.Model):
    name=models.CharField(max_length=50)
    description=models.CharField(max_length=500)
    mrp_price=models.IntegerField()
    categroy=models.CharField(max_length=100)
    offer_price=models.IntegerField()
    
    date=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name


    
    
    

# Create your models here.
