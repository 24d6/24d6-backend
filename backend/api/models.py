from django.db import models
from django.contrib.auth.models import User as DjangoUser


class User(DjangoUser):
    lang = models.CharField(max_length=5)
