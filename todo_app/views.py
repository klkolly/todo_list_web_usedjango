from django.shortcuts import render
from .models import Todo
from django.utils import timezone

from django.http import HttpResponseRedirect

from django.views.decorators.csrf import csrf_exempt


# Create your views here.
def index(request):
    todo_list = Todo.objects.all()
    list_length = Todo.objects.count()
    print(list_length)
    
    pass_to_template = {
        'todo_list':todo_list,
        'list_length':list_length
        }
    return render(request, 'todo_app/index.html', pass_to_template) 

@csrf_exempt
def addtolist(request):
    todo_thing = request.POST['todo_thing']
    Todo.objects.create(list_text = todo_thing, date=timezone.now())
    return HttpResponseRedirect('/') 

@csrf_exempt
def delete_task(request):
    delete_task_id = request.POST['item_id']
    Todo.objects.get(id=delete_task_id).delete()
    return HttpResponseRedirect('/') 