# Django
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views import generic
# Project
from .forms import todoForm
from .models import Todo
from bootstrap_modal_forms.mixins import PassRequestMixin, DeleteAjaxMixin


class Index(generic.ListView):
    model = Todo
    context_object_name = 'todos'
    template_name = 'todo/index.html'


# Create
class todoCreateView(PassRequestMixin, SuccessMessageMixin,
                     generic.CreateView):
    template_name = 'todo/create_todo.html'
    form_class = todoForm
    success_message = 'Success: todo is aangemaakt was created.'
    success_url = reverse_lazy('index')


# Update
class todoUpdateView(PassRequestMixin, SuccessMessageMixin,
                     generic.UpdateView):
    model = Todo
    template_name = 'todo/update_todo.html'
    form_class = todoForm
    success_message = 'Success: todo is geupdate'
    success_url = reverse_lazy('index')


# Read
class todoReadView(generic.DetailView):
    model = Todo
    template_name = 'todo/read_todo.html'


# Delete
class todoDeleteView(DeleteAjaxMixin, generic.DeleteView):
    model = Todo
    template_name = 'todo/delete_todo.html'
    success_message = 'Success: todo is verwijdert.'
    success_url = reverse_lazy('index')