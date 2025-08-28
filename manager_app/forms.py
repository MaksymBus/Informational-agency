from django import forms
from django.contrib.auth import get_user_model

from manager_app.models import Topic, Newspaper


class TopicForm(forms.ModelForm):

    class Meta:
        model = Topic
        fields = "__all__"


class NewspaperForm(forms.ModelForm):
    topics = forms.ModelMultipleChoiceField(
        queryset=Topic.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )
    redactors = forms.ModelMultipleChoiceField(
        queryset=get_user_model().objects.all(),
        widget=forms.CheckboxSelectMultiple
    )

    class Meta:
        model = Newspaper
        fields = "__all__"
