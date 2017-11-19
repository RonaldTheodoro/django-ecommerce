import tempfile

from django.test import TestCase
from django.urls import reverse

from . import models


class ProductListViewTest(TestCase):

    def setUp(self):
        self.response = self.client.get(reverse('product:list'))

    def test_get(self):
        """GET /product/list must return status code 200"""
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        """GET /product/list must use product/list.html template"""
        self.assertTemplateUsed(self.response, 'product/list.html')


class ProductDetailViewTest(TestCase):

    def setUp(self):
        models.Product.objects.create(
            title='hat',
            descripition='this is an awesome hat',
            price=59.99,
            image=tempfile.NamedTemporaryFile(suffix=".jpg").name
        )
        self.response = self.client.get(
            reverse('product:detail', kwargs={'pk': 1})
        )

    def test_get(self):
        """GET /product/list must return status code 200"""
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        """GET /product/list must use product/list.html template"""
        self.assertTemplateUsed(self.response, 'product/detail.html')


class ProductFailDetailViewTest(TestCase):

    def setUp(self):
        self.response = self.client.get(
            reverse('product:detail', kwargs={'pk': 99})
        )

    def test_get(self):
        """GET /product/list must return status code 200"""
        self.assertEqual(404, self.response.status_code)
