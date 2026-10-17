from django.db import models

# Create your models here.

class CalendarDay(models.Model):
    date = models.DateTimeField(max_length=50)
    notes = models.TextField(max_length=300)

class CalendarEvent(models.Model):
    # event = models.ForeignKey("events.Event")
    event = models.ForeignKey("Event", on_delete=models.CASCADE)
    date = models.DateField(max_length=50)

    # Create your models here.
class Event(models.Model):
    title = models.CharField(max_length=100, verbose_name="Заголовок")
    text = models.TextField(verbose_name="Текст посту")
    description = models.TextField()
    date_publication = models.DateField(auto_now_add=True, verbose_name="Дата публікації")
    date_settings_post = models.DateField()
    media_in_post = models.BooleanField()
    video_in_post = models.BooleanField()
    links_in_post = models.BooleanField()
    links_post = models.BooleanField()
    main_photo_post = models.BooleanField()
    main_video_post = models.BooleanField()
    from django.db import models