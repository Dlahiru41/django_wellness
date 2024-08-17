from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Task
from .forms import TaskForm
from slick_reporting.views import SlickReportView
from slick_reporting.fields import SlickReportField
# from slick_reporting.columns import SlickReportColumn

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

# Reports
from django.db.models import Count
from datetime import timedelta
from django.utils.timezone import now

class TaskReportView(SlickReportView):
    report_model = Task
    date_field = 'due_by'

    chart_settings = [
        {
            'type': 'line',
            'data_source': 'due_by',
            'title_source': 'user_email',
            'plot_total': True,
            'title': 'Tasks Due in the Next 30 Days',
        },
        {
            'type': 'pie',
            'data_source': 'priority',
            'title_source': 'priority',
            'plot_total': True,
            'title': 'Tasks by Priority',
        }
    ]

    group_by = 'priority'

    columns = [
        # SlickReportField.create(SlickReportColumn, 'is_urgent', count=True),
        'task',
        'due_by'
    ]
