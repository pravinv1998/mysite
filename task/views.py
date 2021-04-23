from django import forms
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.

task = []


class NewTaskForm(forms.Form):
    task1 = forms.CharField(label='Add Task')
    # priority = forms.IntegerField(label='priority', min_value=1, max_value=5)


def index(request):
    if 'task' not in request.session:
        request.session['task']= []
        pass
    return render(request, 'task/index.html', {
        'task': request.session['task']
    })


def add(request):
    if request.method == "POST":
        form = NewTaskForm(request.POST)
        if form.is_valid():
            tasks = form.cleaned_data['task1'] #get all data of that pertucular form
            request.session['task'] +=[tasks]
            return HttpResponseRedirect(reverse('index'))
        else:
                return render(request, 'task/add.html', {
                    'form': form
                })




    return render(request, 'task/add.html', {
        'form': NewTaskForm()
    })
