from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views import generic

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
