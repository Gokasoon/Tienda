from django.shortcuts import render, redirect
from empanadas.models import Empanada, Ingredient, Composition
from empanadas.forms import IngredientForm, EmpanadaForm, CompositionForm
from django.contrib.auth.models import User

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
    ingrs = Ingredient.objects.all()
    recipe = {}

    for compo in compos :
        recipe[compo.ingredient] = compo.quantite 

    print(recipe)
    return render(
        request,
        'empanadas/empanada.html',
        {'empanada' : laEmpanada,
         'recette' : recipe,
         'ingredients' : ingrs},
    )

def supprimerEmpanada(request, empanada_id) :
    empanada = Empanada.objects.get(idEmpanada = empanada_id)
    empanada.delete()
    return redirect('/empanadas')


def afficherFormulaireModificationEmpanada(request, empanada_id) :
    user = None
    if request.user.is_staff : 
        emp = Empanada.objects.get(idEmpanada = empanada_id)
        user = User.objects.get(id=request.user.id)
        return render(
            request,
            'empanadas/formulaireModificationEmpanada.html',
            { 
                'empanada' : emp,
                'user' : user
            },
        )
    elif request.user.is_authenticated :
        return redirect('/empanadas')
    else :
        return redirect('/login')

def modifierEmpanada(request, empanada_id) :
    user = None
    if request.user.is_staff :
        user = User.objects.get(id=request.user.id)
        emp = Empanada.objects.get(idEmpanada = empanada_id)
        form = EmpanadaForm(request.POST, instance=emp)
        if form.is_valid() :
            emp.image = request.FILES['image']
            emp.save()
            return redirect('/empanada/%d' % empanada_id)
        else :
            return render(
                request,
                'empanadas/formulaireNonValide.html',
                { 
                    'erreurs' : form.errors,
                    'user' : user
                },
            )
    elif request.user.is_authenticated :
        return redirect('/empanadas')
    else :
        return redirect('/login')

def ingredients(request) :
    user = None
    if request.user.is_staff :
        lesIngredients = Ingredient.objects.all()
        user = User.objects.get(id=request.user.id)
        return render(
            request,
            'empanadas/ingredients.html',
            { 
                'ingredients' : lesIngredients,
                'user' : user
            },
        )
    elif request.user.is_authenticated :
        return redirect('/empanadas')
    else :
        return redirect('/login')


def formulaireCreationIngredient(request) :
    user = None
    if request.user.is_staff :
        user = User.objects.get(id=request.user.id)
        return render(
            request,
            'empanadas/formulaireCreationIngredient.html',
            { 'user' : user },
        )
    elif request.user.is_authenticated :
        return redirect('/empanadas')
    else :
        return redirect('/login')

def creerIngredient(request) :
    user = None
    if request.user.is_staff :
        user = User.objects.get(id=request.user.id)
        form = IngredientForm(request.POST)
        if form.is_valid() :
            nomIngr = form.cleaned_data['nomIngredient']
            ingr = Ingredient()
            ingr.nomIngredient = nomIngr
            ingr.save()
            return render(
                request,
                'empanadas/traitementFormulaireCreationIngredient.html',
                { 
                    'nom' : nomIngr,
                    'user' : user
                },
            )
        else :
            return render(
                request,
                'empanadas/formulaireNonValide.html',
                { 
                    'erreurs' : form.errors,
                    'user' : user
                },
            )
    elif request.user.is_authenticated :
        return redirect('/empanadas')
    else :
        return redirect('/login')

def formulaireCreationEmpanada(request) :
    user = None
    if request.user.is_staff :    
        user = User.objects.get(id=request.user.id)
        return render(
            request,
            'empanadas/formulaireCreationEmpanada.html',
            { 'user' : user },
        )
    elif request.user.is_authenticated :
        return redirect('/empanadas')
    else :
        return redirect('/login')


def creerEmpanada(request) :
    user = None
    if request.user.is_staff :
        user = User.objects.get(id=request.user.id)
        form = EmpanadaForm(request.POST)
        if form.is_valid() :
            nomEmp = form.cleaned_data['nomEmpanada']
            prixEmp = form.cleaned_data['prix']
            emp = Empanada()
            emp.nomEmpanada = nomEmp
            emp.prix = prixEmp
            emp.image = request.FILES['image']
            emp.save()
            return empanada(request, emp.idEmpanada)
        else :
            return render(
                request,
                'empanadas/formulaireNonValide.html',
                { 
                    'erreurs' : form.errors,
                    'user' : user
                },
            )
    elif request.user.is_authenticated :
        return redirect('/empanadas')
    else :
        return redirect('/login')

def ajouterIngredientEmpanada(request, empanada_id) :
    form = CompositionForm(request.POST)
    if form.is_valid() :
        ingr = form.cleaned_data['ingredient']
        qt = form.cleaned_data['quantite']
        emp = Empanada.objects.get(idEmpanada=empanada_id)
        recherche = Composition.objects.filter(empanada=empanada_id, ingredient=ingr.idIngredient)
        
        if recherche.count() > 0 :
            ligne = recherche.first()
        else :
            ligne = Composition()
            ligne.ingredient = ingr
            ligne.empanada = emp
        
        ligne.quantite = qt
        ligne.save()
        return redirect('/empanada/%d' % empanada_id)
    
    else :
        return render(
            request,
            'empanada/formulaireNonValide.html',
            { 'erreurs' : form.errors},
        )

def afficherFormulaireModificationIngredient(request, ingredient_id) :
    user = None
    if request.user.is_staff :
        user = User.objects.get(id=request.user.id)
        ingr = Ingredient.objects.get(idIngredient = ingredient_id)
        return render(
            request,
            'empanadas/formulaireModificationIngredient.html',
            { 'ingredient' : ingr, 'user' : user }
        )
    elif request.user.is_authenticated :
        return redirect('/empanadas')
    else :
        return redirect('/login')

def modifierIngredient(request, ingredient_id) :
    user = None
    if request.user.is_staff :
        user = User.objects.get(id=request.user.id)
        ingr = Ingredient.objects.get(idIngredient = ingredient_id)
        form = IngredientForm(request.POST, instance=ingr)
        if form.is_valid() :
            form.save()
            return redirect('/ingredients')
        else :
            return render(
                request,
                'empanadas/formulaireNonValide.html',
                { 'erreurs' : form.errors, 'user' : user },
            )
    elif request.user.is_authenticated :
        return redirect('/empanadas')
    else :
        return redirect('/login')

def supprimerIngredient(request, ingredient_id) :
    ingr = Ingredient.objects.get(idIngredient = ingredient_id)
    ingr.delete()
    return redirect('/ingredients')


def supprimerIngredientEmpanada(request, empanada_id, ingredient_id) :
    compo = Composition.objects.get(empanada = empanada_id, ingredient = ingredient_id)
    compo.delete()
    return redirect('/empanada/%d' % empanada_id)
    