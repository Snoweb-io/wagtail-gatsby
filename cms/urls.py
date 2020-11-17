from django.urls import path
from wagtail.admin import urls as wagtail_urls

from . import views

# TODO: find a better way for overwriting wagtail views (bug if django reverse is used)

urlpatterns = [
    path('pages/<int:page_id>/edit/preview/', views.PreviewOnEdit.as_view(), name='custom_preview_on_edit'),
] + wagtail_urls.urlpatterns
