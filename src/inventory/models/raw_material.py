from django.db import models

from base.models import BaseModel


class RawMaterial(BaseModel):
    name = models.CharField(max_length=255)
    details = models.TextField()
    supplier = models.ForeignKey('organization.Organization', on_delete=models.CASCADE, related_name='raw_materials')
    price = models.FloatField()

    class Meta:
        db_table = 'raw_materials'
        ordering = ['-created_at']
        permissions = [
            ('supplier_can_create', 'Supplier can create raw material'),
            ('supplier_can_update', 'Supplier can update raw material'),
            ('supplier_can_delete', 'Supplier can delete raw material'),
            ('supplier_can_view', 'Supplier can view raw material'),
            ('pharma_can_view', 'Pharmaceutical can view raw material'),
            ('pharma_can_view_list', 'Pharmaceutical can view raw material list'),
        ]