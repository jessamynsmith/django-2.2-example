from django.views.generic import FormView

from example.forms import ExtendedUserForm


class UserEditView(FormView):
    form_class = ExtendedUserForm
    template_name = 'example/user_edit.html'
