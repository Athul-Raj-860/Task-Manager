from rest_framework import serializers
from .models import Task

class PostTask(serializers.ModelSerializer):
    TaskAssignedDate = serializers.DateField(input_formats=['%d-%m-%Y'],format='%d-%m-%Y')
    TaskCompleteDate = serializers.DateField(input_formats=['%d-%m-%Y'],format='%d-%m-%Y')
    class Meta:
        model = Task
        fields =['Id','Name', 'Status', 'TaskAssignedDate', 'TaskCompleteDate']