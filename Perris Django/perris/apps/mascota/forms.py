from django import forms
from apps.mascota.models import Mascota
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
#traeremos el modelo de User
from django.contrib.auth.models import User


class MascotaForms(forms.ModelForm):
    class Meta:
        model= Mascota

        fields =[
            'nombre',
            'sexo',
            'foto',
            'Descripcion',
            'fecha_rescate',
            'estado',
        ]


class CustomCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=True, label="Nombre")
    last_name = forms.CharField(required=True, label="Apellido")

    class Meta:
        #le decimos el modelo de BBDD al que esta asociado este
        #formulario
        model = User
        #le decimos a django en que orden aparecerán los campos
        #en el template
        fields = ('username',
        'first_name',
         'last_name',
         'email',
         'password1',
         'password2')