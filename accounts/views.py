from django.contrib.auth import authenticate
from rest_framework.decorators import permission_classes, api_view
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from accounts.serializers import *
import jwt 
from django.utils import timezone
from datetime import timedelta 
from django.conf import settings 
from rest_framework import status 
from rest_framework.permissions import IsAuthenticated

# Create your views here.
@api_view(['POST'])
@permission_classes([AllowAny])
def user_regist(request):
    serializer = UserSerializer(data = request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return create_access_token(request.data)
    
    
@api_view(["POST"])
@permission_classes([AllowAny])
def user_login(request):
    return create_access_token(request.data)
    

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def test(request):
    return Response(request.user.username)


def create_access_token(data):
    username = data.get("username")
    password = data.get("password")
    user = authenticate(username=username, password=password)
    if user is not None and user.is_active:
        expired_at = (timezone.now() + timedelta(days=14)).strftime(
            "%Y-%m-%d %H:%M:%S"
        )
        access_token = jwt.encode(
            {"user_id": user.id, "expired_at":expired_at},settings.SECRET_KEY)
        kwargs={}
        # kwargs["secure"] = True # https 배포를 하였을 때만!
        kwargs["httponly"] = True
        response = Response(access_token)
        response.set_cookie(
            "access_token", access_token, max_age=60 * 60 * 24 * 14, **kwargs
        )
        return response
    return Response( "Invalid username or password", status=status.HTTP_400_BAD_REQUEST)
