from rest_framework.routers import DefaultRouter
from django.urls import path, include

from api.views import TaskViewSet



router = DefaultRouter()
app_name = 'task'
router.register('', TaskViewSet, basename='tasks')

urlpatterns = [
    path('', include(router.urls)),
]
