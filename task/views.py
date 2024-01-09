from django.shortcuts import render,redirect
from django.views.generic import View
from task.forms import TodoCreateForm,TodoChangeForm
from task.models import Todoo

# Create your views here.
class TodoCreateView(View):
    def get(self,request,*args,**kwargs):
        form=TodoCreateForm()
        return render(request,"todoo_add.html",{"form":form})
    
    def post(self,request,*args,**kwargs):
        form=TodoCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("todoo-list")
        else:
            return render(request,"todoo_add.html",{"form":form})

class TodoListView(View):
    def get(self,request,*args,**kwargs):
        qs=Todoo.objects.all()
        return render(request,"todos_lit.html",{"todos":qs})
    
class TodoDetailView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        qs=Todoo.objects.get(id=id)
        return render(request,"todoo_detail.html",{"todoo":qs})

class TodoDeleteView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        Todoo.objects.filter(id=id).delete()
        return redirect("todoo-list")

class TodoUpdateView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get('pk')
        obj=Todoo.objects.get(id=id)

        form=TodoChangeForm(instance=obj)
        return render(request,"todo_edit.html",{"form":form})
    def post(self,request,*aegs,**kwargs):
        id=kwargs.get("pk")
        obj=Todoo.objects.get(id=id)
        form=TodoChangeForm(request.POST,instance=obj)
        if form.is_valid():
            form.save()

            return redirect("todoo-list")
        else:
            return render(request,"todos_lit.html",{"form":form})