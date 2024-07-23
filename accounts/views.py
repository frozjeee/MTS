from rest_framework.permissions import AllowAny
from rest_framework.generics import CreateAPIView

from .models import SystemUser
from .serializers import RegisterSerializer


class RegisterAPIView(CreateAPIView):
    """
    Register a new user.

    Please, provide valid email and password.
    Password must be confirmed.
    Verification email is sent upon registration.
    """
    queryset = SystemUser.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = (AllowAny, )

    def perform_create(self, serializer):
        serializer.save()
