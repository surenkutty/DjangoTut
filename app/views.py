from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from rest_framework.generics import GenericAPIView
from rest_framework import status
from rest_framework.response import Response
from .serializers import SetNewPasswordSerializer,UserRegisterSerializer,LoginViewSerializers,PasswordResetRequestSerializer
from .utils import send_code_to_user
from rest_framework.permissions import IsAuthenticated
from .models import User,OneTimePassword
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
    
    
from django.utils.http import urlsafe_base64_decode
from django.utils.encoding import smart_str,DjangoUnicodeDecodeError
from django.contrib.auth.tokens import PasswordResetTokenGenerator  
class PasswordResetRequestView(GenericAPIView):
    serializer_class=PasswordResetRequestSerializer
    def post(self,request):
        serializer=self.serializer_class(data=request.data,context={'request':request})
        serializer.is_valid(raise_exception=True) 
        return Response({'message':"a link has been sent to your email to your password"},status=status.HTTP_200_OK)
    
class  PasswordResetConfirm(GenericAPIView):
    def get(self,request,uidb64,token):
        try:
            user_id=smart_str(urlsafe_base64_decode(uidb64))
            user=User.objects.get(id=user_id)
            if not PasswordResetTokenGenerator().check_token(user,token):
                return Response({"message":'token is invalid or has expired'},status=status.HTTP_401_UNAUTHORIZED)
            
            return Response({"sucess":True,"message":"credentials is valid",'uidb64':uidb64,'token':token},status=status.HTTP_200_OK)
        except DjangoUnicodeDecodeError:
            return Response({'message':"token is invalid or has expired"},status=status.HTTP_401_UNAUTHORIZED)
              
      
class SetPassword(GenericAPIView):
    serializer_class=SetNewPasswordSerializer
    def patch(self,request):
        serializer=self.serializer_class(data=request.data,context={'request':request})
        serializer.is_valid(raise_exception=True) 
        
        return Response({"message":"password reset successfully"})
