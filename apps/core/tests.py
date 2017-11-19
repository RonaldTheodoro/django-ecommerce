from django.test import TestCase
from django.urls import reverse

from . import forms


class IndexViewTest(TestCase):

    def setUp(self):
        self.response = self.client.get(reverse('core:index'))

    def test_get(self):
        """GET / must return status code 200"""
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        """GET / must use core/index.html template"""
        self.assertTemplateUsed(self.response, 'core/index.html')


class AboutViewTest(TestCase):

    def setUp(self):
        self.response = self.client.get(reverse('core:about'))

    def test_get(self):
        """GET /about must return status code 200"""
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        """GET /about must use core/about.html template"""
        self.assertTemplateUsed(self.response, 'core/about.html')


class ContactViewTest(TestCase):

    def setUp(self):
        self.response = self.client.get(reverse('core:contact'))

    def test_get(self):
        """GET /contact must return status code 200"""
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        """GET /contact must use core/contact.html template"""
        self.assertTemplateUsed(self.response, 'core/contact.html')

    def test_form_context(self):
        """/contact must have ContactForm in context"""
        self.assertIsInstance(self.response.context['form'], forms.ContactForm)
