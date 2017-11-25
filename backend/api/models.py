from django.db import models
from django.contrib.auth.models import AbstractUser as DjangoUser


class User(DjangoUser):
    LANGUAGES = (
        ('de', 'de_DE'),
        ('en', 'en_GB'),
    )
    lang = models.CharField(max_length=5, choices=LANGUAGES, default='de')


class Character(models.Model):
    RACES = (
        ('human', 'Human'),
        ('ork', 'Ork'),
        ('troll', 'Troll'),
        ('elf', 'Elf'),
        ('dwarf', 'Dwarf'),
    )

    # Game related attributes
    user = models.ForeignKey(
        'User',
        on_delete=models.CASCADE,
    )
    group = models.ForeignKey(
        'Group',
        on_delete=models.CASCADE,
        null=True,
    )

    # Gameplay related attributes
    name = models.CharField(max_length=50)
    streetname = models.CharField(max_length=50)
    metatype = models.CharField(max_length=20, choices=RACES)
    ethnos = models.CharField(max_length=50)

    def __str__(self):
        return '{} ({})'.format(self.name, self.user)


class Group(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return '{}'.format(self.name)
