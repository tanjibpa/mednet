from django import forms
from django.forms import ModelForm, TextInput, ChoiceField, ModelChoiceField

from inventory.models import RawMaterial
from order.models import RawMaterialOrder


class OrderForm(ModelForm):
    raw_material = forms.ModelChoiceField(queryset=RawMaterial.objects.all())

    class Meta:
        model = RawMaterialOrder
        exclude = ('created_by', 'supplier', 'status', 'total_price',)
        # widgets = {
        #     'raw_material': ChoiceField(
        #         attrs={
        #             'placeholder': None,
        #             'class': 'form-control'
        #         }
        #     )
        # }
