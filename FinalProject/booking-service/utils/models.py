from django.db import models
from django.contrib.auth.models import User


class AbstractModel(models.Model):
    created_by = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    created_on = models.DateTimeField(auto_now_add=True)
    edited_on = models.DateTimeField(auto_now=True)
    deleted_on = models.DateTimeField(null=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        abstract = True
