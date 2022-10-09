
from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length = 255, db_index=True)
    slug = models.SlugField(max_length=255, unique=True)
    
    class Meta:
        verbose_name_plural = 'Categories'
    
    def __str__(self):
        return self.name + ' ' + self.slug

class Product(models.Model):
    CategoryP = models.ForeignKey(Category, related_name = 'product', on_delete=models.CASCADE)
    Company = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'product creator')
    Description = models.TextField(max_length=500)
    ProjTeammLead = models.CharField(max_length=255, default = 'blue starz corps')
    image = models.ImageField(upload_to = 'images/')
    slug = models.SlugField(max_length = 500)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    in_stock = models.BooleanField(default=True)
    #out_of_stock = models.DecimalField(max_digits=1000, decimal_places=0)
    stock_active = models.BooleanField(default=True)
    #stock_active_numb = ...
    stock_up = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name_plural = 'Products'
        ordering = ('created')
    
    def __str__(self):
        return self.Description