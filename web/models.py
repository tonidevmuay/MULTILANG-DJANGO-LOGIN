from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    LANGUAGE_CHOICES = [
        ('en', 'English'),
        ('es', 'Español'),
        ('fr', 'Français')
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    language = models.CharField(max_length=2, choices=LANGUAGE_CHOICES, null=True, blank=True)