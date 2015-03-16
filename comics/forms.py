from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import EmailField


class SetupForm(UserCreationForm):
    """Form that creates superusers."""
    email = EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email")

    def save(self, commit=True, *args, **kwargs):
        """Saves the user as a superuser."""
        user = super().save(commit=False, *args, **kwargs)
        user.is_superuser = True
        user.is_staff = True

        if commit:
            user.save()

        return user
