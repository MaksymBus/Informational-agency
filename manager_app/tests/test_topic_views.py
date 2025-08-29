from django.contrib.auth import get_user_model
from django.test import TestCase, RequestFactory
from django.urls import reverse

from manager_app.models import Topic
from manager_app.views import TopicListView

TOPIC_URL = reverse("manager_app:topic-list")


class PublicTopicTest(TestCase):
    def test_login_required(self):
        res = self.client.get(TOPIC_URL)
        self.assertNotEqual(res.status_code, 200)


class PrivateTopicTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="test_username",
            password="test123"
        )
        self.first_topic = Topic.objects.create(
            name="test_first_topic"
        )
        self.second_topic = Topic.objects.create(
            name="test_second_topic"
        )
        self.client.force_login(self.user)
        self.factory = RequestFactory()

    def test_retrieve_topics(self):
        res = self.client.get(TOPIC_URL)
        self.assertEqual(res.status_code, 200)
        topics = Topic.objects.all()
        self.assertEqual(
            list(res.context["topic_list"]),
            list(topics),
        )
        self.assertTemplateUsed(res, "manager_app/topic_list.html")

    def test_create_topic(self):
        topic_data = {
            "name": "test_name",
        }
        res = self.client.post(
            reverse("manager_app:topic-create"),
            topic_data
        )
        self.assertEqual(res.status_code, 302)
        self.assertEqual(Topic.objects.count(), 3)
        self.assertRedirects(res, "/topics/")

    def test_update_topic(self):
        topic_update = {
            "name": "test_name_update",
        }
        res = self.client.post(
            reverse("manager_app:topic-update", args=[self.first_topic.pk]),
            topic_update
        )
        self.assertEqual(res.status_code, 302)
        self.first_topic.refresh_from_db()
        self.assertEqual(self.first_topic.name, "test_name_update")
        self.assertRedirects(res, "/topics/")

    def test_delete_topic(self):
        res = self.client.post(
            reverse("manager_app:topic-delete", args=[self.first_topic.pk])
        )
        self.assertEqual(res.status_code, 302)
        self.assertEqual(Topic.objects.count(), 1)
        self.assertRedirects(res, "/topics/")

    def test_get_context_data_topic(self):
        request = self.factory.get(
            reverse("manager_app:topic-list"), {"name": "Test_first_topic"}
        )
        request.user = self.user

        view = TopicListView()
        view.setup(request)
        queryset = view.get_queryset()

        self.assertEqual(queryset.count(), 1)
        self.assertEqual(queryset.first().name, "test_first_topic")
