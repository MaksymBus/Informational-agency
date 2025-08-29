from django.contrib.auth import get_user_model
from django.test import TestCase

from manager_app.models import Topic, Newspaper


class ModelTests(TestCase):
    def setUp(self):
        self.topic = Topic.objects.create(
            name="test_name"
        )

        self.redactor = get_user_model().objects.create_user(
            username="test_username_first",
            password="90Test1234",
            years_of_experience=2,
            first_name="test_first_name",
            last_name="test_last_name",
        )

    def test_topic_str(self):
        self.assertEqual(
            str(self.topic),
            self.topic.name
        )

    def test_newspaper_str(self):
        newspaper = Newspaper.objects.create(
            title="Test Newspaper",
            content="Some content",
            published_date="2025-02-04"
        )
        newspaper.topics.add(self.topic)
        newspaper.publishers.add(self.redactor)
        self.assertEqual(
            str(newspaper),
            f"{newspaper.title} {newspaper.published_date}"
        )

    def test_redactor_str(self):
        self.assertEqual(
            str(self.redactor),
            f"{self.redactor.username} "
            f"{self.redactor.first_name} "
            f"{self.redactor.last_name}"
        )

    def test_redactor_get_absolut_url(self):
        self.assertEqual(self.redactor.get_absolute_url(), "/redactors/1/")
