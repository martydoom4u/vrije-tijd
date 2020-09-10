# Django
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views import generic
# Project
from .forms import ContractForm
from .models import Contract
from bootstrap_modal_forms.mixins import PassRequestMixin, DeleteAjaxMixin


class Index(generic.ListView):
    model = Contract
    context_object_name = 'Contracts'
    template_name = 'contract/index.html'


# Create
class ContractCreateView(PassRequestMixin, SuccessMessageMixin,
                     generic.CreateView):
    template_name = 'Contract/create_contract.html'
    form_class = ContractForm
    success_message = 'Success: contract is aangemaakt was created.'
    success_url = reverse_lazy('Index')


# Update
class ContractUpdateView(PassRequestMixin, SuccessMessageMixin,
                     generic.UpdateView):
    model = Contract
    template_name = 'Contract/update_contract.html'
    form_class = ContractForm
    success_message = 'Success: contract is geupdate'
    success_url = reverse_lazy('Index')


# Read
class ContractReadView(generic.DetailView):
    model = Contract
    template_name = 'contract/read_contract.html'


# Delete
class ContractDeleteView(DeleteAjaxMixin, generic.DeleteView):
    model = Contract
    template_name = 'Contract/delete_contract.html'
    success_message = 'Success: contract is verwijdert.'
    success_url = reverse_lazy('Index')