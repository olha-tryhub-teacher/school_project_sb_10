
from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Event)
# class PostAdmin(admin.ModelAdmin):
#     list_display = ('title','author','date_posted')
#     list_information = ('title', 'media', 'links')
#     list_filter = ('author','date_posted')
#     list_comment = ('new','old','popular')
    #list_information_user =(name)