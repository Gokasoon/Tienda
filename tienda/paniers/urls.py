from django.urls import path
from paniers import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('cart/', views.afficherPanier),

]