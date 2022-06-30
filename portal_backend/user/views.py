from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
import json

def signin(request):
    inputData = json.loads(request.body)
    return JsonResponse({'message': inputData }, status= 200)

