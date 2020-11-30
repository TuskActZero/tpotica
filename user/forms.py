from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Profesional, Ventas, Secretaria, Gerencia, Taller, User


class SecretariaSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User 
        fields = ["username", "password1", "sector"]

class ProfesionalSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User 
        fields = ["username", "password1", "sector"]

class VentasSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User 
        fields = ["username", "password1", "sector"]

class GerenciaSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User 
        fields = ["username", "password1", "sector"]

class TallerSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User 
        fields = ["username", "password1", "sector"]

