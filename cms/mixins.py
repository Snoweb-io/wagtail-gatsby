from django.conf import settings
from django.shortcuts import redirect
from wagtail.contrib.settings.models import BaseSetting
from .tasks import develop, build


class HeadlessPageMixin(object):

    def get_client_root_url(self):
        try:
            return settings.HEADLESS_PREVIEW_CLIENT_URLS[self.get_site().hostname]
        except (AttributeError, KeyError):
            return settings.HEADLESS_PREVIEW_CLIENT_URLS["default"]

    def get_preview_url(self):
        return "%s%s?preview=1" % (
            self.get_client_root_url(),
            self.get_url()
        )

    def serve_preview(self, request, mode_name):
        if settings.DEBUG:
            develop.delay()
        return redirect(self.get_preview_url())

    def get_url(self):
        site = self.get_site()
        url_folder = "%s" % (
            self.url_path.replace('/' + site.root_page.slug, '')[:-1]
        )
        if not url_folder:
            return '/'
        return url_folder

    url = property(get_url)


class HeadlessSettingMixin(BaseSetting):
    class Meta:
        abstract = True

    def save(self, with_build=True, *args, **kwargs):
        super().save(*args, **kwargs)
        if with_build:
            build.delay(site_id=self.site.id)
