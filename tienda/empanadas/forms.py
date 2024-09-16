from django.forms import ModelForm
from empanadas.models import Ingredient

class IngredientForm(ModelForm) :
    class Meta:
        model = Ingredient
        fields = ['nomIngredient']