from django.forms import ModelForm
from empanadas.models import Ingredient, Empanada, Composition

class IngredientForm(ModelForm) :
    class Meta:
        model = Ingredient
        fields = ['nomIngredient']


class EmpanadaForm(ModelForm) :
    class Meta:
        model = Empanada
        fields = ['nomEmpanada', 'prix']


class CompositionForm(ModelForm) :
    class Meta:
        model = Composition
        fields = ['ingredient', 'quantite']