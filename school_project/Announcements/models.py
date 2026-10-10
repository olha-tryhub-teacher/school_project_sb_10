from django.db import models
from django.contrib.auth.models import User

class Announcement(models.Model):
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    content = models.TextField(verbose_name="Вміст")
    # Добавляем поле для картинки (фото будут сохраняться в папку announcements_images/)
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