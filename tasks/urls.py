from django.urls import path, include
from django.contrib import admin
from .views import landing_page, task_entry, dashboard, task_report

urlpatterns = [
    path('', landing_page, name='landing_page'),
    path('task-entry/', task_entry, name='task_entry'),
    path('dashboard/', dashboard, name='dashboard'),
    path('task-report/', task_report, name='task_report'),
]
