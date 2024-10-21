from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from comptes.models import TiendaUser, TiendaUserForm


def connexion(request) :
    if not request.user.is_authenticated :
        usr = request.POST['username']
        pwd = request.POST['password']
        user = authenticate(request, username=usr, password=pwd)
        if user is None :
            return redirect ('/login')
        else :
            login(request, user)
            return redirect('/empanadas')
    else :
        return redirect('/empanadas')

def deconnexion(request) :
    logout(request)
    return render(request, 'comptes/logout.html')

def formulaireProfil(request) :
    user = None 
    if request.user.is_authenticated :
        return render(
            request,
            'comptes/profil.html',
            {
                'user' : TiendaUser.objects.get(id=request.user.id),
            }
        )
    else :
        return redirect('/login')

def traitementFormulaireProfil(request) :
    user = None
    if request.user.is_authenticated :
        user = TiendaUser.objects.get(id=request.user.id)
        form = TiendaUserForm(request.POST, request.FILES, instance=user)
        if form.is_valid() :
            form.save()
            return redirect('/empanadas')
    else :
        return redirect('/login')


def formulaireInscription(request) :
    user = None 
    if not request.user.is_authenticated :
        return render(
            request,
            'comptes/formulaireInscription.html'
        )
    else :
        return render(
            request,
            'comptes/profil.html',
            {
                'user' : TiendaUser.objects.get(id=request.user.id),
            }
        )

def traitementFormulaireInscription(request): 
    user = TiendaUser() 
    user.first_name = request.POST['first_name']
    user.last_name = request.POST['last_name']
    user.username = request.POST['username']
    user.email = request.POST['email']
    user.set_password(request.POST['password'])
    img = request.FILES.get('image')
    if img :
        user.image = img
    else:
        user.image = "imagesUsers/default.png"
    user.save() 
    login(request, user) 
    return redirect( '/empanadas' ) 
