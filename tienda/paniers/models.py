from django.db import models
from comptes.models import TiendaUser
from empanadas.models import Empanada


class Commande(models.Model):
    utilisateur = models.ForeignKey(TiendaUser, on_delete=models.CASCADE)
    date_commande = models.DateTimeField(auto_now_add=True)
    prix_total = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    est_payee = models.BooleanField(default=False)

    def __str__(self):
        return f"Commande {self.id} - Utilisateur: {self.utilisateur.username}"

class LigneCommande(models.Model):
    commande = models.ForeignKey(Commande, related_name='lignes', on_delete=models.CASCADE)
    empanada = models.ForeignKey(Empanada, on_delete=models.CASCADE)
    quantite = models.PositiveIntegerField()
    prix = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Ligne {self.id} - {self.quantite} x {self.empanada.nom}"
