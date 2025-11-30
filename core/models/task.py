from django.db import models
from django.contrib.auth import get_user_model

from .base import BaseModel



class Status(models.TextChoices):
    PENDING = 'pending', 'Pending'
    DONE = 'done', 'Done'
        
class Task(BaseModel):
    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='tasks'
    )
    title = models.CharField(max_length=120)
    description = models.TextField(blank=True)
    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.PENDING
    )
    deadline = models.DateTimeField(null=True, blank=True)
    
    def __str__(self):
        return self.title