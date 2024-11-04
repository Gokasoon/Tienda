from django.shortcuts import render, redirect
from paniers.models import Commande, LigneCommande
from comptes.models import TiendaUser
from empanadas.models import Empanada

def afficherPanier(request) :
    panier = None
    lignes = []
    user = TiendaUser.objects.get(id=request.user.id)
    non_payees = Commande.objects.filter(utilisateur=user, est_payee=False)

    if non_payees.exists():
        panier = non_payees[0]
        lignes = LigneCommande.objects.filter(commande=panier)

        total_global = 0
        for ligne in lignes: 
            total_global += ligne.prix  

    return render(
        request,
        'paniers/panier.html',
        {
            'panier': panier,
            'lignes': lignes,
            'total': total_global 
        },
    )


def ajouterEmpanadaAuPanier(request, empanada_id):
    user = TiendaUser.objects.get(id=request.user.id)
    empanada = Empanada.objects.get(idEmpanada=empanada_id)  
    non_payees = Commande.objects.filter(utilisateur=user, est_payee=False)

    if non_payees.exists():
        panier = non_payees[0]
    else:
        panier = Commande(utilisateur=user)  
        panier.save()

    panier.prix_total += empanada.prix
    panier.save()

    lignes = LigneCommande.objects.filter(commande=panier)
    ligne_empanada = lignes.filter(empanada=empanada).first()

    if ligne_empanada is None:
        ligne_empanada = LigneCommande(
            commande=panier,
            empanada=empanada,
            quantite=0,
            prix=0
        )
    
    ligne_empanada.quantite += 1
    ligne_empanada.prix = ligne_empanada.quantite * empanada.prix  
    ligne_empanada.save()

    return redirect('/cart')


def retirerDuPanier(request, empanada_id) :
    user = TiendaUser.objects.get(id=request.user.id)
    empanada = Empanada.objects.get(idEmpanada=empanada_id)  
    non_payees = Commande.objects.filter(utilisateur=user, est_payee=False)

    if non_payees.exists() :
        panier = non_payees[0]
    else :
        redirect('/empanadas')

    lignes = LigneCommande.objects.filter(commande=panier)
    ligne_empanada = lignes.filter(empanada=empanada).first()

    if ligne_empanada is None :
        redirect('/empanadas')

    panier.prix_total -= ligne_empanada.prix

    ligne_empanada.delete()

    lignes = LigneCommande.objects.filter(commande=panier)
    if lignes is None :
        panier.delete()
    else :
        panier.save()

    return redirect('/cart')

