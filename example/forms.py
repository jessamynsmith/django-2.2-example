from django import forms

from example import models as example_models


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = example_models.UserProfile
        fields = ['birthday']


class ExtendedUserProfileForm(UserProfileForm):
    class Meta(UserProfileForm.Meta):
        fields = ['nickname']
        fields.extend(UserProfileForm.Meta.fields)

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        obj = super().save(commit=False)
        obj.user = self.user
        if commit:
            obj.save()
        return obj
