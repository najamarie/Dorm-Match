# accounts/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from dormmatch.models import UserProfile
from django.contrib.auth import get_user_model

User = get_user_model()

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'username', 'first_name', 'last_name', 'birthday', 'gender',
            'contact_number', 'email', 'school', 'degree_program', 'password1', 'password2'
        ]

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = (
            'username', 'first_name', 'last_name', 'suffix', 'birthday', 'gender',
            'contact_number', 'email', 'school', 'degree_program'
        )


