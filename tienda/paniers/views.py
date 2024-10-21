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
        
        tot = 0
        for ligne in lignes:
            tot += ligne.prix
    return render(
        request,
        'paniers/panier.html',
        {
            'panier': panier,
            'lignes': lignes,
            'total' : tot
        },
    )
