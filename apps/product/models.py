import os

from django.db import models


def get_filename_ext(filepath):
    basename = os.path.basename(filepath)
    return os.path.splitext(basename)


def upload_image_path(instance, filename):
    name, ext = get_filename_ext(filename)
    new_filename = hash(name)
    return f'products/{instance.pk}/{new_filename}{ext}'


class ProductManager(models.Manager):

    def featured(self, id):
        return self.get_queryset().filter(featured=True)


class Product(models.Model):
    title = models.CharField('title', max_length=120)
    slug = models.SlugField('slug', blank=True, unique=True)
    descripition = models.TextField('descripition')
    price = models.DecimalField(
        'price',
        decimal_places=2,
        max_digits=20,
        default=39.99
    )
    image = models.ImageField(
        'image',
        upload_to=upload_image_path,
        null=True,
        blank=True
    )
    featured = models.BooleanField('featured', default=False)

    objects = ProductManager()

    def __str__(self):
        return self.title
