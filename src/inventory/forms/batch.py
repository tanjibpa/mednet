from django.forms import ModelForm, ModelChoiceField, Select

from inventory.models import Batch


class BatchForm(ModelForm):
    class Meta:
        model = Batch
        fields = ("product",)
        widgets = {"product": Select(choices=[])}
