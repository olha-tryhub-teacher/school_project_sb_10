from django.shortcuts import render, get_object_or_404
from .models import ForumCategory, ForumTopic, ForumPost

def category_list(request):
    #Страница: Список категорий
    categories = ForumCategory.objects.all()
    return render(request, 'forum/category_list.html', {'categories': categories})


def topic_list(request, category_id):
    #Страница: Список тем внутри категории
    category = get_object_or_404(ForumCategory, id=category_id)
    topics = category.topics.all()
    return render(request, 'forum/topic_list.html', {'category': category, 'topics': topics})

def topic_detail(request, topic_id):
   #Страница: Содержимое темы
    topic = get_object_or_404(ForumTopic, id=topic_id)
    posts = topic.posts.all()
    return render(request, 'forum/topic_detail.html', {'topic': topic, 'posts': posts})
