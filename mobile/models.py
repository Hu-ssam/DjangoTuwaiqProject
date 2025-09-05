from django.db import models, migrations
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    icon = models.CharField(max_length=100, blank=True)
    def __str__(self):
        return self.name


class Cosutmer(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=250)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    
class Products(models.Model):
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10,decimal_places=6)
    storage = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    image = models.ImageField(upload_to='mobile/images')
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    session_id = models.CharField(max_length=100, null=True, blank=True)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity = models.PositiveBigIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
