from django.db import models

# Create your models here.

class Ingredient(models.Model) :
    idIngredient = models.AutoField(primary_key = True)
    nomIngredient = models.CharField(max_length = 50)

    def __str__(self) :
        return self.nomIngredient


class Empanada(models.Model) :
    idEmpanada = models.AutoField(primary_key = True)
    nomEmpanada = models.CharField(max_length = 50)
    prix = models.DecimalField(max_digits = 6, decimal_places = 2)

    def __str__(self) :
        return 'empanada ' + self.nomEmpanada + ' (' + str(self.prix) + '€)'

