from django.shortcuts import render
from task.models import Todoo
from task_api.serilaizers import TodoSerializer
from rest_framework.decorators import action

# Create your views here.
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

class TodooViewsetView(ModelViewSet):
    serializer_class=TodoSerializer
    queryset=Todoo.objects.all()

    # localhost:8000/api/todos/pending
    # get
    
    @action(methods=["get"],detail=False)
    def pending(self,request,*args,**kwargs):
        qs=Todoo.objects.filter(status=True)
        serializer=TodoSerializer(qs,many=True)
        return Response(data=serializer.data)

