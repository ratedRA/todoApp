from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import TodoItems

def todoView(request):
	all_items = TodoItems.objects.all()
	return render(request, 'todo.html',
		{'all_items' : all_items})

def addTodo(request):
	new_item = TodoItems(content = request.POST['content'])
	new_item.save()
	return HttpResponseRedirect('/')

def delTodo(request, todo_id):
	item_to_del = TodoItems.objects.get(id = todo_id)
	item_to_del.delete()
	return HttpResponseRedirect('/')