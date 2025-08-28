from django import forms
from django.contrib.auth import get_user_model

from manager_app.models import Topic, Newspaper


class TopicForm(forms.ModelForm):

    class Meta:
        model = Topic
        fields = "__all__"
