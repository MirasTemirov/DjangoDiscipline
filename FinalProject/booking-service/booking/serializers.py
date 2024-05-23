from rest_framework import serializers
from . import models
from account import serializers as account_serializers
from handbook import serializers as handbook_serializers


class BookingGetSerializer(serializers.ModelSerializer):
    created_by = account_serializers.CreatedByInfoSerializer()
    created_on = serializers.DateTimeField(format='%d.%m.%Y %H:%M', allow_null=True)
    edited_on = serializers.DateTimeField(format='%d.%m.%Y %H:%M', allow_null=True)
    deleted_on = serializers.DateTimeField(format='%d.%m.%Y %H:%M', allow_null=True)
    group = handbook_serializers.GroupInfoSerializer()
    object = handbook_serializers.ObjectInfoSerializer()

    class Meta:
        model = models.Schedule
        fields = (
            'id', 'object', 'group', 'start', 'end',
            'created_by', 'created_on', 'edited_on', 'deleted_on', 'is_active', 'comment'
        )


class BookingPostSerializer(serializers.ModelSerializer):
    created_by = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = models.Schedule
        fields = ('group', 'object', 'start', 'end', 'created_by', 'comment')


class BookingPutSerializer(serializers.ModelSerializer):
    group_info = serializers.SerializerMethodField(read_only=True)
    object_info = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = models.Schedule
        fields = ('group', 'object', 'start', 'end', 'is_active', 'deleted_on', 'object_info', 'group_info', 'comment')

    def get_group_info(self, el):
        return {
            'id': el.group.id,
            'title': el.group.title
        }

    def get_object_info(self, el):
        return {
            'id': el.object.id,
            'title': el.object.title
        }


class BusinessHourGetSerializer(serializers.ModelSerializer):
    start = serializers.SerializerMethodField()
    end = serializers.SerializerMethodField()

    def get_start(self, obj):
        arr = []
        if obj.mon:
            arr.append(obj.mon_start)
        if obj.tue:
            arr.append(obj.tue_start)
        if obj.wen:
            arr.append(obj.wen_start)
        if obj.thu:
            arr.append(obj.thu_start)
        if obj.fri:
            arr.append(obj.fri_start)
        if obj.sun:
            arr.append(obj.sun_start)
        if obj.sat:
            arr.append(obj.sat_start)
        arr = sorted(arr)
        return arr[0] + ":00"

    def get_end(self, obj):
        arr = []
        if obj.mon:
            arr.append(obj.mon_end)
        if obj.tue:
            arr.append(obj.tue_end)
        if obj.wen:
            arr.append(obj.wen_end)
        if obj.thu:
            arr.append(obj.thu_end)
        if obj.fri:
            arr.append(obj.fri_end)
        if obj.sun:
            arr.append(obj.sun_end)
        if obj.sat:
            arr.append(obj.sat_end)
        arr = sorted(arr, reverse=True)
        return arr[0] + ":00"

    class Meta:
        model = models.BusinessHour
        fields = (
            'mon', 'mon_start', 'mon_end',
            'tue', 'tue_start', 'tue_end',
            'wen', 'wen_start', 'wen_end',
            'thu', 'thu_start', 'thu_end',
            'fri', 'fri_start', 'fri_end',
            'sun', 'sun_start', 'sun_end',
            'sat', 'sat_start', 'sat_end',
            'start', 'end'
        )


class BusinessHourPostSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.BusinessHour
        fields = (
            'mon', 'mon_start', 'mon_end',
            'tue', 'tue_start', 'tue_end',
            'wen', 'wen_start', 'wen_end',
            'thu', 'thu_start', 'thu_end',
            'fri', 'fri_start', 'fri_end',
            'sun', 'sun_start', 'sun_end',
            'sat', 'sat_start', 'sat_end'
        )
