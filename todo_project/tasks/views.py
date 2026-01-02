from django.shortcuts import render, redirect, get_object_or_404
from .models import Task


def task_list(request):
    # ADD TASK
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description', '')
        reminder_time = request.POST.get('reminder_time') or None

        if title:
            Task.objects.create(
                title=title,
                description=description,
                reminder_time=reminder_time
            )
        return redirect('task_list')

    # SHOW TASKS
    tasks = Task.objects.all()
    return render(request, 'tasks/task_list.html', {'tasks': tasks})


def task_update(request, task_id):
    task = get_object_or_404(Task, id=task_id)

    if request.method == 'POST':
        task.title = request.POST.get('title')
        task.description = request.POST.get('description', '')
        task.reminder_time = request.POST.get('reminder_time') or None
        task.save()
        return redirect('task_list')

    return render(request, 'tasks/task_form.html', {'task': task})


def task_delete(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return redirect('task_list')


def toggle_complete(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.is_completed = not task.is_completed
    task.save()
    return redirect('task_list')
