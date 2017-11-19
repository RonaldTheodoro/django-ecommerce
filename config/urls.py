from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('apps.core.urls', namespace='core')),
    url(r'^product/', include('apps.product.urls', namespace='product')),
    url(r'^account/', include('apps.account.urls', namespace='account')),
]
