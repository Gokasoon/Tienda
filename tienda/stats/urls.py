from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from paniers import views

urlpatterns = [
    
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)