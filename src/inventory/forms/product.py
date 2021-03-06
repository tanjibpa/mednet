from django.forms import ModelForm, TextInput, NumberInput

from inventory.models import Product


class ProductForm(ModelForm):
    class Meta:
        model = Product
        exclude = ("producer",)
        widgets = {
            "name": TextInput(attrs={"placeholder": "Name", "class": "form-control"}),
            "group": TextInput(attrs={"placeholder": "Group", "class": "form-control"}),
            "details": TextInput(
                attrs={"placeholder": "Details", "class": "form-control"}
            ),
            "price": NumberInput(
                attrs={"placeholder": 0.0, "class": "form-control"}
            )
        }
