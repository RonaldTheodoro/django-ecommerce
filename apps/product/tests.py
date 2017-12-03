import tempfile
from unittest import skip

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
            slug='hat',
            descripition='this is an awesome hat',
            price=59.99,
            image=tempfile.NamedTemporaryFile(suffix=".jpg").name
        )
        self.response = self.client.get(
            reverse('product:detail', kwargs={'slug': 'hat'})
        )

    def test_get(self):
        """GET /product/1 must return status code 200"""
        self.assertEqual(200, self.response.status_code)

    @skip
    def test_template(self):
        """GET /product/1 must use product/detail.html template"""
        self.assertTemplateUsed(self.response, 'product/detail.html')


class ProductFailDetailViewTest(TestCase):

    def setUp(self):
        self.response = self.client.get(
            reverse('product:detail', kwargs={'slug': 'asdf'})
        )

    def test_get(self):
        """GET /product/list must return status code 200"""
        self.assertEqual(404, self.response.status_code)


class ProductFeaturedListViewTest(TestCase):

    def setUp(self):
        self.response = self.client.get(reverse('product:featured_list'))

    def test_get(self):
        """GET /product/featured/list must return status code 200"""
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        """GET /product/featured/list must use product/list.html template"""
        self.assertTemplateUsed(self.response, 'product/list.html')


class ProductFeaturedDetailViewTest(TestCase):

    def setUp(self):
        models.Product.objects.create(
            title='hat',
            slug='hat',
            descripition='this is an awesome hat',
            price=59.99,
            image=tempfile.NamedTemporaryFile(suffix=".jpg").name,
            featured=True
        )
        self.response = self.client.get(
            reverse('product:featured_detail', kwargs={'slug': 'hat'})
        )

    @skip
    def test_get(self):
        """GET /product/featured/1 must return status code 200"""
        self.assertEqual(200, self.response.status_code)

    @skip
    def test_template(self):
        """GET /product/featured/1 must use product/detail.html template"""
        self.assertTemplateUsed(self.response, 'product/detail.html')
