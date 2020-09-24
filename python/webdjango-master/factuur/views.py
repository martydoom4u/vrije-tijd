from __future__ import unicode_literals
from django.shortcuts import render
from .models import Factuur
from django.views import generic
from django.shortcuts import render
#from organisatie.models import Organisatie
from weekstaat.models import Weekstaat
#from contract.models import Contractregel
from django.contrib.auth.decorators import login_required


class index(generic.ListView):
    template_name = 'factuur/index.html'


def toevoegen(request):
    return render(request, 'factuur/toevoegen.html', {
        'organisatie': Organisatie.objects.filter(admin=request.user),
        'contractregel': Contractregel.objects.filter(persoon=request.user),
        'weekstaat': Weekstaat.objects.filter(werknemer=request.user)
        })


def toegevoegd(request):
    contractRegel = Contractregel.objects.get(pk=request.POST['contractregel'])

    Factuur.objects.create(
        factuurdatum=request.POST['factuurdatum'],
        vervaldatum=request.POST['vervaldatum'],
        werknemer=request.user,
        organisatie_werknemer=Organisatie.objects.get(pk=request.POST['organisatie']),
        contractregel=contractRegel,
        contract=contractRegel.contract,
        weekstaat=Weekstaat.objects.get(pk=request.POST['weekstaat']),
        totaal_excl_btw=request.POST['totaalEX'],
        totaal_incl_btw=request.POST['totaalIN'],
        btw_procent=request.POST['btw_procent'],
        btw_bedrag=request.POST['btw_bedrag']
        )
