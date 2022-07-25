from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User


class RegisterUserForm(UserCreationForm):

    first_name = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': "Ваше имя", 'id': 'input_name_reg'}))
    last_name = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': "Ваша фамилия"}))

    username = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': "Имя пользователя"}))
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={'placeholder': "Ваш E-mail"}))

    password1 = forms.CharField(widget=forms.PasswordInput(
        attrs={'placeholder': 'Пароль'}))
    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={'placeholder': 'Повторите пароль', 'id': 'input_password_reg_2'}))

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')

    def clean_username(self):
        username = self.cleaned_data['username']
        if username.lower() == 'хуйло':
            raise ValidationError('Заявки от ХУЙЛУШИ не рассматриваем!!')

        return username


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': "Имя пользователя", 'id': 'input_email'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'placeholder': 'Пароль', 'id': 'input_password'}))

    def clean_username(self):
        username = self.cleaned_data['username']
        if username.lower() == 'хуйло':
            raise ValidationError('Заявки от ХУЙЛУШИ не рассматриваем!!')

        return username
