from django.urls import path
from comptes import views
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('login', LoginView.as_view(template_name="comptes/login.html"), name="login"),
]
