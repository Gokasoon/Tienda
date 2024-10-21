from django.urls import path
from comptes import views
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('login', LoginView.as_view(template_name="comptes/login.html"), name="login"),
    path('logout', views.deconnexion, name="logout"),
    path('connexion', views.connexion),
    path('user/update/', views.formulaireProfil),
    path('user/updated/', views.traitementFormulaireProfil),
    path('register/', views.formulaireInscription), 
    path('inscription/', views.traitementFormulaireInscription),    
]
