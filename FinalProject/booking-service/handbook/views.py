from django.http import Http404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from . import models
from . import serializers
from utils import permissions as utils_permissions
from utils import funcs as utils_funcs
from datetime import datetime
from dateutil.rrule import rrule, MONTHLY
import calendar
from django.conf import settings


class GroupList(APIView):
    @utils_permissions.method_permission_classes(
        (utils_permissions.PermissionsGroupList | utils_permissions.PermissionsBookingList,)
    )
    def get(self, request):
        element = models.Group.objects.all()
        serializer = serializers.GroupGetSerializer(element, many=True)
        utils_funcs.logger(
            operation_type='read',
            operation_data='handbook_group',
            user=request.user.id,
            description="Список групп"
        )  # log
        return Response(serializer.data, status=status.HTTP_200_OK)

    @utils_permissions.method_permission_classes((utils_permissions.PermissionsGroupCreate,))
    def post(self, request):
        serializer = serializers.GroupPostSerializer(data=request.data, context={'request': request})
        if serializer.is_valid(raise_exception=True):
            element = serializer.save()
            utils_funcs.logger(
                operation_type='create',
                operation_data='handbook_group',
                user=request.user.id,
                description="Создание новой группы [" + str(element.id) + "]"
            )  # log
        return Response({}, status=status.HTTP_201_CREATED)


class GroupDetail(APIView):
    def get_object(self, group_id):
        try:
            return models.Group.objects.get(id=group_id)
        except models.Group.DoesNotExist:
            raise Http404

    @utils_permissions.method_permission_classes((utils_permissions.PermissionsGroupList,))
    def get(self, request, group_id):
        element = self.get_object(group_id=group_id)
        serializer = serializers.GroupGetSerializer(element)
        utils_funcs.logger(
            operation_type='read_one',
            operation_data='handbook_group',
            user=request.user.id,
            description="Группа [" + str(group_id) + "]"
        )  # log
        return Response(serializer.data, status=status.HTTP_200_OK)

    @utils_permissions.method_permission_classes((utils_permissions.PermissionsGroupUpdate,))
    def put(self, request, group_id):
        element = self.get_object(group_id=group_id)
        serializer = serializers.GroupPutSerializer(element, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            utils_funcs.logger(
                operation_type='update',
                operation_data='handbook_group',
                user=request.user.id,
                description="Редактирование [" + str(group_id) + "]"
            )  # log
        return Response({}, status=status.HTTP_200_OK)

    @utils_permissions.method_permission_classes((utils_permissions.PermissionsGroupDelete,))
    def delete(self, request, group_id):
        element = self.get_object(group_id=group_id)
        element.soft_delete()
        utils_funcs.logger(
            operation_type='delete',
            operation_data='handbook_group',
            user=request.user.id,
            description="Удаление [" + str(group_id) + "]"
        )  # log
        return Response(status=status.HTTP_204_NO_CONTENT)


class GroupAnalytics(APIView):
    @utils_permissions.method_permission_classes((utils_permissions.PermissionsAnalyticList,))
    def get(self, request):
        # init analytics result
        res = {
            'spline': {
                'series': [],
                'max': "1970-01-01 00:00:00",
                'min': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            },
            'pie': {
                'series': [
                    {
                        'colorByPoint': True,
                        'data': []
                    }
                ]
            },
            'column': {
                'series': [],
                'categories': [],
            }
        }

        # fill spline chart && pie chart
        data_tmp_group_month = {}
        for group in models.Group.objects.all().iterator():
            tmp = {
                "name": group.title,
                "data": []
            }
            data_tmp = {}
            if group.id not in data_tmp_group_month:
                data_tmp_group_month[group.id] = {
                    "name": group.title,
                    "month_data": {}
                }
            for booking in group.group_schedules.filter(is_active=True).order_by('start').values('start'):
                start = booking['start'].strftime("%Y-%m-%d %H:%M:%S").split()[0]
                if start[:7] not in data_tmp_group_month[group.id]["month_data"]:
                    data_tmp_group_month[group.id]["month_data"][start[:7]] = 0
                data_tmp_group_month[group.id]["month_data"][start[:7]] += 1
                if start not in data_tmp:
                    data_tmp[start] = 0
                data_tmp[start] += 1
                if start > res['spline']['max']:
                    res['spline']['max'] = start
                if start < res['spline']['min']:
                    res['spline']['min'] = start
            total_amount = 0
            for d, d_amount in data_tmp.items():
                tmp["data"].append(
                    [d, d_amount]
                )
                total_amount += d_amount
            # spline
            res['spline']['series'].append(tmp)

            # pie
            res['pie']['series'][0]['data'].append({
                'name': group.title,
                'y': total_amount,
            })
        # column
        # create categories
        min_date = res['spline']['min'].split()[0][:7]
        min_date = datetime.strptime(min_date + "-01 00:00:00", "%Y-%m-%d %H:%M:%S")

        max_date = res['spline']['max'].split()[0][:7]
        max_date_arr = max_date.split("-")
        max_date_eom = calendar.monthrange(int(max_date_arr[0]), int(max_date_arr[1]))[1]
        max_date = datetime.strptime(max_date + "-" + str(max_date_eom) + " 23:59:59", "%Y-%m-%d %H:%M:%S")

        year_months = []
        for d in rrule(MONTHLY, dtstart=min_date, until=max_date):
            res['column']['categories'].append(
                settings.MONTHS_NAMES_RU[d.month] + " " + str(d.year)
            )
            year_months.append(d.strftime("%Y-%m"))

        for g_id, g_data in data_tmp_group_month.items():
            tmp = {
                "name": g_data["name"],
                "data": []
            }
            for year_month in year_months:
                tmp["data"].append(g_data["month_data"].get(year_month, 0))
            res['column']['series'].append(tmp)
            utils_funcs.logger(
                operation_type='read',
                operation_data='analytic',
                user=request.user.id,
                description="Список аналитика"
            )  # log
        return Response(res, status=status.HTTP_200_OK)


class ObjectList(APIView):
    @utils_permissions.method_permission_classes(
        (utils_permissions.PermissionsObjectList | utils_permissions.PermissionsBookingList,)
    )
    def get(self, request):
        element = models.Object.objects.all()
        serializer = serializers.ObjectGetSerializer(element, many=True)
        utils_funcs.logger(
            operation_type='read',
            operation_data='handbook_object',
            user=request.user.id,
            description="Список обьектов"
        )  # log
        return Response(serializer.data, status=status.HTTP_200_OK)

    @utils_permissions.method_permission_classes((utils_permissions.PermissionsObjectCreate,))
    def post(self, request):
        serializer = serializers.ObjectPostSerializer(data=request.data, context={'request': request})
        if serializer.is_valid(raise_exception=True):
            element = serializer.save()
            utils_funcs.logger(
                operation_type='create',
                operation_data='handbook_object',
                user=request.user.id,
                description="Создание нового обьекта [" + str(element.id) + "]"
            )  # log
        return Response({}, status=status.HTTP_201_CREATED)


class ObjectDetail(APIView):
    def get_object(self, object_id):
        try:
            return models.Object.objects.get(id=object_id)
        except models.Object.DoesNotExist:
            raise Http404

    @utils_permissions.method_permission_classes((utils_permissions.PermissionsObjectList,))
    def get(self, request, object_id):
        element = self.get_object(object_id=object_id)
        serializer = serializers.ObjectGetSerializer(element)
        utils_funcs.logger(
            operation_type='read_one',
            operation_data='handbook_object',
            user=request.user.id,
            description="Обьекты [" + str(object_id) + "]"
        )  # log
        return Response(serializer.data, status=status.HTTP_200_OK)

    @utils_permissions.method_permission_classes((utils_permissions.PermissionsObjectUpdate,))
    def put(self, request, object_id):
        element = self.get_object(object_id=object_id)
        serializer = serializers.ObjectPutSerializer(element, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            utils_funcs.logger(
                operation_type='update',
                operation_data='handbook_object',
                user=request.user.id,
                description="Редактирование [" + str(object_id) + "]"
            )  # log
        return Response({}, status=status.HTTP_200_OK)

    @utils_permissions.method_permission_classes((utils_permissions.PermissionsObjectDelete,))
    def delete(self, request, object_id):
        element = self.get_object(object_id=object_id)
        element.soft_delete()
        utils_funcs.logger(
            operation_type='delete',
            operation_data='handbook_object',
            user=request.user.id,
            description="Удаление [" + str(object_id) + "]"
        )  # log
        return Response(status=status.HTTP_204_NO_CONTENT)


class ObjectAnalytics(APIView):
    @utils_permissions.method_permission_classes((utils_permissions.PermissionsAnalyticList,))
    def get(self, request):
        # init analytics result
        res = {
            'spline': {
                'series': [],
                'max': "1970-01-01 00:00:00",
                'min': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            },
            'pie': {
                'series': [
                    {
                        'colorByPoint': True,
                        'data': []
                    }
                ]
            },
            'column': {
                'series': [],
                'categories': []
            }
        }

        # fill spline chart && pie chart
        data_tmp_object_month = {}
        for object in models.Object.objects.all().iterator():
            tmp = {
                "name": object.title,
                "color": object.background,
                "data": []
            }
            data_tmp = {}
            if object.id not in data_tmp_object_month:
                data_tmp_object_month[object.id] = {
                    "name": object.title,
                    "color": object.background,
                    "month_data": {}
                }
            for booking in object.object_schedules.filter(is_active=True).order_by('start').values('start'):
                start = booking['start'].strftime("%Y-%m-%d %H:%M:%S").split()[0]
                if start[:7] not in data_tmp_object_month[object.id]["month_data"]:
                    data_tmp_object_month[object.id]["month_data"][start[:7]] = 0
                data_tmp_object_month[object.id]["month_data"][start[:7]] += 1
                if start not in data_tmp:
                    data_tmp[start] = 0
                data_tmp[start] += 1
                if start > res['spline']['max']:
                    res['spline']['max'] = start
                if start < res['spline']['min']:
                    res['spline']['min'] = start
            total_amount = 0
            for d, d_amount in data_tmp.items():
                tmp["data"].append(
                    [d, d_amount]
                )
                total_amount += d_amount
            res['spline']['series'].append(tmp)

            res['pie']['series'][0]['data'].append({
                'name': object.title,
                'y': total_amount,
                'color': object.background
            })

        # column
        # create categories
        min_date = res['spline']['min'].split()[0][:7]
        min_date = datetime.strptime(min_date + "-01 00:00:00", "%Y-%m-%d %H:%M:%S")

        max_date = res['spline']['max'].split()[0][:7]
        max_date_arr = max_date.split("-")
        max_date_eom = calendar.monthrange(int(max_date_arr[0]), int(max_date_arr[1]))[1]
        max_date = datetime.strptime(max_date + "-" + str(max_date_eom) + " 23:59:59", "%Y-%m-%d %H:%M:%S")

        year_months = []
        for d in rrule(MONTHLY, dtstart=min_date, until=max_date):
            res['column']['categories'].append(
                settings.MONTHS_NAMES_RU[d.month] + " " + str(d.year)
            )
            year_months.append(d.strftime("%Y-%m"))

        for g_id, g_data in data_tmp_object_month.items():
            tmp = {
                "name": g_data["name"],
                "color": g_data["color"],
                "data": []
            }
            for year_month in year_months:
                tmp["data"].append(g_data["month_data"].get(year_month, 0))
            res['column']['series'].append(tmp)
            utils_funcs.logger(
                operation_type='read',
                operation_data='analytic',
                user=request.user.id,
                description="Список аналитика"
            )  # log
        return Response(res, status=status.HTTP_200_OK)
