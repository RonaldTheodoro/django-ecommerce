from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from . import forms


User = get_user_model()


class LoginViewTest(TestCase):

    def setUp(self):
        self.response = self.client.get(reverse('account:sign_in'))

    def test_get(self):
        """GET /account/login must return status code 200"""
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        """GET /account/login must use account/login.html template"""
        self.assertTemplateUsed(self.response, 'account/login.html')

    def test_form_context(self):
        """/account/login must have LoginForm in context"""
        self.assertIsInstance(self.response.context['form'], forms.LoginForm)


class LoginViewAuthTest(TestCase):

    def setUp(self):
        User.objects.create_user(
            'ronaldtheodoro',
            'ronald@theodoro.com',
            'asdf1234'
        )
        data = {'username': 'ronaldtheodoro', 'password': 'asdf1234'}
        self.response = self.client.post(reverse('account:sign_in'), data)

    def test_login_redirect(self):
        """After login user must be redirect to /"""
        self.assertRedirects(self.response, reverse('core:index'))

    def test_is_authenticated(self):
        """User must be authenticated"""
        response = self.client.get(reverse('core:index'))
        user = response.context.get('user')
        self.assertTrue(user.is_authenticated)


class RegisterViewTest(TestCase):

    def setUp(self):
        self.response = self.client.get(reverse('account:register'))

    def test_get(self):
        """GET /account/register must return status code 200"""
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        """GET /account/register must use account/register.html template"""
        self.assertTemplateUsed(self.response, 'account/register.html')

    def test_form_context(self):
        """/account/register must have RegisterForm in context"""
        self.assertIsInstance(
            self.response.context['form'],
            forms.RegisterForm
        )
