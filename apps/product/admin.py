from django.contrib import admin

from . import models


class ProductAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'slug']

    class Meta:
        model = models.Product


admin.site.register(models.Product, ProductAdmin)
