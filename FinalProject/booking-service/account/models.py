from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    ROLE_LIST = (
        ('teacher', 'teacher'),
        ('mentor', 'mentor'),
        ('admin', 'admin')
    )
    GENDER_LIST = (
        ('m', 'm'),
        ('f', 'f')
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    role = models.CharField(max_length=10, choices=ROLE_LIST, default='admin')
    gender = models.CharField(max_length=1, choices=GENDER_LIST, default='m')
    permissions = models.JSONField(default=list)
