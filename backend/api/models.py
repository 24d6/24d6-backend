from django.db import models
from django.contrib.auth.models import AbstractUser as DjangoUser


class User(DjangoUser):
    LANGUAGES = (
        ('de', 'de_DE'),
        ('en', 'en_GB'),
    )
    lang = models.CharField(max_length=5, choices=LANGUAGES, default='de')
