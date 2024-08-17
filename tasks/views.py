from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Task
from .forms import TaskForm
from django.db.models import Count
from datetime import timedelta
from django.utils.timezone import now

def landing_page(request):
    return render(request, 'tasks/landing_page.html')

@login_required
def task_entry(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = TaskForm()
    return render(request, 'tasks/task_entry.html', {'form': form})

@login_required
def dashboard(request):
    tasks = Task.objects.all()
    return render(request, 'tasks/dashboard.html', {'tasks': tasks})

# Custom Report View
@login_required
def task_report(request):
    # Get tasks due in the next 30 days
    end_date = now() + timedelta(days=30)
    upcoming_tasks = Task.objects.filter(due_by__lte=end_date)

    # Group by priority
    priority_counts = upcoming_tasks.values('priority').annotate(count=Count('id'))

    # Prepare data for the report
    report_data = {
        'upcoming_tasks': upcoming_tasks,
        'priority_counts': priority_counts,
    }

    return render(request, 'tasks/task_report.html', report_data)