from django.db import models

from base.models import BaseModel


class Product(BaseModel):
    name = models.CharField(max_length=255)
    group = models.CharField(max_length=255)
    details = models.TextField(blank=True, null=True)
    producer = models.ForeignKey(
        "organization.Organization", on_delete=models.CASCADE, related_name="products"
    )

    class Meta:
        ordering = ["-created_at"]
        db_table = "products"
        permissions = [
            ("pharma_can_create", "Pharma can create product"),
            ("pharma_can_update", "Pharma can update product"),
            ("pharma_can_delete", "Pharma_can_delete_product"),
            ("pharma_can_view", "Pharma can view product"),
            ("pharma_can_view_list", "Pharma can view product list"),
        ]
