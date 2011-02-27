from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied

from models import Suggestion, Comment
from forms import ExtendedSuggestionForm, SuggestionForm, CommentForm

def show_suggestion(request, suggestion_pk):

    suggestion = get_object_or_404(Suggestion, pk=suggestion_pk)
    comments = suggestion.comments.all()

    if request.method == 'POST' and request.user.is_authenticated():
        comment_form = CommentForm(request.POST)

        if comment_form.is_valid():
            instance = comment_form.save(commit=False)
            instance.comment_by = request.user
            instance.suggestion = suggestion
            instance.save()

            return HttpResponseRedirect(reverse('suggestion_detail',
                                                kwargs={'suggestion_pk' : suggestion.pk}))

    else:
        comment_form = CommentForm()

    return render_to_response('sdvapp/suggestion_detail.html',
                              {'suggestion' : suggestion,
                               'comments' : comments,
                               'comment_form' : comment_form,},
                              context_instance=RequestContext(request))

@login_required
def support(request, suggestion_pk):

    suggestion = get_object_or_404(Suggestion, pk=suggestion_pk)

    if request.method == 'POST':
        suggestion.supported_by.add(request.user)

        return HttpResponseRedirect(reverse('suggestion_detail',
                                            kwargs={'suggestion_pk' : suggestion.pk}))

    else:
        return HttpResponseForbidden()

@login_required
def unsupport(request, suggestion_pk):

    suggestion = get_object_or_404(Suggestion, pk=suggestion_pk)

    if request.method == 'POST':
        suggestion.supported_by.remove(request.user)

        return HttpResponseRedirect(reverse('suggestion_detail',
                                            kwargs={'suggestion_pk' : suggestion.pk}))

    else:
        return HttpResponseForbidden()

@login_required
def update_suggestion(request, suggestion_pk):

    suggestion = get_object_or_404(Suggestion, pk=suggestion_pk)

    if not request.user.has_perm('sdvapp.change_suggestion', obj=suggestion):
        raise PermissionDenied

    if request.user.has_perm('sdvapp.change_suggestion_status', obj=suggestion):
        form_class = ExtendedSuggestionForm
    else:
        form_class = SuggestionForm

    if request.method == 'POST':
        form = form_class(request.POST, instance=suggestion)

        if form.is_valid():
            form.save()

            return HttpResponseRedirect(reverse('suggestion_detail',
                                                kwargs={'suggestion_pk' : suggestion.pk}))

    else:
        form = form_class(instance=suggestion)

    return render_to_response('sdvapp/suggestion_update.html',
                              {'form' : form},
                              context_instance=RequestContext(request))

@login_required
def create_suggestion(request):

    if request.method == 'POST':
        form = SuggestionForm(request.POST)

        if form.is_valid():
            instance = form.save(commit=False)
            instance.suggested_by = request.user
            instance.save()

            return HttpResponseRedirect(reverse('suggestion_list'))

    else:
        form = SuggestionForm()

    return render_to_response('sdvapp/suggestion_create.html',
                              {'form' : form},
                              context_instance=RequestContext(request))