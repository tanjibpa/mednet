from django.forms import ModelForm, TextInput

from inventory.models import RawMaterial


class RawMaterialForm(ModelForm):
    class Meta:
        model = RawMaterial
        exclude = ("supplier",)
        widgets = {
            "name": TextInput(attrs={"placeholder": "Name", "class": "form-control"}),
            "details": TextInput(
                attrs={"placeholder": "Details", "class": "form-control"}
            ),
            "price": TextInput(attrs={"placeholder": "Price", "class": "form-control"}),
        }
