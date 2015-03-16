from django.contrib.auth import get_user_model, authenticate, login
from django.http import HttpResponse, HttpResponseNotFound
from django.views.generic.edit import FormView

from comics.forms import SetupForm


class SetupView(FormView):
    """View for creating superusers.

    If a superuser exists, a 404 is returned.
    """
    template_name = 'setup.html'
    form_class = SetupForm
    success_url = '/admin/'

    def dispatch(self, *args, **kwargs):
        if get_user_model().objects.filter(is_superuser=True).count():
            return HttpResponseNotFound()

        return super().dispatch(*args, **kwargs)

    def form_valid(self, form):
        form.save()
        user = authenticate(
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password1'],
        )
        login(self.request, user)

        return super().form_valid(form)
