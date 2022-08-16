from django.urls import path
from .views import hello_world,users

urlpatterns = [
    path('hello_world/', hello_world.as_view()),
    path('' , users.as_view()),
]