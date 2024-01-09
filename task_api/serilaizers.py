from task.models import Todoo
from rest_framework import serializers
class TodoSerializer(serializers.ModelSerializer):
    id=serializers.CharField(read_only=True)
    created_date=serializers.CharField(read_only=True)
    due_date=serializers.CharField(read_only=True)
    class Meta:
        model=Todoo
        fields="__all__" ""