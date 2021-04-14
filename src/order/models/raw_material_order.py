from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _

from base.models import BaseModel


class RawMaterialOrder(BaseModel):
    class OrderStatus(models.TextChoices):
        ACTIVE = 'active', _('active')
        REJECTED = 'rejected', _('rejected')
        FULFILLED = 'fulfilled', _('fulfilled')
        CANCELED = 'canceled', _('canceled')

    raw_material = models.ForeignKey('inventory.RawMaterial', on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    supplier = models.ForeignKey('organization.Organization', on_delete=models.CASCADE,
                                 related_name='raw_material_orders')
    status = models.CharField(max_length=20, choices=OrderStatus.choices, default=OrderStatus.ACTIVE)
    quantity = models.IntegerField()
    total_price = models.FloatField()

    def __str__(self):
        return self.raw_material.name

    class Meta:
        db_table = 'raw_material_orders'
        ordering = ['-created_at']
        permissions = [
            ('pharma_can_create_order_raw_material', 'Pharma can create order for raw material'),
            ('pharma_can_cancel_order_raw_material', 'Pharma can cancel order for raw material'),
            ('pharma_can_view_ordered_raw_material', 'Pharma can view ordered raw material'),
            ('supplier_can_fulfill_order_raw_material', 'Supplier can fulfill order for raw material'),
            ('supplier_can_reject_order_raw_material', 'Supplier can reject order for raw material'),
            ('supplier_can_view_order_raw_material_list', 'Supplier can view order list for raw material'),
        ]
