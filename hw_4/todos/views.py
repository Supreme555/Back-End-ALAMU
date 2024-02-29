from django.shortcuts import render, get_object_or_404, redirect
from .models import TodoList, Todo

def index(request):
    todo_lists = TodoList.objects.all()
    return render(request, 'todos/index.html', {'todo_lists': todo_lists})

def detail(request, todo_list_id):
    todo_list = get_object_or_404(TodoList, pk=todo_list_id)
    return render(request, 'todos/detail.html', {'todo_list': todo_list})

# Добавьте остальные представления по аналогии
from .forms import TodoListForm

def create_todolist(request):
    if request.method == "POST":
        form = TodoListForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = TodoListForm()

    return render(request, 'todos/create_todolist.html', {'form': form})