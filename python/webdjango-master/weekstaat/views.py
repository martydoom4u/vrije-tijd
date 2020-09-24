# Django
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views import generic
# Project
from .forms import WeekstaatForm
from .models import Weekstaat
from bootstrap_modal_forms.mixins import PassRequestMixin, DeleteAjaxMixin


class Index(generic.ListView):
    model = Weekstaat
    context_object_name = 'Weekstaaten'
    template_name = 'weekstaat/index.html'


# Create
class WeekstaatCreateView(PassRequestMixin, SuccessMessageMixin,
                     generic.CreateView):
    template_name = 'weekstaat/create_weekstaat.html'
    form_class = WeekstaatForm
    success_message = 'Success: weekstaat is aangemaakt was created.'
    success_url = reverse_lazy('indexs')


# Update
class WeekstaatUpdateView(PassRequestMixin, SuccessMessageMixin,
                     generic.UpdateView):
    model = Weekstaat
    template_name = 'weekstaat/update_weekstaat.html'
    form_class = WeekstaatForm
    success_message = 'Success: weekstaat is geupdate'
    success_url = reverse_lazy('indexs')


# Read
class WeekstaatReadView(generic.DetailView):
    model = Weekstaat
    template_name = 'weekstaat/read_weekstaat.html'


# Delete
class WeekstaatDeleteView(DeleteAjaxMixin, generic.DeleteView):
    model = Weekstaat
    template_name = 'weekstaat/delete_weekstaat.html'
    success_message = 'Success: weekstaat is verwijdert.'
    success_url = reverse_lazy('indexs')