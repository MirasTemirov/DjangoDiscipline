from django.http import Http404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from . import serializers
from django.contrib.auth.models import User
from utils import funcs as utils_funcs
from utils import permissions as utils_permissions


class AccountList(APIView):
    @utils_permissions.method_permission_classes(
        (utils_permissions.PermissionsUserList | utils_permissions.PermissionsLogList, )
    )
    def get(self, request):
        filter_type = request.GET.get('type', None)
        filter_booking = request.GET.get('booking', None)

        elements = User.objects.filter(profile__role__in=['teacher', 'mentor'])
        if filter_type == 'teacher':
            elements = elements.filter(profile__role='teacher', is_active=True)
        if filter_type == 'abi':
            elements = elements.filter(profile__role='mentor', profile__gender='m', is_active=True)
        if filter_type == 'abla':
            elements = elements.filter(profile__role='mentor', profile__gender='f', is_active=True)
        if filter_booking:
            elements = elements.filter(profile__permissions__contains=['booking_create'])
            """created_by_ids = []
            for el in User.objects.filter(
                is_active=True
            ).values(
                'id', 'profile__permissions', 'profile__role'
            ).iterator():
                if el['profile__role'] == 'admin':
                    created_by_ids.append(el['id'])
                else:
                    if el['profile__permissions']:
                        if 'booking_create' in el['profile__permissions']:
                            created_by_ids.append(el['id'])
            elements = User.objects.filter(id__in=created_by_ids)"""

        serializer = serializers.AccountGetSerializer(elements, many=True)
        utils_funcs.logger(
            operation_type='read',
            operation_data='account',
            user=request.user.id,
            description="Список аккаунтов"
        )  # log
        return Response(serializer.data, status=status.HTTP_200_OK)

    @utils_permissions.method_permission_classes((utils_permissions.PermissionsUserCreate,))
    def post(self, request):
        serializer = serializers.AccountPostSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            generated_password = utils_funcs.generate_password()
            user.set_password(generated_password)
            user.save()
            utils_funcs.logger(
                operation_type='create',
                operation_data='account',
                user=request.user.id,
                description="Создание нового аккаунта [" + str(user.id) + "]"
            )  # log
            return Response({'password': generated_password}, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class AccountDetail(APIView):
    def get_object(self, user_id):
        try:
            return User.objects.get(id=user_id, profile__role__in=['teacher', 'mentor'])
        except User.DoesNotExist:
            raise Http404

    @utils_permissions.method_permission_classes((utils_permissions.PermissionsUserList,))
    def get(self, request, user_id):
        element = self.get_object(user_id=user_id)
        serializer = serializers.AccountGetSerializer(element)
        utils_funcs.logger(
            operation_type='read_one',
            operation_data='account',
            user=request.user.id,
            description="Аккаунт [" + str(user_id) + "]"
        )  # log
        return Response(serializer.data, status=status.HTTP_200_OK)

    @utils_permissions.method_permission_classes((utils_permissions.PermissionsUserUpdate,))
    def put(self, request, user_id):
        element = self.get_object(user_id=user_id)
        serializer = serializers.AccountPostSerializer(element, partial=True, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            utils_funcs.logger(
                operation_type='update',
                operation_data='account',
                user=request.user.id,
                description="Редактирование [" + str(user_id) + "]"
            )  # log
        return Response({}, status=status.HTTP_200_OK)

    @utils_permissions.method_permission_classes((utils_permissions.PermissionsUserDelete,))
    def delete(self, request, user_id):
        element = self.get_object(user_id=user_id)
        element.is_active = False
        element.save()
        utils_funcs.logger(
            operation_type='delete',
            operation_data='account',
            user=request.user.id,
            description="Удаление [" + str(user_id) + "]"
        )  # log
        return Response(status=status.HTTP_204_NO_CONTENT)


class AccountResetPassword(APIView):
    def get_object(self, user_id):
        try:
            return User.objects.get(id=user_id, profile__role__in=['teacher', 'mentor'])
        except User.DoesNotExist:
            raise Http404

    @utils_permissions.method_permission_classes((utils_permissions.PermissionsUserUpdate,))
    def post(self, request, user_id):
        user = self.get_object(user_id=user_id)

        generated_password = utils_funcs.generate_password()
        user.set_password(generated_password)
        user.save()
        utils_funcs.logger(
            operation_type='reset_password',
            operation_data='account',
            user=request.user.id,
            description="Сброс пароля [" + str(user_id) + "]"
        )  # log

        return Response({'password': generated_password}, status=status.HTTP_200_OK)


class AccountProfileInfo(APIView):
    def get(self, request):
        serializer = serializers.AccountProfileSerializer(instance=request.user)
        utils_funcs.logger(
            operation_type='read_one',
            operation_data='account',
            user=request.user.id,
            description="Аккаунт [" + str(request.user.id) + "]"
        )  # log
        return Response(serializer.data, status=status.HTTP_200_OK)


class AccountProfile(APIView):
    def put(self, request):
        serializer = serializers.AccountProfileSerializer(request.user, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()

            utils_funcs.logger(
                operation_type='update',
                operation_data='account',
                user=request.user.id,
                description="Редактирование профиля"
            )  # log
        return Response({}, status=status.HTTP_200_OK)


class AccountPassword(APIView):
    def put(self, request):
        serializer = serializers.AccountPasswordSerializer(request.user, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()

            utils_funcs.logger(
                operation_type='update',
                operation_data='account',
                user=request.user.id,
                description="Редактирование пароля"
            )  # log
        return Response({}, status=status.HTTP_200_OK)
