from django.urls import path

from manager_app.views import (
    index,
    TopicListView,
    TopicCreatView,
    TopicUpdateView,
    TopicDeleteView,
    NewspaperListView,
    NewspaperCreatView,
    NewspaperUpdateView,
    NewspaperDeleteView,
    NewspaperDetailView,

)

urlpatterns = [
    path("", index, name="index"),
    path(
        "topics/",
        TopicListView.as_view(),
        name="topic-list"
    ),
    path(
        "topics/create/",
        TopicCreatView.as_view(),
        name="topic-create"
    ),
    path(
        "topics/<int>:pk/update/",
        TopicUpdateView.as_view(),
        name="topic-update"
    ),
    path(
        "topics/<int>:pk/delete/",
        TopicDeleteView.as_view(),
        name="topic-delete"
    ),
    path(
        "newspapers/",
        NewspaperListView.as_view(),
        name="newspaper-list"
    ),
    path(
        "newspapers/create/",
        NewspaperCreatView.as_view(),
        name="newspaper-create"
    ),
    path(
        "newspapers/<int>:pk/update/",
        NewspaperUpdateView.as_view(),
        name="newspaper-update"
    ),
    path(
        "newspapers/<int>:pk/",
        NewspaperDetailView.as_view(),
        name="newspaper-detail"
    ),
    path(
        "newspapers/<int>:pk/delete/",
        NewspaperDeleteView.as_view(),
        name="newspaper-delete"
    ),
]

app_name = "manager_app"
