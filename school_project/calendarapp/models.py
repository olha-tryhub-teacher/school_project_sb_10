from django.db import models

# Create your models here.

class CalendarDay(models.Model):
    date = models.DateTimeField(max_length=50)
    notes = models.TextField(max_length=300)

class CalendarEvent(models.Model):
    event = models.ForeignKey("events.Event")
    date = models.DateField(max_length=50)