from django import forms
# Project
from .models import Contract
from bootstrap_modal_forms.mixins import PopRequestMixin, CreateUpdateAjaxMixin


class ContractForm(PopRequestMixin, CreateUpdateAjaxMixin, forms.ModelForm):
    class Meta:
        model = Contract
        fields = ['organisatie','tussenpersoon', 'tussenpersoon_email','uurtarief','functie','begindatum','einddatum','status']