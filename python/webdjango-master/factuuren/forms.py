from django import forms
# Project
from .models import Factuur
from bootstrap_modal_forms.mixins import PopRequestMixin, CreateUpdateAjaxMixin


class FactuurForm(PopRequestMixin, CreateUpdateAjaxMixin, forms.ModelForm):
    class Meta:
        model = Factuur
        fields = ['factuurdatum','vervaldatum', 'werknemer','weekstaat','totaal_excl_btw','totaal_incl_btw','btw_procent', 'btw_bedrag']