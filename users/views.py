from rest_framework.views import APIView, status, Request, Response
from .serializers import UserSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAdminUser
from .permissions import IsUserAccountOwner
from django.shortcuts import get_object_or_404
from .models import User


class UserView(APIView):
    def post(self, req: Request) -> Response:
        serializer = UserSerializer(data=req.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)


class UserDetailView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser | IsUserAccountOwner]

    def get(self, request: Request, user_id: int) -> Response:
        found_user = get_object_or_404(User, pk=user_id)
        self.check_object_permissions(request, found_user)
        serializer = UserSerializer(found_user)
        return Response(serializer.data)

    def patch(self, request: Request, user_id: int) -> Response:
        found_user = get_object_or_404(User, pk=user_id)
        self.check_object_permissions(request, found_user)
        serializer = UserSerializer(found_user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
