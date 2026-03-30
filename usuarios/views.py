from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken

@api_view(['POST'])
@permission_classes([AllowAny]) # Permitir que cualquiera intente loguearse
def login_view(request):
    email = request.data.get('email')
    password = request.data.get('password')
    
    # IMPORTANTE: Aunque usemos email, el parámetro de authenticate 
    # se sigue llamando 'username' internamente por Django, 
    # pero le pasamos el valor de la variable 'email'.
    user = authenticate(username=email, password=password)

    if user is not None:
        if not user.is_active:
            return Response({"success": False, "message": "Usuario desactivado"}, status=403)
            
        refresh = RefreshToken.for_user(user)
        
        return Response({
            "success": True,
            "access": str(refresh.access_token),
            "refresh": str(refresh), # Es buena práctica enviar ambos
            "user": {
                "email": user.email,
                "full_name": f"{user.first_name} {user.last_name}".strip() or user.email,
                "rol": user.rol_interno,
                "cuenta_id": user.cuenta.id if user.cuenta else None
            }
        })
        
    return Response({
        "success": False, 
        "message": "Correo o contraseña incorrectos"
    }, status=status.HTTP_401_UNAUTHORIZED)