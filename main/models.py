from django.db import models
import uuid

# Create your models here.

class Product(models.Model):
    CATEGORY_CHOICES = [
        ('shoes', 'Shoes'),
        ('jersey', 'Jersey'),
        ('pants', 'Pants'),
        ('pad', 'Pad'),
        ('headwear', 'Headwear'),
        ('gloves', 'Gloves'),
        ('ball', 'Ball'),
        ('bag', 'Bag'),
        ('bottle', 'Bottle'),
        ('other', 'Other'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    stock = models.PositiveIntegerField(default=0)
    price = models.IntegerField(default=0)
    description = models.TextField()
    thumbnail = models.URLField(blank=True, null=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='other')
    is_featured = models.BooleanField(default=False)

    def __str__(self):
        return self.name 
    
    def consume_stock(self, amount):
        if self.stock < amount:
            return
        else:
            stock -= amount
