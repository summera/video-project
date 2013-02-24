from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from videoApp.views import *
# admin.autodiscover()

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
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
