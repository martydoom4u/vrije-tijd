# Django
from django import forms
# Project
from .models import Weekstaat
from bootstrap_modal_forms.mixins import PopRequestMixin, CreateUpdateAjaxMixin


class WeekstaatForm(PopRequestMixin, CreateUpdateAjaxMixin, forms.ModelForm):
    class Meta:
        model = Weekstaat
        fields = ['jaar', 'week', 'maandag', 'dinsdag' ,'woensdag', 'donderdag', 'vrijdag', 'zaterdag', 'zondag']
