from rest_framework import serializers

from core.models import Task



class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = [
            'id',
            'user',
            'title',
            'description',
            'status',
            'deadline',
            'created_at',
            'updated_at'
        ]
        
        read_only_fields = ['id', 'user', 'created_at', 'updated_at']