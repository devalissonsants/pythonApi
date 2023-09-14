from rest_framework import serializers
from .models import TaskItem

class TaskItemSerializer(serializers.ModelSerializer):
    
    name = serializers.CharField(max_length=200)
    description = serializers.CharField(max_length=200)
    quantity = serializers.FloatField()

    class Meta:
        model = TaskItem
        fields = ('__all__')