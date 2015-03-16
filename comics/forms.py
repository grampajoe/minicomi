from django.contrib.auth.forms import UserCreationForm


class SetupForm(UserCreationForm):
    """Form that creates superusers."""
    def save(self, commit=True, *args, **kwargs):
        """Saves the user as a superuser."""
        user = super().save(commit=False, *args, **kwargs)
        user.is_superuser = True
        user.is_staff = True

        if commit:
            user.save()

        return user
