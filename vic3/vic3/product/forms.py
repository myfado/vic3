from django import forms
from .models import Product

class ProductModelForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = [
            'created_at',
            'updated_at',
        ]
 
