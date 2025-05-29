from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import UserStat


class CityForm(forms.ModelForm):
    """
    Форма для выбора города
    """
    def __init__(self, current_city, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['city'].initial = current_city

    city = forms.CharField(label='Введите город:', empty_value='', required=False)

    class Meta:
        model = UserStat
        fields = ['city']


class SignUpForm(UserCreationForm):
    """
    Форма для регистрации пользователей
    """
    username = forms.CharField(label='Ник пользователя:')
    first_name = forms.CharField(label='Имя пользователя (не обязательно):', required=False)
    password1 = forms.CharField(label='Введите пароль:', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Повторите пароль:', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'password1', 'password2',)


