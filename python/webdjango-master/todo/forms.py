from django import forms
# Project
from .models import Todo
from bootstrap_modal_forms.mixins import PopRequestMixin, CreateUpdateAjaxMixin


class todoForm(PopRequestMixin, CreateUpdateAjaxMixin, forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['actie_naam','actie_aanmaakdatum', 'actie_einddatum','actie_eindtijdstip']