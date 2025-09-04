from django.contrib.auth import get_user_model
from django.test import TestCase, RequestFactory
from django.urls import reverse

from manager_app.models import Newspaper
from manager_app.views import NewspaperListView, RedactorListView

REDACTOR_URL = reverse("manager_app:redactor-list")


class PublicRedactorTest(TestCase):
    def test_login_required(self):
        res = self.client.get(REDACTOR_URL)
        self.assertNotEqual(res.status_code, 200)


class PrivateRedactorTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="test_username",
            password="test123",
        )
        self.redactor = get_user_model().objects.create_user(
            username="test_username_first",
            password="90Test1234",
            years_of_experience=2,
            first_name="test_first_name",
            last_name="test_last_name",
        )
        self.client.force_login(self.user)
        self.factory = RequestFactory()

    def test_retrieve_redactors(self):
        res = self.client.get(REDACTOR_URL)
        self.assertEqual(res.status_code, 200)
        redactors = get_user_model().objects.all()
        self.assertEqual(
            list(res.context["redactor_list"]),
            list(redactors),
        )
        self.assertTemplateUsed(res, "manager_app/redactor_list.html")

    def test_create_redactor(self):
        redactor_data = {
            "username": "test_username_new",
            "password1": "90Test1234",
            "password2": "90Test1234",
            "years_of_experience": 3,
            "first_name": "test_first_name",
            "last_name": "test_last_name"
        }
        res = self.client.post(
            reverse("manager_app:redactor-create"),
            redactor_data
        )
        self.assertEqual(res.status_code, 302)
        self.assertEqual(get_user_model().objects.count(), 3)
        self.assertRedirects(res, "/redactors/")

    def test_delete_redactor(self):
        res = self.client.post(
            reverse("manager_app:redactor-delete", args=[self.redactor.pk])
        )
        self.assertEqual(res.status_code, 302)
        self.assertEqual(get_user_model().objects.count(), 1)
        self.assertRedirects(res, "/redactors/")

    def test_get_context_data_redactor(self):
        request = self.factory.get(
            reverse("manager_app:redactor-list"),
            {"username": "test_username_first"}
        )
        request.user = self.user

        view = RedactorListView()
        view.setup(request)
        queryset = view.get_queryset()

        self.assertEqual(queryset.count(), 1)
        self.assertEqual(queryset.first().username, "test_username_first")
