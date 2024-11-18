from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin
from .managers import UserManager

from django.utils.translation import gettext_lazy as _ 
# Create your models here.
class User(AbstractBaseUser,PermissionsMixin):
    email=models.EmailField(max_length=225,unique=True,verbose_name=_("Email Adreess"))
    first_name=models.CharField(max_length=100,unique=True,verbose_name=_("First Name"))
    last_name=models.CharField(max_length=100,unique=True,verbose_name=_("Last Name"))
    is_staff=models.BooleanField(default=False)
    is_superuser=models.BooleanField(default=False)
    is_verified=models.BooleanField(default=False)
    is_activate=models.BooleanField(default=True)
    date_joined=models.DateTimeField(auto_now_add=True)
    last_login=models.DateTimeField(auto_now=True)
    USERNAME_FIELD="email"
    REQUIRED_FIELDS=["first_name","last_name"]
    objects=UserManager()
    def __str__(self):
        return self.email
    
    @property
    def get_full_name(self):
        return f"{self.first_name}{self.last_name}"
    def tokens(self):
        pass

# class Product(models.Model):
#     title=models.CharField(max_length=120)
#     content=models.TextField(blank=True,null=True)
#     price=models.DecimalField(max_digits=15,decimal_places=2,default=99.99)
    
    
