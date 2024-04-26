from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    """Класс модели истории"""

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(null=True, blank=True)

