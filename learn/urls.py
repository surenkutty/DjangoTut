from django.urls import path,include
from .views import home
from .views import ProductView,ProducetViewset
from rest_framework.routers import DefaultRouter



# Create a router and register our ViewSets with it.
router = DefaultRouter()
router.register(r'pro',ProducetViewset, basename='pro')

urlpatterns=[
    path('',include(router.urls)),
    path('demo/',home),
     path('products/<int:pk>/', ProductView.as_view()),
    path('product',ProductView.as_view(),name='product'),
   
]