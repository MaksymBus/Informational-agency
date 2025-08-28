from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from manager_app.forms import TopicForm
from manager_app.models import Topic, Redactor, Newspaper



@login_required
def index(request):
    num_topics = Topic.objects.count()
    num_redactors = Redactor.objects.count()
    num_newspapers = Newspaper.objects.count()

# Create your views here.
    context = {
        "num_topics": num_topics,
        "num_redactors": num_redactors,
        "num_newspapers": num_newspapers
    }

    return render(request, "manager_app/index.html", context=context)


class TopicListView(LoginRequiredMixin, generic.ListView):
    model = Topic
    context_object_name = "topic-list"
    template_name = "manager_app/topic_list.html"
    paginate_by = 5


class TopicCreatView(LoginRequiredMixin, generic.CreateView):
    model = Topic
    form_class = TopicForm
    success_url = reverse_lazy("manager_app:topic-list")


class TopicUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Topic
    form_class = TopicForm
    success_url = reverse_lazy("manager_app:topic-list")


class TopicDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Topic
    success_url = reverse_lazy("manager_app:topic-list")
