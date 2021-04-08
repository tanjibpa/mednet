from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User

from base.models import BaseModel


class Organization(BaseModel):
    class OrgType(models.TextChoices):
        PRODUCER = 'producer', _('Producer')
        SELLER = 'seller', _('Seller')

    name = models.CharField(max_length=255)
    org_type = models.CharField(max_length=20, choices=OrgType.choices)
    contact = models.CharField(max_length=20)
    address = models.TextField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=BaseModel.StatusChoices.choices,
                              default=BaseModel.StatusChoices.INACTIVE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='organizations')

    class Meta:
        ordering = ['-created_at']
        db_table = 'organizations'
