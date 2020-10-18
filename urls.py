from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from wagtail.admin import urls as wagtailadmin_urls
from wagtail.core import urls as wagtail_urls
from grapple import urls as grapple_urls
from wagtail.core import views
views.serve.csrf_exempt = True

urlpatterns = [
    url(r'^admin', admin.site.urls),
    url(r'^wagtail/', include(wagtailadmin_urls)),
    url(r"", include(grapple_urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)