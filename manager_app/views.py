from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from manager_app.forms import TopicForm, NewspaperForm, RedactorCreationForm
from manager_app.models import Topic, Redactor, Newspaper


@login_required
def index(request):
    num_topics = Topic.objects.count()
    num_redactors = Redactor.objects.count()
    num_newspapers = Newspaper.objects.count()

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


class NewspaperListView(LoginRequiredMixin, generic.ListView):
    model = Newspaper
    context_object_name = "newspaper-list"
    template_name = "manager_app/newspaper_list.html"
    paginate_by = 5


class NewspaperCreatView(LoginRequiredMixin, generic.CreateView):
    model = Newspaper
    form_class = NewspaperForm
    success_url = reverse_lazy("manager_app:newspaper-list")


class NewspaperUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Newspaper
    form_class = NewspaperForm
    success_url = reverse_lazy("manager_app:newspaper-list")


class NewspaperDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Newspaper
    success_url = reverse_lazy("manager_app:newspaper-list")


class NewspaperDetailView(LoginRequiredMixin, generic.DetailView):
    model = Newspaper


class RedactorListView(LoginRequiredMixin, generic.ListView):
    model = get_user_model()
    context_object_name = "redactor-list"
    template_name = "manager_app/redactor_list.html"
    paginate_by = 5


class RedactorCreatView(LoginRequiredMixin, generic.CreateView):
    model = get_user_model()
    form_class = RedactorCreationForm
    success_url = reverse_lazy("manager_app:redactor-list")


class RedactorDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = get_user_model()
    success_url = reverse_lazy("manager_app:redactor-list")


class RedactorDetailView(LoginRequiredMixin, generic.DetailView):
    model = get_user_model()
    queryset = get_user_model().objects.all().prefetch_related("newspapers__topics")


@login_required
def toggle_assign_to_newspaper(request, pk):
    redactor = get_user_model().objects.get(id=request.user.id)
    if Newspaper.objects.get(id=pk) in redactor.newspapers.all():
        redactor.newspapers.remove(pk)
    else:
        redactor.newspapers.add(pk)
    return HttpResponseRedirect(reverse_lazy("manager_app:newspaper-detail", args=[pk]))
