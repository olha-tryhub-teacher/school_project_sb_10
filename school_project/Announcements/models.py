from django.db import models
from django.contrib.auth.models import User

class Announcement(models.Model):
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    content = models.TextField(verbose_name="Вміст")
    image = models.ImageField(upload_to='announcements_images/', blank=True, null=True, verbose_name="Фото")
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name="Автор"
    )
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name="Дата створення"
    )
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name="Дата оновлення"
    )
    is_active = models.BooleanField(default=True, verbose_name="Активно")

    def __str__(self):
        return self.title


class Reaction(models.Model):
    REACTION_CHOICES = [
        ('heart', '❤️ Сердечко'),
        ('thumbs_up', '👍 Клас'),
        ('thumbs_down', '👎 Дизлайк'),
    ]

    announcement = models.ForeignKey(Announcement, on_delete=models.CASCADE, related_name='reactions', verbose_name="Оголошення")
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Користувач")
    reaction_type = models.CharField(max_length=20, choices=REACTION_CHOICES, verbose_name="Тип реакції")

    class Meta:
        verbose_name = "Реакція"
        verbose_name_plural = "Реакції"
        unique_together = ('announcement', 'user')

    def __str__(self):
        return f'{self.user.username} -> {self.get_reaction_type_display()}'


class Comment(models.Model):
    announcement = models.ForeignKey(Announcement, on_delete=models.CASCADE, related_name='comments', verbose_name="Оголошення")
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Автор коментаря")
    text = models.TextField(verbose_name="Текст коментаря")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата створення")

    class Meta:
        verbose_name = "Коментар"
        verbose_name_plural = "Коментарі"
        ordering = ['created_at']

    def __str__(self):
        return f'Коментар від {self.user.username}'