from .models import Comment
from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class CommentForm(ModelForm):
    message = forms.CharField(widget=forms.Textarea(attrs={"rows":3}))
    class Meta:
        model = Comment
        fields = ['message']


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']