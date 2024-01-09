from django.urls import path
from reminder.views import SignInView,SignupView,IndexView,TodooCreateview,TodoListView,TodoDetailView,TodoChangeView,remove_todo

urlpatterns=[
path("signup",SignupView.as_view(),name="signup"),
path("",SignInView.as_view(),name="signin"),
path("index",IndexView.as_view(),name="index"),
path("add/",TodooCreateview.as_view(),name="todo-add1"),
path("all/",TodoListView.as_view(),name="todo-list"),
path("<int:pk>",TodoDetailView.as_view(),name="todo-detail"),
path("<int:pk>/update",TodoChangeView.as_view(),name="todo-update"),
path("<int:pk>/delete",remove_todo,name="todo-delete")
    
]
