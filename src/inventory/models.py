from django.db import models

from base.models import BaseModel


class Product(BaseModel):
    name = models.CharField(max_length=255)
    group = models.CharField(max_length=255)
    details = models.TextField(blank=True, null=True)
    producer = models.ForeignKey('organization.Organization', on_delete=models.CASCADE, related_name='products')

    class Meta:
        ordering = ['-created_at']
        db_table = 'products'
