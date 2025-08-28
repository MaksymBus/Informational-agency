from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator
from django.db import models


class Topic(models.Model):
    name = models.CharField(
        max_length=255,
        unique=True
    )

    class Meta:
        verbose_name = "topic"
        verbose_name_plural = "topics"

    def __str__(self):
        return self.name


class Redactor(AbstractUser):
    years_of_experience = models.IntegerField(
        default=0,
        blank=True,
        verbose_name="Years of Experience",
        validators=[MinValueValidator(0)]
    )

    class Meta:
        verbose_name = "redactor"
        verbose_name_plural = "redactors"

    def __str__(self):
        return f"{self.username} {self.first_name} {self.last_name}"


class Newspaper(models.Model):
    title = models.CharField(
        max_length=255
    )
    content = models.TextField(blank=True, default="")
    published_date = models.DateField(auto_now_add=True)
    topics = models.ManyToManyField(
        Topic,
        related_name="newspapers"
    )
    publishers = models.ManyToManyField(
        Redactor,
        related_name="newspapers"
    )

    class Meta:
        ordering = ["-published_date"]

    def __str__(self):
        return f"{self.title} {self.published_date}"
