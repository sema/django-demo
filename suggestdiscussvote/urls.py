from django.conf.urls.defaults import *
from django.conf import settings
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^accounts/login/$',
        'django.contrib.auth.views.login',
        name='login'),

    url(r'^accounts/logout/$',
        'django.contrib.auth.views.logout_then_login',
        name='logout'),

    (r'^', include('suggestdiscussvote.sdvapp.urls')),

    (r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    )