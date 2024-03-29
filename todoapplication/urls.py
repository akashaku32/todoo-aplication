"""
URL configuration for todoapplication project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from task.views import TodoCreateView,TodoListView,TodoDetailView,TodoDeleteView,TodoUpdateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('todos/add/',TodoCreateView.as_view(),name="todoo-add"),
    path('todos/list/',TodoListView.as_view(),name="todoo-list"),
    path('todos/<int:pk>',TodoDetailView.as_view(),name="todoo-detail"),
    path('todos/<int:pk>/remove/',TodoDeleteView.as_view(),name="todoo-delete"),
    path('todos/<int:pk>/edit/',TodoUpdateView.as_view(),name="todoo-update"),
    path("",include("reminder.urls")),
    path("api/",include("task_api.urls")),
    path("api/v2/",include("reminderapi.urls"))
]
