from django.db import models
from django.contrib.auth.models import User
from utils import models as utils_models
from datetime import datetime


class Group(utils_models.AbstractModel):
    title = models.CharField(max_length=50, unique=True)
    teacher = models.ForeignKey(User, on_delete=models.CASCADE, related_name='teacher_groups')
    mentor_for_boys = models.ForeignKey(User, on_delete=models.CASCADE, related_name='abi_groups')
    mentor_for_girls = models.ForeignKey(User, on_delete=models.CASCADE, related_name='abla_groups')

    def soft_delete(self):
        self.deleted_on = datetime.now()
        self.is_active = False
        self.save()


class Object(utils_models.AbstractModel):
    title = models.CharField(max_length=255, unique=True)
    background = models.CharField(max_length=7)
    text_color = models.CharField(max_length=7)

    def soft_delete(self):
        self.deleted_on = datetime.now()
        self.is_active = False
        self.save()
