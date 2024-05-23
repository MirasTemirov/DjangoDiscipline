import string

from rest_framework import serializers
from django.contrib.auth.models import User


class AccountGetSerializer(serializers.ModelSerializer):
    permissions = serializers.SerializerMethodField()
    gender = serializers.CharField(source='profile.gender')
    role = serializers.CharField(source='profile.role')
    last_login = serializers.DateTimeField(format='%d.%m.%Y %H:%M', allow_null=True)

    def get_permissions(self, obj):
        r = obj.profile.permissions if obj.profile.permissions else []
        r = sorted(r)
        return r

    class Meta:
        model = User
        fields = (
            'id', 'first_name', 'last_name', 'email', 'username',
            'permissions', 'gender', 'role', 'is_active', 'last_login'
        )


class AccountPostSerializer(serializers.ModelSerializer):
    permissions = serializers.JSONField(default=list)
    role = serializers.CharField(max_length=10)
    gender = serializers.CharField(max_length=1)

    def validate_email(self, value):
        if User.objects.filter(username=value).count() > 0:
            raise serializers.ValidationError("Пользователь с таким 'email' уже существует")
        return value

    def validate_role(self, value):
        if value not in ['teacher', 'mentor']:
            raise serializers.ValidationError("Роль должна быть 'Учитель' или 'Воспитатель'")
        return value

    def validate_gender(self, value):
        if value not in ['m', 'f']:
            raise serializers.ValidationError("Пол должен быть 'Мужской' or 'Женский'")
        return value

    def create(self, validated_data):
        user = User()
        user.username = validated_data['email']
        user.email = validated_data['email']
        user.first_name = validated_data['first_name']
        user.last_name = validated_data['last_name']
        user.is_active = True
        user.save()

        user.profile.permissions = validated_data['permissions']
        user.profile.role = validated_data['role']
        user.profile.gender = validated_data['gender']
        user.profile.save()

        return user

    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.is_active = validated_data.get('is_active', instance.is_active)
        instance.save()

        instance.profile.permissions = validated_data.get('permissions', instance.profile.permissions)
        instance.profile.role = validated_data.get('role', instance.profile.role)
        instance.profile.gender = validated_data.get('gender', instance.profile.gender)
        instance.profile.save()

        return instance

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'permissions', 'role', 'gender', 'is_active')
        extra_kwargs = {
            'first_name': {'write_only': True, 'required': True},
            'last_name': {'write_only': True, 'required': True},
            'email': {'write_only': True, 'required': True},
            'is_active': {'write_only': True, 'required': False},
            'permissions': {'write_only': True, 'required': True},
            'role': {'write_only': True, 'required': True},
            'gender': {'write_only': True, 'required': True}
        }


class CreatedByInfoSerializer(serializers.ModelSerializer):
    email = serializers.SerializerMethodField()

    def get_email(self, obj):
        return obj.email if obj.email else obj.username

    class Meta:
        model = User
        fields = (
            'first_name', 'last_name', 'email'
        )


class AccountInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            'id', 'first_name', 'last_name'
        )


class AccountProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            'first_name', 'last_name', 'email'
        )


class AccountPasswordSerializer(serializers.ModelSerializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)
    new_password_confirmation = serializers.CharField(required=True)

    def validate_old_password(self, value):
        if self.instance.check_password(value) is False:
            raise serializers.ValidationError("Неправильный пароль")
        return value

    def validate_new_password(self, value):
        for ch in value:
            if ch in string.digits or ch in string.ascii_letters:
                pass
            else:
                raise serializers.ValidationError(
                    "Неправильный пароль, пароль должен содержать только английские буквы и числа"
                )
        if len(value) < 6 or len(value) > 16:
            raise serializers.ValidationError(
                "Неправильный пароль, длина пароль должен быть между 6 и 16"
            )
        return value

    def validate_new_password_confirmation(self, value):
        for ch in value:
            if ch in string.digits or ch in string.ascii_letters:
                pass
            else:
                raise serializers.ValidationError(
                    "Неправильный пароль, пароль должен содержать только английские буквы и числа"
                )
        if len(value) < 6 or len(value) > 16:
            raise serializers.ValidationError(
                "Неправильный пароль, длина пароль должен быть между 6 и 16"
            )
        if value != self.initial_data['new_password']:
            raise serializers.ValidationError(
                "Не совпадает с новым паролем"
            )
        return value

    def update(self, instance, validated_data):
        instance.set_password(validated_data.get('new_password'))
        instance.save()

        return instance

    class Meta:
        model = User
        fields = (
            'old_password', 'new_password', 'new_password_confirmation'
        )
