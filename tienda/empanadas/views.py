from django.shortcuts import render
from empanadas.models import Empanada, Ingredient, Composition
from empanadas.forms import IngredientForm, EmpanadaForm

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


def formulaireCreationIngredient(request) :
    return render(
        request,
        'empanadas/formulaireCreationIngredient.html'
    )


def creerIngredient(request) :
    form = IngredientForm(request.POST)
    if form.is_valid() :
        nomIngr = form.cleaned_data['nomIngredient']
        ingr = Ingredient()
        ingr.nomIngredient = nomIngr
        ingr.save()
        return render(
            request,
            'empanadas/traitementFormulaireCreationIngredient.html',
            { 'nom' : nomIngr },
        )
    else :
        return render(
            request,
            'empanadas/formulaireNonValide.html',
            { 'erreurs' : form.errors },
        )

def formulaireCreationEmpanada(request) :
    return render(
        request,
        'empanadas/formulaireCreationEmpanada.html'
    )


def creerEmpanada(request) :
    form = EmpanadaForm(request.POST)
    if form.is_valid() :
        nomEmp = form.cleaned_data['nomEmpanada']
        prixEmp = form.cleaned_data['prix']
        emp = Empanada()
        emp.nomEmpanada = nomEmp
        emp.prix = prixEmp
        emp.save()
        return empanada(request, emp.idEmpanada)
    else :
        return render(
            request,
            'empanadas/formulaireNonValide.html',
            { 'erreurs' : form.errors },
        )
