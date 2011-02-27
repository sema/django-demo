from django import forms

from models import Suggestion, Comment

class SuggestionForm(forms.ModelForm):
    class Meta:
        model = Suggestion
        fields = ('title', 'description', )

class ExampleForm(forms.Form):
    title = forms.CharField(max_length=255)
    description = forms.CharField(widget=forms.Textarea())

    a_number = forms.IntegerField()

class ExtendedSuggestionForm(forms.ModelForm):
    class Meta:
        model = Suggestion
        fields = ('title', 'description', 'status')

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment',)