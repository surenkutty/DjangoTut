from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
# from .models import Product
import json
from django.forms.models import model_to_dict
# Create your views here.

# def home(request,*args,**kwargs):
#     model_data=Product.objects.all().order_by('?').first()
#     data={}
#     if model_data:
#         data=model_to_dict(model_data,fields=['id','title','content','price'])
#         json_data_str=json.dumps(data)
#         print(data)
#     return  HttpResponse(json_data_str,headers={"content-type":"application/json"})
def home(request):
    return render(request,"templates/index.html")