from django import forms

from .models import Customer


class CustomerModelForm(forms.ModelForm):
    class Meta:
        model = Customer
        exclude = [
            'created_at',
            'updated_at',
        ]
