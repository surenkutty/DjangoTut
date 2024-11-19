from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from rest_framework.generics import GenericAPIView
from rest_framework import status
from rest_framework.response import Response
from .serializers import UserRegisterSerializer,LoginViewSerializers
from .utils import send_code_to_user
from rest_framework.permissions import IsAuthenticated
# Create your views here.

class RegisterUserView(GenericAPIView):
    serializer_class=UserRegisterSerializer
    
    def post(self,request):
        user_data=request.data
        
        serializer=self.serializer_class(data=user_data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            user=serializer.data
            print(user)
            send_code_to_user(user['email'])
            return Response({
                'data':user,
                "message":f'hi{user['first_name']} thanks for Signing up'
            },status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
from .utils import OneTimePassword
class VerifyUserEmail(GenericAPIView):
    def post(self,request):
        otpcode=request.data.get('otp')
        try:
            user_code_obj=OneTimePassword.objects.get(code=otpcode)
            user=user_code_obj.user
            if not user.is_verified:
                user.is_verified=True
                user.save()
                return Response({
                    "message":'account email verify successfully'
                },status=status.HTTP_200_OK)
            return Response({
                "message":"code is invalid user already verified"
            },status=status.HTTP_204_NO_CONTENT)
        except OneTimePassword.DoesNotExist:
            return Response({
                "message":"passcode not provided"
            },status=status.HTTP_401_UNAUTHORIZED)

class LoginUserView(GenericAPIView):
    serializer_class=LoginViewSerializers
    def post(self,request):
        serializer=self.serializer_class(data=request.data,context={'request':request})
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
class TestAuthenticatedView(GenericAPIView):
    permission_classes=[IsAuthenticated]
    def get(self,request):
        data={
            'msg':"its working"
        }
        return Response(data=data,status=status.HTTP_200_OK)
    