from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.conf import settings

from .models import Choice, Question

app_name = 'cmct'

class IndexView(generic.ListView):
    template_name = f'{app_name}/index.html'
    context_object_name = 'latest_question_list' # default is object_list
    app_url = settings.APP_URL[app_name]

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in the publisher
        context['app_url'] = self.app_url
        return context

class DetailView(generic.DetailView):
    model = Question
    template_name = f'{app_name}/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = f'{app_name}/results.html'

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, f'{app_name}/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse(f'{app_name}:results', args=(question.id,)))
