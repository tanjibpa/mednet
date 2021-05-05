from django.db import models

from base.models import BaseModel


class Batch(BaseModel):
    batch_number = models.CharField(max_length=50, unique=True)
    product = models.ForeignKey(
        "inventory.Product", related_name="batches", on_delete=models.CASCADE
    )

    class Meta:
        ordering = ["-created_at"]
        db_table = "batches"
        permissions = [
            ("pharma_can_create", "Pharma can create batch"),
            ("pharma_can_update", "Pharma can update batch"),
            ("pharma_can_view", "Pharma can view batch"),
            ("retailer_can_order", "Retailer can order batch"),
            ("retailer_can_view", "Retailer can view batch"),
        ]
