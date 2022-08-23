from django.urls import path
from accounts.views import *
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('regist', user_regist, name="regist"),
    path('login', user_login, name="login"),
    path('test', test, name="test"),
    
    path('login2', TokenObtainPairView.as_view(), name="login2"),
    path('refresh', TokenRefreshView.as_view(), name="refresh"),
]
