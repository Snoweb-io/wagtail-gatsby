from time import time
from django.http import JsonResponse
from wagtail.admin.views.pages import preview


class PreviewOnEdit(preview.PreviewOnEdit):

    def post(self, request, *args, **kwargs):
        request.session[self.session_key] = request.POST.urlencode(), time()
        self.remove_old_preview_data()
        page = self.get_page()
        form = self.get_form(page, request.POST)
        form.save()
        return JsonResponse({'is_valid': form.is_valid()})
