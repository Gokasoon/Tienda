from django.urls import path
from paniers import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('cart/', views.afficherPanier),
    path('cart/<int:empanada_id>/buy/', views.ajouterEmpanadaAuPanier),
    path('cart/<int:empanada_id>/delete/', views.retirerDuPanier),
    path('cart/delete/', views.viderPanier),
]
