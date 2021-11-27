import requests
import hashlib
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from django.conf import settings
from wxauth.models import WXUser

# Create your views here.


def index(request):
    return HttpResponse("Hello world.")


def wx_auth(request, code):
    wxapi = "https://api.weixin.qq.com/sns/jscode2session?appid={AppId}&secret={AppSecret}&js_code={code}&grant_type=authorization_code".format(
        AppId=settings.WX_MINIPROGRAM_APPID,
        AppSecret=settings.WX_MINIPROGRAM_SECRET_KEY,
        code=code
    )
    try:
        response = requests.get(wxapi)
        if(response.json().get('openid') == None):
            raise Exception()
    except Exception:
        return JsonResponse({"session": None})

    openid = response.json().get('openid')
    hashdata = hashlib.md5()
    hashdata.update(bytes(openid, encoding='utf-8'))
    session = hashdata.hexdigest()
    data = {
        "session": session,
    }
    if(not WXUser.objects.filter(openid=openid)):
        WXUser.objects.create(openid=openid, session=session)
    return JsonResponse(data)
