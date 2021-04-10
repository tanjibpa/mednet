from django.forms import ModelForm, TextInput

from order.models import Order


class OrderForm(ModelForm):
    class Meta:
        model = Order
        exclude = ('created_by',)
        widgets = {
            'product': TextInput(
                attrs={
                    'placeholder': 'Product',
                    
                }
            )
        }
