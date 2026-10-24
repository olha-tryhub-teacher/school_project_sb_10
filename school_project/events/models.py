
from django.db import models
from django.contrib.auth.models import User


class Event(models.Model):
    title = models.CharField(
        max_length=100,
        verbose_name="Назва події"
    )
    description = models.TextField(
        verbose_name="Опис"
    )
    date = models.DateField(
        verbose_name="Дата проведення"
    )
    time = models.TimeField(
        verbose_name="Час проведення"
    )
    location = models.CharField(
        max_length=200,
        verbose_name="Місце проведення"
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="created_events",
        verbose_name="Автор"
    )
    participants = models.ManyToManyField(
        User,
        blank=True,
        related_name="joined_events",
        verbose_name="Учасники"
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        ordering = ["date", "time"]
        verbose_name = "Подія"
        verbose_name_plural = "Події"

    def __str__(self):
        return self.title
