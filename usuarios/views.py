from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken

@api_view(['POST'])
def login_view(request):
    email = request.data.get('email')
    password = request.data.get('password')
    user = authenticate(username=email, password=password)

    if user is not None:
        refresh = RefreshToken.for_user(user)
        return Response({
            "success": True,
            "access": str(refresh.access_token),
            "user": {
                "email": user.email,
                "full_name": user.get_full_name() or user.username # <--- Enviamos el nombre
            }
        })
    return Response({"success": False, "message": "Credenciales incorrectas"}, status=401)