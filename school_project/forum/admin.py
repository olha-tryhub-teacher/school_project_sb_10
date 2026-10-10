from django.contrib import admin
from .models import ForumCategory, ForumTopic, ForumPost

@admin.register(ForumCategory)
class ForumCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')
    search_fields = ('name',)

@admin.register(ForumTopic)
class ForumTopicAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'author', 'created_at')
    list_filter = ('category', 'created_at')
    search_fields = ('title',)

@admin.register(ForumPost)
class ForumPostAdmin(admin.ModelAdmin):
    list_display = ('id', 'topic', 'author', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('content',)


