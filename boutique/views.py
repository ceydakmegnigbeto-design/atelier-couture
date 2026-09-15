from django.shortcuts import get_object_or_404, redirect, render

from .forms import CommandeForm, MessageContactForm
from .models import Creation


def accueil(request):
    creations = Creation.objects.filter(
        disponible=True
    ).order_by('-date_creation')

    recherche = request.GET.get('recherche', '').strip()
    categorie = request.GET.get('categorie', '').strip()

    if recherche:
        creations = creations.filter(
            nom__icontains=recherche
        )

    if categorie:
        creations = creations.filter(
            categorie=categorie
        )

    return render(
        request,
        'boutique/accueil.html',
        {
            'creations': creations,
            'categories': Creation.CATEGORIES,
            'recherche': recherche,
            'categorie_selectionnee': categorie,
        }
    )


def detail_creation(request, creation_id):
    creation = get_object_or_404(
        Creation,
        id=creation_id,
        disponible=True
    )

    return render(
        request,
        'boutique/detail.html',
        {
            'creation': creation,
        }
    )


def commander(request, creation_id):
    creation = get_object_or_404(
        Creation,
        id=creation_id,
        disponible=True
    )

    if request.method == 'POST':
        formulaire = CommandeForm(request.POST)

        if formulaire.is_valid():
            commande = formulaire.save(commit=False)
            commande.creation = creation
            commande.save()

            return redirect('confirmation', commande_id=commande.id)
    else:
        formulaire = CommandeForm()

    return render(
        request,
        'boutique/commande.html',
        {
            'creation': creation,
            'formulaire': formulaire,
        }
    )


def confirmation(request, commande_id):
    return render(
        request,
        'boutique/confirmation.html',
        {
            'commande_id': commande_id,
        }
    )
def contact(request):
    if request.method == 'POST':
        formulaire = MessageContactForm(request.POST)

        if formulaire.is_valid():
            formulaire.save()

            return redirect('contact_confirmation')
    else:
        formulaire = MessageContactForm()

    return render(
        request,
        'boutique/contact.html',
        {
            'formulaire': formulaire,
        }
    )

def contact_confirmation(request):
    return render(
        request,
        'boutique/contact_confirmation.html'
    )