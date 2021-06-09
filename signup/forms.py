from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class CreateUserForm(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput(
        attrs={"name": "password1", 'placeholder': 'Mot de passe'}))

    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={"name": "password2", 'placeholder': 'Confirmer mot de passe'}))

    class Meta:
        model = User

        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={"name": "username", "placeholder": "Nom d'utilisateur"}),
            'first_name': forms.TextInput(attrs={"name": "first_name", "placeholder": "Prénom"}),
            'last_name': forms.TextInput(attrs={"name": "last_name", "placeholder": "Nom"}),
            'email': forms.TextInput(attrs={"name": "email", "placeholder": "Email"}),
        }



