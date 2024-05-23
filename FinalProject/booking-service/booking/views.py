from django.http import Http404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from . import models
from . import serializers
from utils import permissions as utils_permissions
from utils import funcs as utils_funcs


class BookingList(APIView):
    @utils_permissions.method_permission_classes((utils_permissions.PermissionsBookingList,))
    def get(self, request):
        filter_group = request.GET.get('group', None)
        filter_object = request.GET.get('object', None)
        filter_created_by = request.GET.get('created_by', None)

        elements = models.Schedule.objects.all()
        if filter_group:
            elements = elements.filter(group__id=filter_group)
        if filter_object:
            elements = elements.filter(object__id=filter_object)
        if filter_created_by:
            elements = elements.filter(created_by__id=filter_created_by)

        serializer = serializers.BookingGetSerializer(elements, many=True)
        utils_funcs.logger(
            operation_type='read',
            operation_data='booking',
            user=request.user.id,
            description="Список бронирование"
        )  # log
        return Response(serializer.data, status=status.HTTP_200_OK)

    @utils_permissions.method_permission_classes((utils_permissions.PermissionsBookingCreate,))
    def post(self, request):
        serializer = serializers.BookingPostSerializer(data=request.data, context={'request': request})
        if serializer.is_valid(raise_exception=True):
            element = serializer.save()
            utils_funcs.logger(
                operation_type='create',
                operation_data='booking',
                user=request.user.id,
                description="Создание нового бронирование [" + str(element.id) + "]"
            )  # log
            return Response({}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BookingDetail(APIView):
    def get_object(self, booking_id):
        try:
            return models.Schedule.objects.get(id=booking_id)
        except models.Schedule.DoesNotExist:
            raise Http404

    @utils_permissions.method_permission_classes((utils_permissions.PermissionsBookingList,))
    def get(self, request, booking_id):
        element = self.get_object(booking_id=booking_id)
        serializer = serializers.BookingGetSerializer(element)
        utils_funcs.logger(
            operation_type='read_one',
            operation_data='booking',
            user=request.user.id,
            description="Бронирования [" + str(booking_id) + "]"
        )  # log
        return Response(serializer.data, status=status.HTTP_200_OK)

    @utils_permissions.method_permission_classes((utils_permissions.PermissionsBookingUpdate,))
    def put(self, request, booking_id):
        element = self.get_object(booking_id=booking_id)
        serializer = serializers.BookingPutSerializer(element, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            utils_funcs.logger(
                operation_type='update',
                operation_data='booking',
                user=request.user.id,
                description="Редактирование [" + str(booking_id) + "]"
            )  # log
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @utils_permissions.method_permission_classes((utils_permissions.PermissionsBookingDelete,))
    def delete(self, request, booking_id):
        element = self.get_object(booking_id=booking_id)
        element.soft_delete()
        utils_funcs.logger(
            operation_type='delete',
            operation_data='booking',
            user=request.user.id,
            description="Удаление [" + str(booking_id) + "]"
        )  # log
        return Response(status=status.HTTP_204_NO_CONTENT)


class BusinessHourList(APIView):
    def get(self, request):
        element = models.BusinessHour.objects.all().first()
        if element:
            serializer = serializers.BusinessHourGetSerializer(element)
            utils_funcs.logger(
                operation_type='read',
                operation_data='booking_business_hour',
                user=request.user.id,
                description="Список рабочих часов"
            )  # log
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(
            {
                "mon": False,
                "mon_start": "00:00",
                "mon_end": "23:59",
                "tue": False,
                "tue_start": "00:00",
                "tue_end": "23:59",
                "wen": False,
                "wen_start": "00:00",
                "wen_end": "23:59",
                "thu": False,
                "thu_start": "00:00",
                "thu_end": "23:59",
                "fri": False,
                "fri_start": "00:00",
                "fri_end": "23:59",
                "sun": False,
                "sun_start": "00:00",
                "sun_end": "23:59",
                "sat": False,
                "sat_start": "00:00",
                "sat_end": "23:59",
                "start": "00:00:00",
                "end": "23:59:00"
            },
            status=status.HTTP_200_OK
        )

    @utils_permissions.method_permission_classes((utils_permissions.PermissionsBusinessHourCreate,))
    def post(self, request):
        bh = models.BusinessHour.objects.all()
        serializer = serializers.BusinessHourPostSerializer(data=request.data)  # create
        if bh.count() == 1:
            serializer = serializers.BusinessHourPostSerializer(bh.first(), data=request.data, partial=True)  # update
        if serializer.is_valid(raise_exception=True):
            element = serializer.save()
            utils_funcs.logger(
                operation_type='update',
                operation_data='booking_business_hour',
                user=request.user.id,
                description="Редактирование  [" + str(element.id) + "]"
            )  # log
        return Response({}, status=status.HTTP_200_OK)
