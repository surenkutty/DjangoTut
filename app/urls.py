from django.urls import path,include

from .views import *

urlpatterns = [
    path('register/',RegisterUserView.as_view(),name="register" ),
    path('verify-email/',VerifyUserEmail.as_view(),name="verify" ),
    path('login/',LoginUserView.as_view(),name="login" ),
    path('profile/',TestAuthenticatedView.as_view(),name="profile" ),
    path('password-reset/',PasswordResetRequestView.as_view(),name="password-reset" ),
    path('password-reset-confirm/<uidb64>/<token>/',PasswordResetConfirm.as_view(),name="password-reset-confirm" ),
    path('set-new-password/',SetPassword.as_view(),name="setpassword" ),
    path('logout-user/',LoginUserView.as_view(),name="logout-user" ),
    
    
    
]