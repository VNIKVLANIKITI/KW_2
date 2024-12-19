from rest_framework import generics
from users.serializers import UsersSerializer

# Create your views here.
class UserCreateAPIView(generics.CreateAPIView):
    serializer_class = UsersSerializer