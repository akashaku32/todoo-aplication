from django.shortcuts import render,redirect
from django.db.models.query import QuerySet
from reminder.forms import RegistrationForm,LoginForm,TodooCreateForm,TodooChangeForm
from django.views.generic import View,TemplateView,FormView,ListView,DetailView,UpdateView
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from reminder.models import Todos
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator

# decorator

def signin_decorator(fn):
    def wrapper(request,*args,**kwargs):
        if not request.user.is_authenticated:
            messages.error(request,"invalid session")
            return redirect("signin")
        else:
            return fn(request,*args,**kwargs)
    return wrapper

class SignupView(View):
    def get(self,request,*args,**kwargs):
        form=RegistrationForm()
        return render(request,"signup.html",{"form":form})
    def post(self,request,*args,**kwargs):
        form=RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"registered successfully")
            return redirect("signin")
        else:
            messages.error(request,"not registered")
            return render(request,"signup.html",{"form":form})



# Create your views here.
class SignInView(View):
    def get(self,request,*args,**kwargs):
        form=LoginForm()
        return render(request,"login.html",{"form":form})
    def post(self,request,*args,**kwargs):
        form=LoginForm(request.POST)
        if form.is_valid():
            uname=form.cleaned_data.get("username")
            pswd=form.cleaned_data.get("password")
            usr=authenticate(request,username=uname,password=pswd)
            if usr:
                login(request,usr)
                messages.success(request,"login success")
                return redirect("index")
            else:
                messages.error(request,"invalid credentials!!")
                return render(request,"login.html",{"form":form})
@method_decorator(signin_decorator,name="dispatch")
class IndexView(TemplateView):
    template_name="index.html"

@method_decorator(signin_decorator,name="dispatch")
class TodooCreateview(FormView):
    
    template_name="reminder/todoo_add.html"
    form_class=TodooCreateForm
    def post(self,request,*args,**kwargs):
        form=TodooCreateForm(request.POST)
        if form.is_valid():
            Todos.objects.create(**form.cleaned_data,user=request.user)
            messages.success(request,"todo created successfully")
            return redirect("todo-add1")
        else:
            return render(request,"reminder/todoo_add.html",{"form":form})

@method_decorator(signin_decorator,name="dispatch")        
class TodoListView(ListView):
    template_name="reminder/todo_list.html"

    context_object_name="todos"
    model=Todos

@method_decorator(signin_decorator,name="dispatch")
class TodoDetailView(DetailView):
    template_name="reminder/todo_detail.html"
    context_object_name="todo"
    model=Todos

@method_decorator(signin_decorator,name="dispatch")
class TodoChangeView(UpdateView):
    template_name="reminder/todo_update.html"
    form_class=TodooChangeForm
    model=Todos
    success_url=reverse_lazy("todo-list")

@signin_decorator
def remove_todo(request,*args,**kwargs):
    id=kwargs.get("pk")
    Todos.objects.filter(id=id).delete()
    return redirect("todo-list")


 