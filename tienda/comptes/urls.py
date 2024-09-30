from django.urls import path
from comptes import views
from django.contrib.auth import auth_views

urlpatterns = [
    path('login', auth_views.LoginView.as_view(template_name="comptes/login.html"), name="login"),
]
