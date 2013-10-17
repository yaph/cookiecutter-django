from django.conf import settings
from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView


urlpatterns = patterns('',
    url(r'^$',
        view=TemplateView.as_view(template_name='index.html'),
        name='index'),
)


# Debug static media
if settings.DEBUG:
    urlpatterns = patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
        (r'', include('django.contrib.staticfiles.urls')),
    ) + urlpatterns
