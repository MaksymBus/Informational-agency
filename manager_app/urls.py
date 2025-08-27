from django.urls import path

from manager_app.views import (
    index,
)

urlpatterns = [
    path("", index, name="index"),
]

app_name = "manager_app"
