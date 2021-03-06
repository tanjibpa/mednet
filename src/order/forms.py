from django.forms import ModelForm, ModelChoiceField, NumberInput, Select

from inventory.models import RawMaterial, Product
from order.models import RawMaterialOrder, ProductOrder


class RawMaterialOrderForm(ModelForm):
    raw_material = ModelChoiceField(queryset=RawMaterial.objects.all())

    class Meta:
        model = RawMaterialOrder
        exclude = (
            "created_by",
            "supplier",
            "status",
            "total_price",
        )
        # widgets = {
        #     'raw_material': ChoiceField(
        #         attrs={
        #             'placeholder': None,
        #             'class': 'form-control'
        #         }
        #     )
        # }


class ProductOrderForm(ModelForm):
    # product = ModelChoiceField(queryset=Product.objects.all())

    class Meta:
        model = ProductOrder
        exclude = ("created_at", "updated_at", "status", "created_by", "producer")
        widgets = {
            # "product": Select(attrs={"class": "form-control"}),
            "quantity": NumberInput(attrs={"placeholder": 1, "class": "form-control"}),
        }
