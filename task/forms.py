from django import forms
from task.models import Todoo

class TodoCreateForm(forms.ModelForm):
    class Meta:
        model=Todoo
        fields=["title","user","status","due_date"]
        widgets={
            "title":forms.TextInput(attrs={"class":"form-control"}),
            "user":forms.TextInput(attrs={"class":"form-control"}),
            "due_date":forms.DateInput(attrs={"class":"form-control"})
                 }
        
    # title=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    # user=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    # due_date=forms.DateTimeField(widget=forms.DateTimeInput(attrs={"type":"date"}))


# class TodoChangeForm(forms.Form):
#     title=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
#     due_date=forms.DateTimeField(widget=forms.DateTimeInput(attrs={"type":"date"}))
#     status=forms.BooleanField()


class TodoChangeForm(forms.ModelForm):
    class Meta:
        model=Todoo
        fields=["title","due_date","status"]

        widgets={
            "title":forms.TextInput(attrs={"class":"form-control"}),
            "due_date":forms.DateInput(attrs={"class":"form-control"})
                 }
        
