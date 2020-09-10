from django.shortcuts import render
from django.contrib.auth.decorators import login_required



@login_required
def profiel(request):
    return render(request, 'profiel/profiel.html')


