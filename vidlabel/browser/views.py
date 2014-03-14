from django.views.generic import TemplateView

class BrowserView(TemplateView):
	template_name = 'browser.html'
