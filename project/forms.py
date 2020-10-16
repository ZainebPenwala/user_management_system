from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Employee
from django.contrib.auth.forms import AuthenticationForm, UsernameField


class EmployeeForm(forms.ModelForm):

    class Meta:
        model = Employee
        exclude = ('user_id', )


class CustomAuthenticationForm(AuthenticationForm):
    username = UsernameField(
        label='Email Id',
        widget=forms.TextInput(attrs={'autofocus': True})
    )


class RegistrationForm(UserCreationForm):
    username = forms.CharField(
        label=('Email Id'),
        max_length=100,
        help_text=('Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        error_messages={'unique': ("A user with that email id already exists.")},
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', )
