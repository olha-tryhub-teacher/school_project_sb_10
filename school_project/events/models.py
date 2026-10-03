from django.db import models

# Create your models here.
class Events(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    date_publication = models.DateField()
    date_settings_post = models.DateField()
    media_in_post = models.BooleanField()
    video_in_post = models.BooleanField()
    links_in_post = models.BooleanField()
    links_post = models.BooleanField()
    main_photo_post = models.BooleanField()
    main_video_post = models.BooleanField()



