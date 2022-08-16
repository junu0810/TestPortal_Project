from django.http import HttpResponse,JsonResponse
from django.shortcuts import render
from django.views import View

import json

from .serializers import BaseUserSerializer


# Create your views here.
class hello_world(View):
    def get(self , request):    
       return HttpResponse('hello world') 

class users(View):
    def post(self , request , format = None):
        data = json.loads(request.body.decode('utf-8'))
        print('원래 방식::::' + data['email'])
        print('request.data::::' + self.request.data)
        post_serializer = BaseUserSerializer(
            email = request.body
        )
        if post_serializer.is_valid():
            board = post_serializer.save()
            return JsonResponse(post_serializer.data,status = statistics.HTTP_201_CREATED, safe=False)

        
        return JsonResponse(post_serializer.errors,status = status.HTTP_400_BAD_REQUEST, safe=False)
