from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from . import serializers
from . import models
from utils import permissions as utils_permissions
from django.core.paginator import Paginator
from utils import funcs as utils_funcs


class Log(APIView):
    @utils_permissions.method_permission_classes((utils_permissions.PermissionsLogList,))
    def get(self, request):
        filter_type = request.GET.get('type', None)
        filter_from = request.GET.get('from', None)
        filter_to = request.GET.get('to', None)
        filter_data = request.GET.get('data', None)
        filter_user = request.GET.get('user', None)

        elements = models.Log.objects.all()
        if filter_type:
            elements = elements.filter(type=filter_type)
        if filter_from:
            elements = elements.filter(created_on__gte=filter_from + ' 00:00:00')
        if filter_to:
            elements = elements.filter(created_on__lte=filter_to + ' 23:59:59')
        if filter_data:
            elements = elements.filter(data=filter_data)
        if filter_user:
            elements = elements.filter(user=filter_user)

        paginator = Paginator(elements, 10)

        page = request.GET.get('page', '1')
        page = int(page) if page.isnumeric() else 1
        if page > paginator.num_pages:
            page = 1

        page_data = paginator.page(page)

        serializer = serializers.LogGetSerializer(page_data.object_list, many=True)

        """
        utils_funcs.logger(
            operation_type='read',
            operation_data='log',
            user=request.user.id,
            description="Список лога"
        )  # log
        """
        return Response({
            'data': serializer.data,
            'pagination': {
                'num_pages': paginator.num_pages,
                'num_elements': paginator.count
            }
        }, status=status.HTTP_200_OK)
