from django import forms
from django.forms import ModelForm, TextInput, ChoiceField, ModelChoiceField

from inventory.models import RawMaterial, Product
from order.models import RawMaterialOrder, ProductOrder


class RawMaterialOrderForm(ModelForm):
    raw_material = forms.ModelChoiceField(queryset=RawMaterial.objects.all())

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
    product = forms.ModelChoiceField(queryset=Product.objects.all())

    class Meta:
        model = ProductOrder
        exclude = ("created_at", "updated_at", "status")
