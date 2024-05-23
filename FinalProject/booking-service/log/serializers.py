from rest_framework import serializers
from account import serializers as account_serializers
from . import models


class LogGetSerializer(serializers.ModelSerializer):
    user = account_serializers.CreatedByInfoSerializer()
    created_on = serializers.DateTimeField(format='%d.%m.%Y %H:%M', allow_null=True)

    class Meta:
        model = models.Log
        fields = ('id', 'user', 'type', 'data', 'created_on', 'description')


class LogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Log
        fields = ('user', 'type', 'data', 'description')
