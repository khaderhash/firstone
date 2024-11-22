from django.db import models
from django.contrib.auth.models import User
# Create your models here.


    
class Category (models.TextChoices):
    Computer = 'computer'
    child = 'child'
    animals = 'animals'
    home = 'home'


class Product(models.Model):
    name = models.CharField(blank=False,default="",max_length=50)
    description = models.TextField(blank=False, default="",max_length=200)
    # price = models.DecimalField(blank=False,default=0,max_digits=8)
    brand = models.CharField(blank=False,default="",max_length=50)
    category=models.CharField(max_length=30,choices=Category.choices)
    rating = models.DecimalField(max_digits=5, decimal_places=2,default=0)
    stock = models.IntegerField(default=0)
    creatAt = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)