from backend.api.models import Character, Group, Run, User
from rest_framework import viewsets
from backend.api.serializers import (
    CharacterSerializer, GroupSerializer, RunSerializer, UserSerializer)


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
    serializer_class = CharacterSerializer

    def get_queryset(self):
        queryset = Character.objects.all()
        user_id = self.request.query_params.get('user_id', None)
        if user_id:
            queryset = queryset.filter(user_id=user_id)
        return queryset


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class RunViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows runs to be viewed or edited.
    """
    queryset = Run.objects.all()
    serializer_class = RunSerializer
