from django.urls import path

from . import views

urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    path("filemanager/", views.filemanager, name="filemanager"),
    path("payroll/", views.payroll, name="payroll"),
    path("performance/", views.performance, name="performance"),
    path("screening/", views.screening, name="screening"),
    path("chatbot/", views.chatbot, name="chatbot"),
]
