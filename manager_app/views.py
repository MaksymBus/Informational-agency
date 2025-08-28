from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from manager_app.forms import (
    TopicForm,
    NewspaperForm,
    RedactorCreationForm,
    TopicSearchForm,
    NewspaperSearchForm,
    RedactorSearchForm
)
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

    def get_context_data(
        self, *, object_list=..., **kwargs
    ):
        context = super(TopicListView, self).get_context_data(**kwargs)
        name = self.request.GET.get("name", "")
        context["search_form"] = TopicSearchForm(
            initial={"name": name}
        )
        return context

    def get_queryset(self):
        queryset = Topic.objects.all()
        form = TopicSearchForm(self.request.GET)
        if form.is_valid():
            return queryset.filter(name__icontains=form.cleaned_data["name"])
        return queryset


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

    def get_context_data(
        self, *, object_list=..., **kwargs
    ):
        context = super(NewspaperListView, self).get_context_data(**kwargs)
        title = self.request.GET.get("title", "")
        context["search_form"] = NewspaperSearchForm(
            initial={"title": title}
        )
        return context

    def get_queryset(self):
        queryset = Newspaper.objects.all()
        form = NewspaperSearchForm(self.request.GET)
        if form.is_valid():
            return queryset.filter(name__icontains=form.cleaned_data["title"])
        return queryset


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

    def get_context_data(
        self, *, object_list=..., **kwargs
    ):
        context = super(RedactorListView, self).get_context_data(**kwargs)
        username = self.request.GET.get("username", "")
        context["search_form"] = RedactorSearchForm(
            initial={"username": username}
        )
        return context

    def get_queryset(self):
        queryset = get_user_model().objects.all()
        form = RedactorSearchForm(self.request.GET)
        if form.is_valid():
            return queryset.filter(
                name__icontains=form.cleaned_data["username"]
            )
        return queryset


class RedactorCreatView(LoginRequiredMixin, generic.CreateView):
    model = get_user_model()
    form_class = RedactorCreationForm
    success_url = reverse_lazy("manager_app:redactor-list")


class RedactorDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = get_user_model()
    success_url = reverse_lazy("manager_app:redactor-list")


class RedactorDetailView(LoginRequiredMixin, generic.DetailView):
    model = get_user_model()
    queryset = get_user_model().objects.all().prefetch_related(
        "newspapers__topics"
    )


@login_required
def toggle_assign_to_newspaper(request, pk):
    redactor = get_user_model().objects.get(id=request.user.id)
    if Newspaper.objects.get(id=pk) in redactor.newspapers.all():
        redactor.newspapers.remove(pk)
    else:
        redactor.newspapers.add(pk)
    return HttpResponseRedirect(
        reverse_lazy("manager_app:newspaper-detail", args=[pk])
    )
