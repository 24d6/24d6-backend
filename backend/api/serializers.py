from backend.api.models import Character, Group, Run, User
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'url', 'username', 'email', 'lang', 'character_set')


class CharacterSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Character
        fields = ('id', 'url', 'name', 'streetname', 'metatype', 'ethnos', 'user', 'group')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('id', 'url', 'name', 'character_set')


class RunSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Run
        fields = ('id', 'name', 'gamemaster', 'group')
