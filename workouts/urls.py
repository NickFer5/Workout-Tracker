from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.workout_log, name='workout-log'),
]
