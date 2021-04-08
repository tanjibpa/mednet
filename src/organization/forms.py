from django.forms import ModelForm, TextInput, Select
from organization.models import Organization


class OrganizationForm(ModelForm):
    class Meta:
        model = Organization
        exclude = ('user', 'status',)
        widgets = {
            'name': TextInput(
                attrs={
                    'placeholder': 'Name',
                    'class': 'form-control'
                }
            ),
            'org_type': Select(
                attrs={
                    'class': 'form-control'
                }
            ),
            'contact': TextInput(
                attrs={
                    'placeholder': 'Contact',
                    'class': 'form-control'
                }
            ),
            'address': TextInput(
                attrs={
                    'placeholder': 'Address',
                    'class': 'form-control'
                }
            )
        }
