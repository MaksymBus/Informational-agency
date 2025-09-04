from django.contrib.auth import get_user_model
from django.test import TestCase, RequestFactory

from django.urls import reverse

from manager_app.models import Topic, Newspaper
from manager_app.views import NewspaperListView

NEWSPAPER_URL = reverse("manager_app:newspaper-list")


class PublicNewspaperTest(TestCase):
    def test_login_required(self):
        res = self.client.get(NEWSPAPER_URL)
        self.assertNotEqual(res.status_code, 200)


class PrivateNewspaperTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="test_username",
            password="test123"
        )
        self.topic = Topic.objects.create(
            name="test_first_topic"
        )
        self.first_newspaper = Newspaper.objects.create(
            title="Test_Newspaper",
            content="Some_content",
            published_date="2025-02-04"
        )
        self.first_newspaper.topics.add(self.topic)
        self.first_newspaper.publishers.add(self.user)
        self.second_newspaper = Newspaper.objects.create(
            title="Test_Second_Newspaper",
            content="Some_content",
            published_date="2022-02-04"
        )
        self.second_newspaper.topics.add(self.topic)
        self.second_newspaper.publishers.add(self.user)
        self.client.force_login(self.user)
        self.factory = RequestFactory()

    def test_retrieve_newspapers(self):
        res = self.client.get(NEWSPAPER_URL)
        self.assertEqual(res.status_code, 200)
        newspapers = Newspaper.objects.all()
        self.assertEqual(
            list(res.context["newspaper_list"]),
            list(newspapers),
        )
        self.assertTemplateUsed(res, "manager_app/newspaper_list.html")

    def test_create_newspaper(self):
        newspaper_data = {
            "title": "new_test_title",
            "content": "Some_new_content",
            "topics": [self.topic.pk],
            "publishers": [self.user.pk]
        }
        res = self.client.post(
            reverse("manager_app:newspaper-create"),
            newspaper_data
        )
        self.assertEqual(res.status_code, 302)
        self.assertEqual(Newspaper.objects.count(), 3)
        self.assertRedirects(res, "/newspapers/")

    def test_update_newspaper(self):
        newspaper_update = {
            "title": "update_test_title",
            "content": "Some_new_content",
            "topics": [self.topic.pk],
            "publishers": [self.user.pk]
        }
        res = self.client.post(
            reverse(
                "manager_app:newspaper-update",
                args=[self.first_newspaper.pk]
            ),
            newspaper_update
        )
        self.assertEqual(res.status_code, 302)
        self.assertRedirects(res, "/newspapers/")
        self.first_newspaper.refresh_from_db()
        self.assertEqual(self.first_newspaper.title, "update_test_title")

    def test_delete_newspaper(self):
        res = self.client.post(
            reverse(
                "manager_app:newspaper-delete",
                args=[self.first_newspaper.pk]
            )
        )
        self.assertEqual(res.status_code, 302)
        self.assertEqual(Newspaper.objects.count(), 1)
        self.assertRedirects(res, "/newspapers/")

    def test_get_context_data_newspaper(self):
        request = self.factory.get(
            reverse("manager_app:newspaper-list"),
            {"title": "test_newspaper"}
        )
        request.user = self.user

        view = NewspaperListView()
        view.setup(request)
        queryset = view.get_queryset()

        self.assertEqual(queryset.count(), 1)
        self.assertEqual(queryset.first().title, "Test_Newspaper")
