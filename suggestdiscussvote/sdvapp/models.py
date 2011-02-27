from django.db import models
from django.utils.translation import ugettext as _
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

class Suggestion(models.Model):
    UNDECIDED = 'undecided'
    REJECTED = 'rejected'
    PLANNED = 'planned'
    COMPLETED = 'completed'

    STATUS_CHOICES = (
        (UNDECIDED, _(u'Undecided')),
        (REJECTED, _(u'Rejected')),
        (PLANNED, _(u'Planned')),
        (COMPLETED, _(u'Completed')))

    status = models.CharField(max_length=32, choices=STATUS_CHOICES, default=UNDECIDED)

    title = models.CharField(max_length=255)
    description = models.TextField()

    created = models.DateTimeField(auto_now_add=True)
    changed = models.DateTimeField(auto_now=True)

    suggested_by = models.ForeignKey(User)
    supported_by = models.ManyToManyField(User, related_name='supports')

    class Meta:
        permissions = (
            ('change_suggestion_status', _(u'Can change the status of suggestions')),
        )

    def __str__(self):
        return self.title

class Comment(models.Model):
    suggestion = models.ForeignKey(Suggestion, related_name='comments')
    comment_by = models.ForeignKey(User)

    comment = models.TextField()

    created = models.DateTimeField(auto_now_add=True)

from django.contrib.admin import ModelAdmin, site

class SuggestionAdmin(ModelAdmin):
    search_fields = ('title',)

site.register(Suggestion, SuggestionAdmin)
site.register(Comment)