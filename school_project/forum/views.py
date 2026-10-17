from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
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
    #Страница темы с сообщениями и формой создания нового ответа
    topic = get_object_or_404(ForumTopic, id=topic_id)
    posts = topic.posts.all()

    #Если пользователь отправил форму с новым сообщением
    if request.method == 'POST':
        #Проверяем, залогинен ли пользователь
        if request.user.is_authenticated:
            content = request.POST.get('content')
            if content:
                ForumPost.objects.create(
                    topic=topic,
                    author=request.user,
                    content=content
                )
                return redirect('forum:topic_detail', topic_id=topic.id)
        else:

            return redirect('admin:login')

    return render(request, 'forum/topic_detail.html', {'topic': topic, 'posts': posts})

