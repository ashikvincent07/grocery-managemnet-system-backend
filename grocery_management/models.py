from django.db import models
from django.contrib.auth.models import User

class Grocery(models.Model):

    CATEGORY_CHOICES =  (
            ('VEG', 'Vegetables'),
            ('FRU', 'Fruits'),
            ('DAI', 'Dairy'),
            ('BEV', 'Beverages'),
            ('SNA', 'Snacks'),
            ('OTH', 'Others')
    )

      
    item_id = models.AutoField(primary_key=True)

    item_name = models.CharField(max_length=200)

    category = models.CharField(
        max_length=3,
        choices=CATEGORY_CHOICES,
        default='OTH' 
    )

    price = models.DecimalField(max_digits=10, decimal_places=2)

    quantity = models.IntegerField(default=1)

    expiry_date = models.DateField()
    
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    created_date = models.DateTimeField(auto_now_add=True)

    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.item_name} ({self.quantity})"