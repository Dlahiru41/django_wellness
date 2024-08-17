from django.urls import path
from .views import landing_page, task_entry, dashboard, TaskReportView

urlpatterns = [
    path('', landing_page, name='landing_page'),
    path('task-entry/', task_entry, name='task_entry'),
    path('dashboard/', dashboard, name='dashboard'),
    path('reports/', TaskReportView.as_view(), name='task_reports'),
]
