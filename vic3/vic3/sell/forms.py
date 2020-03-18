from django import forms
from .models import *
from django.forms.models import inlineformset_factory
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Fieldset, Div, HTML, ButtonHolder, Submit
from .custom_layout_object import *

class SellForm(forms.ModelForm):

    class Meta:
        model = Sell
        exclude = ('created_at','updated_at',)

    def __init__(self, *args, **kwargs):
        super(SellForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = True
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-3 create-label'
        self.helper.field_class = 'col-md-9'
        self.helper.layout = Layout(
            Div(
                Field('customer'),
                Field('discount_cc'),
                Field('discount_ci'),
                Field('delivery'),
                Field('money_received'),
                # Field('created_at'),
                # Field('updated_at'),
                Fieldset('Add items',
                    Formset('items')),
                Field('note'),
                HTML("<br>"),
                ButtonHolder(Submit('submit', 'save')),
                )
            )


class SellItemForm(forms.ModelForm):

    class Meta:
        model = SellItem
        exclude = ()

SellItemFormSet = inlineformset_factory(
    Sell, SellItem, form=SellItemForm,
    fields=['sell', 'product', 'quantity'], extra=10, can_delete=True
    )
