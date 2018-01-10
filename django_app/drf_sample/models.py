from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
from rest_framework.authtoken.models import Token


class Member(AbstractUser):

    email = models.EmailField(
        blank=True,
    )

    def get_user_token(self, user_pk):
        return Token.objects.get_or_create(user_id=user_pk)