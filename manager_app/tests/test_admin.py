from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from manager_app.models import (
    Topic,
    Newspaper,
    Redactor
)

class AdminTests(TestCase):

    def setUp(self):
        self.superuser = get_user_model().objects.create_superuser(
            username="admin",
            password="password123",
            years_of_experience=15
        )
        self.staff_user = get_user_model().objects.create_user(
            username="staff",
            password="password123",
            years_of_experience=5,
            is_staff=True
        )

        self.topic = Topic.objects.create(name="Test Topic")
        self.redactor = Redactor.objects.create_user(
            username="test_redactor",
            password="password123",
            years_of_experience=1,
            is_staff=True
        )
        self.newspaper = Newspaper.objects.create(
            title="Test Newspaper",
            content="Test content",
            published_date="2025-08-28"
        )
        self.newspaper.topics.add(self.topic)
        self.newspaper.publishers.add(self.redactor)


    def test_admin_index_access(self):
        self.client.force_login(self.staff_user)
        response = self.client.get(reverse("admin:index"))
        self.assertEqual(response.status_code, 200)

    def test_topic_admin_list_view(self):
        self.client.force_login(self.superuser)
        response = self.client.get(reverse("admin:manager_app_topic_changelist"))
        self.assertContains(response, self.topic.name)
        self.assertEqual(response.status_code, 200)

    def test_newspaper_admin_list_view(self):
        self.client.force_login(self.superuser)
        response = self.client.get(reverse("admin:manager_app_newspaper_changelist"))
        self.assertContains(response, self.newspaper.title)
        self.assertEqual(response.status_code, 200)

    def test_redactor_admin_list_view(self):
        self.client.force_login(self.superuser)
        response = self.client.get(reverse("admin:manager_app_redactor_changelist"))
        self.assertContains(response, self.redactor.username)
        self.assertEqual(response.status_code, 200)

    def test_topic_admin_add_view(self):
        self.client.force_login(self.superuser)
        response = self.client.get(reverse("admin:manager_app_topic_add"))
        self.assertEqual(response.status_code, 200)

    def test_newspaper_admin_change_view(self):
        self.client.force_login(self.superuser)
        response = self.client.get(reverse(
            "admin:manager_app_newspaper_change", args=[self.newspaper.id]
        ))
        self.assertContains(response, self.newspaper.title)
        self.assertEqual(response.status_code, 200)
