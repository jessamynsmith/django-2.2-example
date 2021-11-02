from django import forms
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username']


class ExtendedUserForm(UserForm):
    class Meta(UserForm.Meta):
        fields = ['first_name']
        fields.extend(UserForm.Meta.fields)
