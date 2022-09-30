from django.shortcuts import render
from django.http import HttpResponseRedirect


# Create your views here.
def index(request):
    if request.method == 'POST':
        name = request.POST['name']
        print(name)
        return HttpResponseRedirect('/done')
    return render(request, 'feedback/feedback.html')

def done(request):
    return render(request, 'feedback/done.html')