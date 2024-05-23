from django.db import models
from django.contrib.auth.models import User


class Log(models.Model):
    TYPE = (
        ('read', 'read'),
        ('create', 'create'),
        ('update', 'update'),
        ('delete', 'delete'),
        ('login', 'login'),
        ('read_one', 'read_one'),
        ('reset_password', 'reset_password')
    )
    DATA = (
        ('account', 'account'),
        ('booking', 'booking'),
        ('handbook_group', 'handbook_group'),
        ('handbook_object', 'handbook_object'),
        ('log', 'log'),
        ('booking_business_hour', 'booking_business_hour'),
        ('analytic', 'analytic')
    )
    created_on = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='logs')
    type = models.CharField(max_length=30, choices=TYPE)
    data = models.CharField(max_length=30, choices=DATA)
    description = models.TextField(null=True)

    class Meta:
        ordering = ('-created_on', )
