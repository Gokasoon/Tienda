from django.shortcuts import render
from paniers.models import Commande, LigneCommande
from comptes.models import TiendaUser

def afficherPanier(request):
    panier = None
    lignes = []
    user = TiendaUser.objects.get(id=request.user.id)
    non_payees = Commande.objects.filter(utilisateur=user, est_payee=False)

    if non_payees.exists():
        panier = non_payees[0]
        lignes = LigneCommande.objects.filter(commande=panier)

        total_global = 0
        for ligne in lignes:
            ligne.total = ligne.quantite * ligne.prix  
            total_global += ligne.total  

    return render(
        request,
        'paniers/panier.html',
        {
            'panier': panier,
            'lignes': lignes,
            'total': total_global 
        },
    )
