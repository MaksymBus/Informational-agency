from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from manager_app.models import Newspaper, Redactor, Topic


class IndexViewTests(TestCase):

    def setUp(self):
        self.topic = Topic.objects.create(
            name="Test Topic"
        )
        self.redactor = get_user_model().objects.create_user(
            username="test_username_first",
            password="90Test1234",
            years_of_experience=2,
            first_name="test_first_name",
            last_name="test_last_name",
        )
        self.newspaper = Newspaper.objects.create(
            title="Test Newspaper",
            content="Some content",
            published_date="2025-02-04"
        )
        self.newspaper.topics.add(self.topic)
        self.newspaper.publishers.add(self.redactor)

    def test_index_view_status_code(self):
        response = self.client.get(reverse("manager_app:index"))
        self.assertEqual(response.status_code, 200)

    def test_index_view_context(self):
        response = self.client.get(reverse("manager_app:index"))
        self.assertEqual(response.context["num_newspapers"], 1)
        self.assertEqual(response.context["num_redactors"], 1)
        self.assertEqual(response.context["num_topics"], 1)

    def test_index_view_empty_data(self):
        Newspaper.objects.all().delete()
        Redactor.objects.all().delete()
        Topic.objects.all().delete()

        response = self.client.get(reverse("manager_app:index"))
        self.assertEqual(response.context["num_newspapers"], 0)
        self.assertEqual(response.context["num_redactors"], 0)
        self.assertEqual(response.context["num_topics"], 0)