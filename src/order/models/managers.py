from django.db import models


class SupplierOrderList(models.Manager):
    def supplier_order(self):
        return super().get_queryset().filter(producer__org_type="supplier")
