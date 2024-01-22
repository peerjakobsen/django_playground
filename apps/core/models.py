from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """A custom user model that extends the base django user model."""

    # add additional fields in here

    def __str__(self) -> str:
        """Return a string representation of our custom user."""
        return super().__str__()
