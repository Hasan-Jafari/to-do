from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions

from core.models import Task
from core.serializers import TaskSerializer



class TaskViewSet(ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)