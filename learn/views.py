from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ProductSerializers
from learn.models import Product

# Create your views here
@api_view(['GET','POST','PUT'])
def home(request,*args, **kwargs):
    courses={
        'person':1,
        'name':'surend',
        
    }
    if request.method=='GET':
        
        
        return Response(courses)
    elif request.method=='POST':
        
        return Response(courses)
    return Response(courses)

class ProductView(APIView):
    
    def get(self, request, *args, **kwargs):
        
        products = Product.objects.all()
        
        
        serializer = ProductSerializers(products, many=True)
        
        # Return the serialized data as a response
        return Response(serializer.data)
    
    def post(self,request):
        serializer=ProductSerializers(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            user = serializer.data
            return Response({
                'data':user,
                "message":"Successfully Created"
            },status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def put(self,request,pk,*args, **kwargs):
        try:
            product=Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            return Response({'msg': 'Product not found'},
                            status=status.HTTP_404_NOT_FOUND)
        serializer=ProductSerializers(product,data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            user = serializer.data
            return Response({
                'data':user,
                "message":"Successfully Updated"
            },status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def patch(self,request,*args, **kwargs):
        try:
            product=Product.objects.get(id=request.data['id'])
        except Product.DoesNotExist:
            return Response({'msg': 'Product not found'},
                            status=status.HTTP_404_NOT_FOUND)
        serializer=ProductSerializers(product,data=request.data,partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            user = serializer.data
            return Response({
                'data':user,
                "message":"Successfully Updated"
            },status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,*args, **kwargs):
        product=Product.objects.get(id=request.data['id'])
        serializer=ProductSerializers(product,data=request.data)
        product.delete()
        return Response({"message":"Successfull deleted"},status=status.HTTP_200_OK)
        
