from django.conf.urls import patterns, include, url
from browser.views import BrowserView

urlpatterns = patterns('',
    url(r'^$', BrowserView.as_view())
)
