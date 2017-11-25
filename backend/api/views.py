from backend.api.models import User, Character
from rest_framework import viewsets
from backend.api.serializers import UserSerializer, CharacterSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class CharacterViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows characters to be viewed or edited.
    """
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer
