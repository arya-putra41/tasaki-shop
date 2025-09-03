from django.db import models
import uuid

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=255)
    stock = models.PositiveIntegerField(default=0)
    price = models.IntegerField(default=0)
    description = models.TextField()
    thumbnail = models.URLField()
    category = models.CharField(max_length=255)
    is_featured = models.BooleanField(default=False)

    def __str__(self):
        return self.name 
