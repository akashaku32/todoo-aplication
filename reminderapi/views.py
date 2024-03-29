from django.shortcuts import render
from django.contrib.auth.models import User
from reminderapi.serializers import UserSerializer,Todooserializer
from reminder.models import Todos
from rest_framework.viewsets import ViewSet,ModelViewSet

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework  import authentication
from rest_framework import permissions

class UserCreationView(APIView):
    def post(self,request,*args,**kwargs):
        serializer=UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)

class TodooViewSet(ViewSet):
    authentication_classes=[authentication.BasicAuthentication]
    permission_classes=[permissions.IsAuthenticated]
    def create(self,request,*args,**kwargs):
        serializer=Todooserializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)
        
    def list(self,request,*args,**kwargs):
        qs=Todos.objects.filter(user=request.user)
        serializer=Todooserializer(qs,many=True)
        return Response(data=serializer.data)
    
    def retrieve(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        qs=Todos.objects.get(id=id)
        serializer=Todooserializer(qs)
        return Response(data=serializer.data)
    
    def update(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        obj=Todos.objects.get(id=id)
        serializer=Todooserializer(data=request.data,instance=obj)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.error)



    



# Create your views here.
