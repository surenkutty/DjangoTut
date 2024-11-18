from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from rest_framework.generics import GenericAPIView
from rest_framework import status
from rest_framework.response import Response
from .serializers import UserRegisterSerializer
# Create your views here.

class RegisterUserView(GenericAPIView):
    serializer_class=UserRegisterSerializer
    
    def post(self,request):
        
        serializer=self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            user=serializer.data
            return Response({
                'data':user,
                "message":f'hi{user.first_name} thanks for Signing up'
            },status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)