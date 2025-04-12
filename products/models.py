from django.db import models
from common.base_models import BaseModels

class Product(BaseModels):
    name = models.CharField(max_length=150)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey('categories.Category', on_delete=models.CASCADE, related_name='products')
    in_stock = models.BooleanField(default=True)
    quantity = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.name} - ${self.price}"

    class Meta:
        ordering = ['-created_at']
