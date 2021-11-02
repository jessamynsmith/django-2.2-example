from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView

from example.forms import ExtendedUserProfileForm


class UserEditView(LoginRequiredMixin, CreateView):
    form_class = ExtendedUserProfileForm
    template_name = 'example/user_profile_edit.html'
    success_url = reverse_lazy('user_edit')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs
