from django.urls import path
from reminderapi import views
from rest_framework.routers import DefaultRouter
router=DefaultRouter()
router.register("todos",views.TodooViewSet,basename="todos")

urlpatterns=[
    path("register/",views.UserCreationView.as_view(),name="signup")
]+router.urls