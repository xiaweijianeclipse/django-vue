from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
import re
import uuid
# Create your views here.

def phone_validator(value):
    if not re.match(r"^[1][3,4,5,7,8,9][0-9]{9}$",value):
        raise ValidationError("手机格式错误")

class MesssageSerializers(serializers.Serializer):
     phone = serializers.CharField(label="手机号",validators=[phone_validator])


class LoginView(APIView):

    def post(self, request, *args, **kwargs):
        if re.match(r"[1][3,4,5,7,8,9][0-9]{9}$", request.data.get('phone')):
            from api import models
            user_object,flag = models.UserInfo.objects.get_or_create(phone=request.data.get('phone'))
            user_object.token = str(uuid.uuid4())
            user_object.save()
            return Response({"status": True,'data':{"token":user_object.token,'phone':request.data.get('phone')}})


class MessageView(APIView):

    def get(self,request):
        ser = MesssageSerializers(data=request.query_params)
        if not ser.is_valid():
           return Response({"status":False,"message":'手机格式错误'})
        phone = ser.validated_data.get('phone')
        import random
        random_code = random.randint(1000,9999)


        # from django_redis import get_redis_connection
        # conn = get_redis_connection()
        # conn.set(phone,random_code,ex=30)
        # return Response({"status":"验证码发送成功 "})

        # import redis
        # pool = redis.ConnectionPool(host="127.0.0.1",port=6379)
        # conn = redis.Redis(connection_pool=pool)
        # conn.set(phone,random_code,ex=30)
        #
        #1.获取手机号
        #2.手机格式校验
        #3.生成随机验证码
        #4.把验证码发送到手机上
        #5.把验证码+手机号保留（30s过期）

