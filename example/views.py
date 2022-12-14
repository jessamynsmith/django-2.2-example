from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView

from rest_framework import serializers, viewsets

from example import models
from example.forms import ExtendedUserProfileForm


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.UserProfile
        fields = ['birthday', 'nickname']


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = models.UserProfile.objects.all()
    serializer_class = UserProfileSerializer


class UserEditView(LoginRequiredMixin, CreateView):
    form_class = ExtendedUserProfileForm
    template_name = 'example/user_profile_edit.html'
    success_url = reverse_lazy('user_edit')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs
