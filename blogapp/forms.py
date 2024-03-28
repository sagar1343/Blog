from typing import Any
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Author, BlogPost
from django_ckeditor_5.widgets import CKEditor5Widget


class RegistrationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs.update({
            'class': 'form-control input input-bordered w-full max-w-xs my-2',
            'placeholder': 'Password'
        })
        self.fields['password2'].widget.attrs.update({
            'class': 'form-control input input-bordered w-full max-w-xs my-2',
            'placeholder': 'Confirm Password'
        })

    class Meta:
        model = Author
        fields = ['first_name', 'last_name',
                  'username', 'password1', 'password2', 'profile_image']
        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'form-control input input-bordered w-full max-w-xs my-2', 'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control input input-bordered w-full max-w-xs my-2', 'placeholder': 'Last Name'}),
            'username': forms.TextInput(attrs={
                'class': 'form-control input input-bordered w-full max-w-xs my-2', 'placeholder': 'Username'}),
            'profile_image': forms.FileInput(attrs={"class": "file-input w-full max-w-xs"})
        }


class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=150,
        widget=forms.TextInput(
            attrs={'class': 'form-control input input-bordered w-full max-w-xs my-2', 'placeholder': 'Username'})
    )
    password = forms.CharField(
        max_length=150,
        widget=forms.PasswordInput(
            attrs={'class': 'form-control input input-bordered w-full max-w-xs my-2', 'placeholder': 'Password'})
    )


class CreateBlogForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'description', 'content', 'category']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control input input-bordered w-full max-w-xs my-2', 'placeholder': 'Title'}),
            'description': forms.TextInput(attrs={'class': 'form-control input input-bordered w-full max-w-xs my-2', 'placeholder': 'Description'}),
            'category': forms.Select(attrs={'class': 'form-control select select-bordered w-full max-w-xs my-2'}),
            'content':   CKEditor5Widget(config_name='list', attrs={'class': 'form-control input input-bordered  my-2', 'placeholder': 'Content'})
        }
