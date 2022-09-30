from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import FeedbackForm


# Create your views here.
def index(request):
    form = FeedbackForm()
    if request.method == 'POST':
        name = request.POST['name']
        if len(name) == 0:
            return render(request, 'feedback/feedback.html', context={'form': form})
        print(name)
        return HttpResponseRedirect('/done')
    return render(request, 'feedback/feedback.html', context={'form': form})


def done(request):
    return render(request, 'feedback/done.html')
