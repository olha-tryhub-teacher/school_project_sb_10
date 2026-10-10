from django.db import models
from django.contrib.auth.models import User

class ForumCategory(models.Model):
    #Категории форума
    name = models.CharField(max_length=100, verbose_name="Название категории")
    description = models.TextField(blank=True, verbose_name="Описание")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория форума"
        verbose_name_plural = "Категории форума"


class ForumTopic(models.Model):
    #Темы форума
    title = models.CharField(max_length=255, verbose_name="Заголовок темы")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='forum_topics', verbose_name="Автор")
    category = models.ForeignKey(ForumCategory, on_delete=models.CASCADE, related_name='topics', verbose_name="Категория")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Тема форума"
        verbose_name_plural = "Темы форума"
        ordering = ['-created_at']


class ForumPost(models.Model):
    #Сообщения внутри тем
    topic = models.ForeignKey(ForumTopic, on_delete=models.CASCADE, related_name='posts', verbose_name="Тема")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='forum_posts', verbose_name="Автор")
    content = models.TextField(verbose_name="Текст сообщения")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата отправки")

    def __str__(self):
        return f"Пост от {self.author.username} в теме {self.topic.title}"

    class Meta:
        verbose_name = "Сообщение форума"
        verbose_name_plural = "Сообщения форума"
        ordering = ['created_at']
