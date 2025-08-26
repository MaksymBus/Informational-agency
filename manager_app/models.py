from django.db import models

# Create your models here.

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

