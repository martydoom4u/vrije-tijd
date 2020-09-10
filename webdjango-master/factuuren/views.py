# Django
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views import generic
# Project
from .forms import FactuurForm
from .models import Factuur
from bootstrap_modal_forms.mixins import PassRequestMixin, DeleteAjaxMixin


class Index(generic.ListView):
    model = Factuur
    context_object_name = 'Factuurens'
    template_name = 'factuuren/index.html'


# Create
class FactuurenCreateView(PassRequestMixin, SuccessMessageMixin,
                     generic.CreateView):
    template_name = 'factuuren/create_factuur.html'
    form_class = FactuurForm
    success_message = 'Success: facatuur  is aangemaakt was created.'
    success_url = reverse_lazy('indexf')


# Update
class FactuurenUpdateView(PassRequestMixin, SuccessMessageMixin,
                     generic.UpdateView):
    model = Factuur
    template_name = 'factuuren/update_facatuuren.html'
    form_class = FactuurForm
    success_message = 'Success: facatuur is geupdate'
    success_url = reverse_lazy('indexf')


# Read
class FactuurenReadView(generic.DetailView):
    model = FactuurForm
    template_name = 'factuuren/read_facatuuren.html'


# Delete
class FactuurenDeleteView(DeleteAjaxMixin, generic.DeleteView):
    model = FactuurForm
    template_name = 'factuuren/delete_facatuuren.html'
    success_message = 'Success: facatuur is verwijdert.'
    success_url = reverse_lazy('indexf')