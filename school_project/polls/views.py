from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, View
from django.contrib import messages
from .models import Poll, Choice, PollResponse, Answer


class PollListView(ListView):
    model = Poll
    context_object_name = "polls"
    template_name = "polls/poll_list.html"

    def get_queryset(self):
        return Poll.objects.filter(is_active="active").order_by('-created_at')


class PollDetailView(LoginRequiredMixin, DetailView):
    model = Poll
    context_object_name = "poll"
    template_name = "polls/poll_detail.html"

    def get_queryset(self):
        return Poll.objects.filter(is_active="active")

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()

        if PollResponse.objects.filter(poll=self.object, user=request.user).exists():
            messages.warning(request, "Вы уже прошли этот опрос.")
            return redirect('poll_results', pk=self.object.pk)

        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)


class PollSubmitView(LoginRequiredMixin, View):
    def post(self, request, pk):
        poll = get_object_or_404(Poll, pk=pk, is_active="active")

        if PollResponse.objects.filter(poll=poll, user=request.user).exists():
            messages.warning(request, "Вы уже прошли этот опрос.")
            return redirect('poll_results', pk=poll.pk)

        response = PollResponse.objects.create(poll=poll, user=request.user)

        for question in poll.questions.all():
            choice_id = request.POST.get(f'question_{question.id}')
            if choice_id:
                choice = get_object_or_404(Choice, id=choice_id, question=question)
                Answer.objects.create(
                    response=response,
                    question=question,
                    choice=choice
                )

        messages.success(request, "Ваши ответы успешно сохранены!")
        return redirect('poll_results', pk=poll.pk)


class PollResultsView(LoginRequiredMixin, DetailView):
    model = Poll
    context_object_name = "poll"
    template_name = "polls/poll_results.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        poll = self.object

        questions_data = []
        for question in poll.questions.all():
            choices_data = []
            total_answers = Answer.objects.filter(question=question).count()

            for choice in question.choices.all():
                count = choice.answers.count()
                percentage = (count / total_answers * 100) if total_answers > 0 else 0
                choices_data.append({
                    'choice': choice,
                    'count': count,
                    'percentage': round(percentage, 1)
                })

            questions_data.append({
                'question': question,
                'choices': choices_data,
                'total_answers': total_answers
            })

        context['questions_data'] = questions_data
        return context