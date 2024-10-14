from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User

class TiendaUser(User) :
    image = models.ImageField( default = "imagesUsers/default.png",
                               upload_to = "imagesUsers/")


class TiendaUserForm(ModelForm) :
    class Meta :
        model = TiendaUser
        fields = [ 'username', 'first_name', 'last_name', 'email', 'image']