from django.urls import path

from task_api import views
from rest_framework.routers import DefaultRouter
router=DefaultRouter()
router.register("v1/todos",views.TodooViewsetView,basename="todos")

urlpatterns=[

]+router.urls