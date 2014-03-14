from django.views.generic import TemplateView
from django.conf import settings

import os



class BrowserView(TemplateView):
    template_name = 'browser.html'

    def get_context_data(self, **kwargs):
        dirs = os.listdir(os.path.join(settings.STATICFILES_DIRS[0], "data"))
        files  = []
        for di in dirs:
            files.append(len(os.listdir(os.path.join(settings.STATICFILES_DIRS[0], "data", di))))

        return {'directories':dirs, 'nfiles': files}


