from rest_framework import serializers
from . import models
from account import serializers as account_serializers


class GroupGetSerializer(serializers.ModelSerializer):
    created_by = account_serializers.CreatedByInfoSerializer()
    teacher = account_serializers.AccountInfoSerializer()
    mentor_for_boys = account_serializers.AccountInfoSerializer()
    mentor_for_girls = account_serializers.AccountInfoSerializer()
    created_on = serializers.DateTimeField(format='%d.%m.%Y %H:%M', allow_null=True)
    edited_on = serializers.DateTimeField(format='%d.%m.%Y %H:%M', allow_null=True)
    deleted_on = serializers.DateTimeField(format='%d.%m.%Y %H:%M', allow_null=True)

    class Meta:
        model = models.Group
        fields = (
            'id', 'title', 'teacher', 'mentor_for_boys', 'mentor_for_girls',
            'created_by', 'created_on', 'edited_on', 'deleted_on', 'is_active'
        )


class GroupPostSerializer(serializers.ModelSerializer):
    created_by = serializers.HiddenField(default=serializers.CurrentUserDefault())

    def validate_teacher(self, value):
        """
        Check teacher
        """
        if value.profile.role != 'teacher':
            raise serializers.ValidationError("Выберите учителя")
        return value

    def validate_mentor_for_boys(self, value):
        """
        Check abi
        """
        if value.profile.role != 'mentor':
            raise serializers.ValidationError("Выберите воспитателя")
        if value.profile.gender != 'm':
            raise serializers.ValidationError("Воспитателем не может быть женщиной")
        return value

    def validate_mentor_for_girls(self, value):
        """
        Check abla
        """
        if value.profile.role != 'mentor':
            raise serializers.ValidationError("Выберите воспитателя")
        if value.profile.gender != 'f':
            raise serializers.ValidationError("Воспитателем не может быть мужчина")
        return value

    class Meta:
        model = models.Group
        fields = ('title', 'teacher', 'mentor_for_boys', 'mentor_for_girls', 'created_by')


class GroupPutSerializer(serializers.ModelSerializer):

    def validate_teacher(self, value):
        """
        Check teacher
        """
        if value.profile.role != 'teacher':
            raise serializers.ValidationError("Выберите учителя")
        return value

    def validate_mentor_for_boys(self, value):
        """
        Check abi
        """
        if value.profile.role != 'mentor':
            raise serializers.ValidationError("Выберите воспитателя")
        if value.profile.gender != 'm':
            raise serializers.ValidationError("Воспитателем не может быть женщиной")
        return value

    def validate_mentor_for_girls(self, value):
        """
        Check abla
        """
        if value.profile.role != 'mentor':
            raise serializers.ValidationError("Выберите воспитателя")
        if value.profile.gender != 'f':
            raise serializers.ValidationError("Воспитателем не может быть мужчиной")
        return value

    class Meta:
        model = models.Group
        fields = ('title', 'teacher', 'mentor_for_boys', 'mentor_for_girls', 'is_active', 'deleted_on')


class ObjectGetSerializer(serializers.ModelSerializer):
    created_by = account_serializers.CreatedByInfoSerializer()
    created_on = serializers.DateTimeField(format='%d.%m.%Y %H:%M', allow_null=True)
    edited_on = serializers.DateTimeField(format='%d.%m.%Y %H:%M', allow_null=True)
    deleted_on = serializers.DateTimeField(format='%d.%m.%Y %H:%M', allow_null=True)

    class Meta:
        model = models.Object
        fields = ('id', 'title', 'background', 'text_color', 'created_by', 'created_on', 'edited_on', 'deleted_on', 'is_active')


class ObjectPostSerializer(serializers.ModelSerializer):
    created_by = serializers.HiddenField(default=serializers.CurrentUserDefault())

    def validate_background(self, value):
        """
        Check background color
        """
        dict = "0123456789abcdefABCDEF"
        is_ok = True
        for ch in value[1:]:
            if ch not in dict:
                is_ok = False
                break
        print(value.startswith("#"), is_ok)
        if value.startswith("#") is False or is_ok is False:
            raise serializers.ValidationError("Неправильный цвет")
        return value

    def validate_text_color(self, value):
        """
        Check text_color color
        """
        dict = "0123456789abcdefABCDEF"
        is_ok = True
        for ch in value[1:]:
            if ch not in dict:
                is_ok = False
                break
        print(value.startswith("#"), is_ok)
        if value.startswith("#") is False or is_ok is False:
            raise serializers.ValidationError("Неправильный цвет")
        return value

    class Meta:
        model = models.Object
        fields = ('title', 'background', 'text_color', 'created_by')


class ObjectPutSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Object
        fields = ('title', 'background', 'text_color', 'is_active', 'deleted_on')


class GroupInfoSerializer(serializers.ModelSerializer):
    teacher = serializers.SerializerMethodField()
    mentor_for_boys = serializers.SerializerMethodField()
    mentor_for_girls = serializers.SerializerMethodField()

    def get_teacher(self, obj):
        return obj.teacher.get_full_name()

    def get_mentor_for_boys(self, obj):
        return obj.mentor_for_boys.get_full_name()

    def get_mentor_for_girls(self, obj):
        return obj.mentor_for_girls.get_full_name()

    class Meta:
        model = models.Group
        fields = ('id', 'title', 'teacher', 'mentor_for_boys', 'mentor_for_girls')


class ObjectInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Object
        fields = ('id', 'title', 'text_color', 'background')
