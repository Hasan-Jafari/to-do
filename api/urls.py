from django.urls import path, include



app_name = 'api'

urlpatterns = [
    path('task/', include('api.endpoints.task', namespace='task')),
]
