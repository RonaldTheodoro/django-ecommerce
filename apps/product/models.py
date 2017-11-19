from django.db import models


class Product(models.Model):
    title = models.CharField('title', max_length=120)
    descripition = models.TextField('descripition')
    price = models.DecimalField(
        'price',
        decimal_places=2,
        max_digits=20,
        default=39.99
    )

    def __str__(self):
        return self.title
