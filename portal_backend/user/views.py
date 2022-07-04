from datetime import datetime
from email import message
from time import timezone
from django.http import  JsonResponse
import datetime
import json, jwt
import time


def signin(request):
    key = "secret"
    expired = datetime.datetime.utcnow()+datetime.timedelta(minutes=30)

    #토큰의 유효기간을 30분으로 부여하였음
    encoded = jwt.encode({"exp":expired,"userId": "baek1008"}, key , algorithm = "HS256")
    print(encoded)
    inputData = json.loads(request.body)
    
    #만약 유효기간 부분을 없애고 아래의 코드를 주석해제하면 401이 return 된다.
    #time.sleep(5)

    try:
        decoded = jwt.decode(encoded,key,algorithm = "HS256")
    #유효기간이 지난 토큰일 경우 출력 
    except jwt.ExpiredSignatureError:
        return JsonResponse({'message': 'expired Token' }, status= 401)
    #유효하지 않은 토큰(해독이 안되는 토큰)일 경우 출력
    except jwt.InvalidTokenError:
        return JsonResponse({'message': 'InvalidToken' }, status= 403)
    else:
        response = JsonResponse({'message': decoded }, status= 200)
        response.set_cookie('auth',encoded, expires=expired)
        return response

    #착안사항
    #쿠키발행을 할경우 쿠키 expired가 있지만 토큰의 expired도 따로설정해두는게 맞을까?

def getDashBoard(request):
    auth = request.COOKIES.get('auth')
    print('쿠키를 받았어요' + auth)
    return JsonResponse({'message':'ok'} , status =200)

