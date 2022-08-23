from datetime import datetime

import jwt
from django.contrib.auth.models import User
from rest_framework import authentication, exceptions

from django.conf import settings


class JWTAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        access_token = request.headers.get("Authorization") or request.COOKIES.get("access_token")
        if not access_token:
            return None
        return self.authenticate_credentials(access_token)

    def authenticate_credentials(self, token):
        if isinstance(token, bytes):
            token = token.decode("ascii")
        try:
            data = jwt.decode(token, settings.SECRET_KEY, algorithms="HS256")
            user_id = data["user_id"]
            expired_at = data["expired_at"]
            user = User.objects.get(id=user_id)

        except (jwt.DecodeError, jwt.InvalidAlgorithmError, AttributeError):
            raise exceptions.AuthenticationFailed("Invalid Token")
        except User.DoesNotExist:
            raise exceptions.AuthenticationFailed("No such user")

        if expired_at:
            expired_at = datetime.strptime(expired_at, "%Y-%m-%d %H:%M:%S")
            if datetime.now() >= expired_at:
                raise exceptions.AuthenticationFailed("Expired Token")

        return user, None
