from django.urls import path
from .views import home
from .views import ProductView

urlpatterns=[
    path('demo/',home),
     path('products/<int:pk>/', ProductView.as_view()),
    path('',ProductView.as_view(),name='product'),
   
]