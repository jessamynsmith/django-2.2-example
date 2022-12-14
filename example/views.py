import json

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView

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


class UserProfileJsonView(LoginRequiredMixin, DetailView):
    model = models.UserProfile
    template_name = 'example/user_profile_json.html'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        serializer_class = UserProfileSerializer(instance=self.object)
        json_data = serializer_class.data
        formatted_data = json.dumps(json_data, indent=4)
        context_data['json_data'] = formatted_data
        return context_data
