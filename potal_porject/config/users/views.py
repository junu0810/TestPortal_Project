from http.client import HTTPResponse
from django.shortcuts import render

# Create your views here.
def hello_world(request):
    return HTTPResponse("hello_world")