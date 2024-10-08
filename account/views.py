
from .serializer import UserSerializers,UserLoginSerializer
from rest_framework.response import Response
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework import status
from rest_framework import generics, status
from rest_framework.response import Response
from .models import User
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.generics import RetrieveUpdateAPIView


# register the user

class Register(generics.GenericAPIView):
    permission_classes = [AllowAny]
    serializer_class = UserSerializers
    # renderer_classes = (UserRenderer,)
    def post(self, request):
        user = request.data
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        user_data = serializer.data
       
        return Response(user_data, status=status.HTTP_201_CREATED)

# login apis
class Login(generics.GenericAPIView):
    permission_classes = [AllowAny]
    serializer_class = UserLoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    



class userData(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        serializer = UserSerializers(self.request.user,context={'request': request})
        return Response(serializer.data)

# update the user details
class update_profile(RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializers
    def update(self, request, *args, **kwargs):
        serializer = self.serializer_class(request.user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)