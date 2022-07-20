from csv import reader
from datetime import datetime

from django.http import  HttpResponseRedirect, JsonResponse
import datetime
import json, jwt
from django.shortcuts import redirect
import time

global key
key = "secret"

def signin(request):
    expired = datetime.datetime.utcnow()+datetime.timedelta(minutes=30)

    #토큰의 유효기간을 30분으로 부여하였음
    encoded = jwt.encode({"exp":expired,"userId": "baek1008"}, key , algorithm = "HS256").decode('utf-8')
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
        print(decoded)
        response = JsonResponse({'message': decoded }, status= 200)
        response.set_cookie('auth',encoded, expires=expired)
        return response

    #착안사항
    #쿠키발행을 할경우 쿠키 expired가 있지만 토큰의 expired도 따로설정해두는게 맞을까?

def getDashBoard(request):
    # auth = request.COOKIES.get('auth')

    # print('쿠키를 받았어요' + auth)
    
    # #토큰 해독한다.
    # try:
    #     decoded = jwt.decode(auth,key,algorithms=["HS256"])
    #     print(decoded)

    # #유효기간이 지난 토큰일 경우 출력 
    # except jwt.ExpiredSignatureError:
    #     return JsonResponse({'message': 'expired Token' }, status= 401)

    # #유효하지 않은 토큰(해독이 안되는 토큰)일 경우 출력
    # except jwt.InvalidTokenError:
    #     return JsonResponse({'message': 'InvalidToken' }, status= 403)
        
    #else:
    print('반응')
    # res = HttpResponseRedirect('https://localhost:3001/', status=301)
    # res.headers.setdefault(key='Access-Control-Allow-Origin',value='http://localhost:3000')
    # return res
    # return redirect('https://hms.imtrial.com')
    # dataURL = json.loads(request.body.decode('utf-8'))
    # print(dataURL['url'])
    return redirect('http://localhost:3001')
    # return redirect(dataURL['url'])
    # return reader(request,'http://localhost:3000')