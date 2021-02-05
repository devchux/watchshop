from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Item(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to="items")
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=10000)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Customer(models.Model):
    customer = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to="profile", null=True, default="profile/logo.png")

    def __str__(self):
        return self.name

class Order(models.Model):
    STATUS = (
        ('pending', 'pending'),
        ('done', 'done')
    )
    customer = models.ForeignKey(Customer, null=True, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, blank=True, null=True, on_delete=models.SET_NULL)
    status = models.CharField(default='pending', null=True, choices=STATUS, max_length=100)
    date_created = models.DateTimeField(auto_now_add=True)