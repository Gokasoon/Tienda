from django.shortcuts import render
from empanadas.models import Empanada, Ingredient

def empanadas(request) :
    lesEmpanadas = Empanada.objects.all()
    return render(
        request,
        'empanadas/empanadas.html',
        { 'empanadas' : lesEmpanadas}
    )


def empanada(request, empanada_id) :
    laEmpanada = Empanada.objects.get(idEmpanada = empanada_id)
    return render(
        request,
        'empanadas/empanada.html',
        {'empanada' : laEmpanada}
    )


def ingredients(request) :
    lesIngredients = Ingredient.objects.all()
    return render(
        request,
        'empanadas/ingredients.html',
        { 'ingredients' : lesIngredients}
    )