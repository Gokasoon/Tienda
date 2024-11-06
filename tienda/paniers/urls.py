from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from paniers import views

urlpatterns = [
    path('cart/', views.afficherPanier),
    path('cart/<int:empanada_id>/buy/', views.ajouterEmpanadaAuPanier),
    path('cart/<int:empanada_id>/delete/', views.retirerDuPanier),
    path('cart/delete/', views.viderPanier),
    path('cart/<int:empanada_id>/decrease/', views.retirerUneEmpanadaDuPanier),
    path('cart/pay/', views.payerPanier),
    path('orders/', views.afficherCommandes),
    path('order/<int:order_id>/', views.afficherCommande),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)