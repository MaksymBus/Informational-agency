from django.contrib.auth import get_user_model
from django.test import TestCase

from manager_app.forms import (
    RedactorCreationForm,
    RedactorSearchForm,
    NewspaperForm,
    TopicForm,
    TopicSearchForm,
    NewspaperSearchForm
)
from manager_app.models import Topic


class RedactorCreationFormTest(TestCase):
    def test_redactor_creation_form(self):
        form_data = {
            "username": "test_username",
            "password1": "70Test123",
            "password2": "70Test123",
            "first_name": "test_first_name",
            "last_name": "test_last_name",
            "years_of_experience": 2
        }
        form = RedactorCreationForm(data=form_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data["username"], "test_username")
        self.assertEqual(form.cleaned_data["first_name"], "test_first_name")
        self.assertEqual(form.cleaned_data["last_name"], "test_last_name")
        self.assertEqual(form.cleaned_data["years_of_experience"], 2)


class NewspaperFormTests(TestCase):
    def setUp(self):
        self.topic1 = Topic.objects.create(name="Topic 1")
        self.topic2 = Topic.objects.create(name="Topic 2")
        self.redactor1 = get_user_model().objects.create(username="redactor1")
        self.redactor2 = get_user_model().objects.create(username="redactor2")

    def test_form_is_valid_with_data(self):
        form_data = {
            "title": "Test Newspaper",
            "content": "Test content",
            "topics": [self.topic1.id, self.topic2.id],
            "publishers": [self.redactor1.id]
        }
        form = NewspaperForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_form_is_invalid_without_title(self):
        form_data = {
            "title": "",
            "content": "Test content",
            "topics": [self.topic1.id],
            "publishers": [self.redactor1.id]
        }
        form = NewspaperForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn("title", form.errors)


class TopicFormTests(TestCase):

    def test_form_is_valid_with_name(self):
        form = TopicForm(data={"name": "Test Topic"})
        self.assertTrue(form.is_valid())

    def test_form_is_invalid_without_name(self):
        form = TopicForm(data={"name": ""})
        self.assertFalse(form.is_valid())
        self.assertIn("name", form.errors)


class SearchFormTests(TestCase):

    def test_topic_search_form_valid(self):
        form = TopicSearchForm(data={"name": "test"})
        self.assertTrue(form.is_valid())

    def test_topic_search_form_empty_is_valid(self):
        form = TopicSearchForm(data={"name": ""})
        self.assertTrue(form.is_valid())

    def test_newspaper_search_form_valid(self):
        form = NewspaperSearchForm(data={"title": "test"})
        self.assertTrue(form.is_valid())

    def test_redactor_search_form_valid(self):
        form = RedactorSearchForm(data={"username": "test_user"})
        self.assertTrue(form.is_valid())
