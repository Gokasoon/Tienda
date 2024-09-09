from django.shortcuts import render
from empanadas.models import Empanada, Ingredient, Composition

def empanadas(request) :
    lesEmpanadas = Empanada.objects.all()
    return render(
        request,
        'empanadas/empanadas.html',
        { 'empanadas' : lesEmpanadas}
    )


def empanada(request, empanada_id) :
    laEmpanada = Empanada.objects.get(idEmpanada = empanada_id)
    compos = Composition.objects.filter(empanada = empanada_id)
    recipe = {}

    for compo in compos :
        recipe[compo.ingredient] = compo.quantite 

    print(recipe)
    return render(
        request,
        'empanadas/empanada.html',
        {'empanada' : laEmpanada,
         'recette' : recipe},

    )


def ingredients(request) :
    lesIngredients = Ingredient.objects.all()
    return render(
        request,
        'empanadas/ingredients.html',
        { 'ingredients' : lesIngredients}
    )