from django.urls import path
from potal_porject.config.users.views import hello_world

urlpatterns = [
    path('hello_world/', hello_world),
]