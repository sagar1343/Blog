from typing import Any
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update(
                {"class": "h-10 px-4 border-2 border-zinc-300 shadow-sm rounded-md focus-visible:outline-sky-300"})


class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=150,
        widget=forms.TextInput(attrs={
                               "class": "h-10 px-4 border-2 border-zinc-300 shadow-sm rounded-md focus-visible:outline-sky-300"}))
    password = forms.CharField(max_length=150, widget=forms.PasswordInput(attrs={
        "class": "h-10 px-4 border-2 border-zinc-300 shadow-sm rounded-md focus-visible:outline-sky-300"})
    )
