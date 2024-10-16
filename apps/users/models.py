from django.contrib.auth.models import AbstractUser
from django.db.models import EmailField, BooleanField

from users.managers import CustomUserManager


class User(AbstractUser):
    username = None
    email = EmailField(unique=True)
    is_active = BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = CustomUserManager()


class Author(Model):
    first_name = CharField(max_length=255)
    last_name = CharField(max_length=255)
    description = CKEditor5Field(null=True, blank=True)

    def __str__(self):
        return f"{self.first_name}{self.last_name}"
