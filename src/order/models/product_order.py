from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _

from base.models import BaseModel
from order.models.managers import SupplierOrderList


class ProductOrder(BaseModel):
    class OrderStatus(models.TextChoices):
        ACTIVE = "active", _("active")
        REJECTED = "rejected", _("rejected")
        FULFILLED = "fulfilled", _("fulfilled")
        CANCELED = "canceled", _("canceled")

    product = models.ForeignKey("inventory.Product", on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    producer = models.ForeignKey(
        "organization.Organization", on_delete=models.CASCADE, related_name="orders"
    )
    status = models.CharField(
        max_length=20, choices=OrderStatus.choices, default=OrderStatus.ACTIVE
    )
    quantity = models.IntegerField()

    objects = models.Manager()
    supplier_order_objects = SupplierOrderList()

    class Meta:
        db_table = "product_orders"
        ordering = ["-created_at"]
        permissions = [
            ("supplier_order_list", "Can view order request list for the supplier"),
            ("pharma_order_list", "Can view order list made by pharma"),
            ("retailer_order_list", "Can view order list made by retailer"),
            ("retailer_create_order", "Retailer can create order"),
        ]
