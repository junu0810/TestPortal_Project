from pydoc import visiblename
from django.urls import path
from . import views


urlpatterns = [
    path('', views.signin),
    path('Dashboard', views.getDashBoard)
]