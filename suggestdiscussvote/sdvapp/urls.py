from django.conf.urls.defaults import *
from django.views.generic import create_update, list_detail

from models import Suggestion
from forms import SuggestionForm

urlpatterns = patterns('suggestdiscussvote.sdvapp.views',
    url('^$',
        list_detail.object_list,
        kwargs={'queryset' : Suggestion.objects.all()},
        name='suggestion_list'),

    url('^(?P<suggestion_pk>[0-9]+)/update/$',
        'update_suggestion',
        name='suggestion_update'),

     url('^suggestion/(?P<suggestion_pk>[0-9]+)/$',
        'show_suggestion',
        name='suggestion_detail'),

     url('^(?P<suggestion_pk>[0-9]+)/support/$',
        'support',
        name='suggestion_support'),

     url('^(?P<suggestion_pk>[0-9]+)/unsupport/$',
        'unsupport',
        name='suggestion_unsupport'),

    url('^create/',
        'create_suggestion',
        name='suggestion_create'),
)
