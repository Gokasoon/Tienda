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
    image = models.ImageField(default = 'imagesEmpanadas/default.png', upload_to = 'imagesEmpanadas/')

    def __str__(self) :
        return 'empanada ' + self.nomEmpanada + ' (prix: ' + str(self.prix) + '€)'


class Composition(models.Model) :
    class Meta :
        unique_together = ('ingredient', 'empanada')
    
    idComposition = models.AutoField(primary_key = True)
    ingredient = models.ForeignKey(Ingredient, on_delete = models.CASCADE)
    empanada = models.ForeignKey(Empanada, on_delete = models.CASCADE)
    quantite = models.CharField(max_length = 100)

    def __str__(self) :
        return self.ingredient.nomIngredient + " fait partie de l'empanada" \
                + " '" + self.empanada.nomEmpanada + "' (qt: " + self.quantite + "g)"
    