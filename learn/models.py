from django.db import models

class Category(models.Model):
    category_name=models.CharField(max_length=50)
    
    def __str__(self):
        return self.category_name

class Product(models.Model):
    # category=models.ForeignKey(Category,null=True,blank=True,on_delete=models.CASCADE,related_name='category')
    name=models.CharField(max_length=50)
    offer_price=models.IntegerField()
    description=models.CharField(max_length=500)
    mrp_price=models.IntegerField()
    category=models.CharField(max_length=50)
    
    date=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name


    
    
    

# Create your models here.
