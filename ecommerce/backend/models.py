from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.deletion import CASCADE, SET_NULL
from django.db.models.fields import BooleanField
from django.db.models.fields.files import ImageField
from django.utils.translation import activate
from ckeditor.fields import RichTextField
from django.utils.text import slugify
# Create your models here.
class User(AbstractUser):
    avt = models.ImageField(upload_to='avt/%Y/%m')
    name = models.CharField(max_length=60,null=True,blank=True)
    phone = models.CharField(max_length=10, null=True,blank=True)
    sex = models.CharField(max_length=5,null=True,blank=True)
    dateofbirth=models.DateField(null=True, blank=True)
    
class ProductImage(models.Model):
    img=models.ImageField(upload_to='static/%Y/%m',default=None)
    

class ProductCategory(models.Model):
    name = models.CharField(max_length=300,null=True, blank=True)
    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=500, null=True,blank=True)
    description = models.TextField(null=True,blank=True)
    price = models.IntegerField(null=True,blank=True)
    sold= models.IntegerField(default=0,null=True, blank=True)
    instruction =models.TextField(null=True, blank=True)
    origin=models.CharField(max_length=50,null=True, blank=True)
    IsActive= models.BooleanField(default=True)
    images=models.ManyToManyField("ProductImage",blank=True,)
    category=models.ForeignKey(ProductCategory,on_delete=models.SET_NULL,null=True)
    
class Rating(models.Model):
    dayandtime = models.DateTimeField(auto_now_add=True)
    ratingpoint = models.IntegerField(null=True,blank=True)
    ratingcomment = models.TextField(null=True, blank=True)
    img = models.ImageField(upload_to='static/%Y/%m',default=None)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

class LoveList(models.Model):
    product_id = models.ForeignKey(Product,on_delete=models.CASCADE)
    customer_id = models.ForeignKey(User, on_delete=models.CASCADE)

class IngredientsTag(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    def __str__(self):
        return self.name

class Ingredients(models.Model):
    name = models.CharField(max_length=300, null=True, blank=True)
    levelOfSave = models.IntegerField(null=True, blank=True)
    Description = models.TextField(null=True,blank=True)
    Tag = models.ManyToManyField("IngredientsTag", blank=True, )
    def __str__(self):
        return self.name