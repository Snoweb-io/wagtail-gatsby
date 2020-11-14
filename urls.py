from django.conf.urls import include, url
from django.contrib import admin
from grapple import urls as grapple_urls
from wagtail.core import views
from cms import urls as cms_urls

views.serve.csrf_exempt = True

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^wagtail/', include(cms_urls)),
    url(r"", include(grapple_urls)),
]
