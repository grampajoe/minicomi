from django.contrib.auth import get_user_model
from django.test import TestCase


class HomeTests(TestCase):
    """Tests for the home page."""
    def test_home_title(self):
        """The title should have "Minicomi" in it."""
        response = self.client.get('/')

        self.assertIn('<title>Minicomi', str(response.content))


class SetupTests(TestCase):
    """Tests for the setup view."""
    def test_ok(self):
        """The setup page should render."""
        response = self.client.get('/setup/')

        self.assertEqual(response.status_code, 200)

    def test_creates_superuser(self):
        """Should create a superuser on submit."""
        response = self.client.post('/setup/', {
            'username': 'hello',
            'password1': 'friend',
            'password2': 'friend',
        })

        user = get_user_model().objects.get(username='hello')

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

    def test_logs_you_in(self):
        """Should log in the newly created user."""
        response = self.client.post('/setup/', {
            'username': 'hello',
            'password1': 'friend',
            'password2': 'friend',
        }, follow=True)

        self.assertTrue(response.context['user'].is_authenticated())

    def test_redirects_to_admin(self):
        """Should redirect to the admin page."""
        response = self.client.post('/setup/', {
            'username': 'hello',
            'password1': 'friend',
            'password2': 'friend',
        })

        self.assertRedirects(response, '/admin/')

    def test_404_if_admin_exists(self):
        """The setup page should 404 if an admin exists."""
        get_user_model().objects.create(
            username='me',
            is_superuser=True,
        )

        self.assertEqual(self.client.get('/setup/').status_code, 404)
        self.assertEqual(self.client.post('/setup/').status_code, 404)
        self.assertEqual(self.client.put('/setup/').status_code, 404)
        self.assertEqual(self.client.delete('/setup/').status_code, 404)
