from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from videoApp.views import *
from dajaxice.core import dajaxice_autodiscover, dajaxice_config
from videoApp.api import TimeTagResource
from tastypie.api import Api
dajaxice_autodiscover()
# admin.autodiscover()

v1_api = Api(api_name='v1')

v1_api.register(TimeTagResource())

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'videoApp.views.home', name='home'),
    # url(r'^videoApp/', include('videoApp.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'video/add/$', VideoCreate.as_view(), name='video_add'),
    url(r'video/(?P<pk>\d+)/$', VideoUpdate.as_view(), name='video_update'),
    url(r'video/(?P<pk>\d+)/delete/$', VideoDelete.as_view(), name='video_delete'),
    url(r'video/detail/(?P<pk>\d+)/$', VideoDetail.as_view(), name='video_detail'),
    url(r'^api/', include(v1_api.urls)),
    url(dajaxice_config.dajaxice_url, include('dajaxice.urls')),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
