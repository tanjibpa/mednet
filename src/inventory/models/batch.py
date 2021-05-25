from uuid import uuid4

from django.db import models

from base.models import BaseModel


class Batch(BaseModel):
    batch_number = models.CharField(max_length=50, unique=True)
    product = models.ForeignKey(
        "inventory.Product", related_name="batches", on_delete=models.CASCADE
    )

    class Meta:
        ordering = ["created_at"]
        db_table = "batches"
        permissions = [
            ("pharma_can_create_batch", "Pharma can create batch"),
            ("pharma_can_update_batch", "Pharma can update batch"),
            ("pharma_can_view_batch", "Pharma can view batch"),
            ("retailer_can_order_batch", "Retailer can order batch"),
            ("retailer_can_view_batch", "Retailer can view batch"),
        ]

    def save(self, *args, **kwargs):
        self.batch_number = uuid4().hex[:6].upper()
        super().save(*args, **kwargs)
