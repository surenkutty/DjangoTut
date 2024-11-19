from django.urls import path
from .views import RegisterUserView, TestAuthenticatedView,VerifyUserEmail,LoginUserView

urlpatterns = [
    path('register/',RegisterUserView.as_view(),name="register" ),
    path('verify-email/',VerifyUserEmail.as_view(),name="verify" ),
    path('login/',LoginUserView.as_view(),name="login" ),
    path('profile/',TestAuthenticatedView.as_view(),name="profile" ),
    
]