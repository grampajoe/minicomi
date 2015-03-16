from django.conf.urls import patterns, url
from django.views.generic.base import TemplateView, View

from comics.views import SetupView


urlpatterns = patterns(
    '',
    url(r'^$', TemplateView.as_view(template_name='home.html'), name='home'),
    url(r'^setup/$', SetupView.as_view(), name='setup'),
)
