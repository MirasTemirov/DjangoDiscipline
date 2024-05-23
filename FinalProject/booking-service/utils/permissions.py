from rest_framework.permissions import BasePermission


def method_permission_classes(classes):
    def decorator(func):
        def decorated_func(self, *args, **kwargs):
            self.permission_classes = classes
            self.check_permissions(self.request)
            return func(self, *args, **kwargs)
        return decorated_func
    return decorator


class PermissionsUserList(BasePermission):
    message = "You don't have enough permissions to do this operation. Please, contact to the administrator. P.S: " \
              "Azamat "

    def has_permission(self, request, view):
        if request.user.is_anonymous:
            return False
        if request.user.profile.role == 'admin':
            return True
        if 'user_list' in request.user.profile.permissions:
            return True
        return False


class PermissionsUserCreate(BasePermission):
    message = "You don't have enough permissions to do this operation. Please, contact to the administrator. P.S: " \
              "Azamat "

    def has_permission(self, request, view):
        if request.user.is_anonymous:
            return False
        if request.user.profile.role == 'admin' :
            return True
        if 'user_create' in request.user.profile.permissions:
            return True
        return False


class PermissionsUserUpdate(BasePermission):
    message = "You don't have enough permissions to do this operation. Please, contact to the administrator. P.S: " \
              "Azamat "

    def has_permission(self, request, view):
        if request.user.is_anonymous:
            return False
        if request.user.profile.role == 'admin':
            return True
        if 'user_update' in request.user.profile.permissions:
            return True
        return False


class PermissionsUserDelete(BasePermission):
    message = "You don't have enough permissions to do this operation. Please, contact to the administrator. P.S: " \
              "Azamat "

    def has_permission(self, request, view):
        if request.user.is_anonymous:
            return False
        if request.user.profile.role == 'admin':
            return True
        if 'user_delete' in request.user.profile.permissions:
            return True
        return False


class PermissionsGroupList(BasePermission):
    message = "You don't have enough permissions to do this operation. Please, contact to the administrator. P.S: " \
              "Azamat "

    def has_permission(self, request, view):
        if request.user.is_anonymous:
            return False
        if request.user.profile.role == 'admin':
            return True
        if 'group_list' in request.user.profile.permissions:
            return True
        return False


class PermissionsGroupCreate(BasePermission):
    message = "You don't have enough permissions to do this operation. Please, contact to the administrator. P.S: " \
              "Azamat "

    def has_permission(self, request, view):
        if request.user.is_anonymous:
            return False
        if request.user.profile.role == 'admin' :
            return True
        if 'group_create' in request.user.profile.permissions:
            return True
        return False


class PermissionsGroupUpdate(BasePermission):
    message = "You don't have enough permissions to do this operation. Please, contact to the administrator. P.S: " \
              "Azamat "

    def has_permission(self, request, view):
        if request.user.is_anonymous:
            return False
        if request.user.profile.role == 'admin':
            return True
        if 'group_update' in request.user.profile.permissions:
            return True
        return False


class PermissionsGroupDelete(BasePermission):
    message = "You don't have enough permissions to do this operation. Please, contact to the administrator. P.S: " \
              "Azamat "

    def has_permission(self, request, view):
        if request.user.is_anonymous:
            return False
        if request.user.profile.role == 'admin':
            return True
        if 'group_delete' in request.user.profile.permissions:
            return True
        return False


class PermissionsObjectList(BasePermission):
    message = "You don't have enough permissions to do this operation. Please, contact to the administrator. P.S: " \
              "Azamat "

    def has_permission(self, request, view):
        if request.user.is_anonymous:
            return False
        if request.user.profile.role == 'admin':
            return True
        if 'object_list' in request.user.profile.permissions:
            return True
        return False


class PermissionsObjectCreate(BasePermission):
    message = "You don't have enough permissions to do this operation. Please, contact to the administrator. P.S: " \
              "Azamat "

    def has_permission(self, request, view):
        if request.user.is_anonymous:
            return False
        if request.user.profile.role == 'admin':
            return True
        if 'object_create' in request.user.profile.permissions:
            return True
        return False


class PermissionsObjectUpdate(BasePermission):
    message = "You don't have enough permissions to do this operation. Please, contact to the administrator. P.S: " \
              "Azamat "

    def has_permission(self, request, view):
        if request.user.is_anonymous:
            return False
        if request.user.profile.role == 'admin':
            return True
        if 'object_update' in request.user.profile.permissions:
            return True
        return False


class PermissionsObjectDelete(BasePermission):
    message = "You don't have enough permissions to do this operation. Please, contact to the administrator. P.S: " \
              "Azamat "

    def has_permission(self, request, view):
        if request.user.is_anonymous:
            return False
        if request.user.profile.role == 'admin':
            return True
        if 'object_delete' in request.user.profile.permissions:
            return True
        return False


class PermissionsBookingList(BasePermission):
    message = "You don't have enough permissions to do this operation. Please, contact to the administrator. P.S: " \
              "Azamat "

    def has_permission(self, request, view):
        if request.user.is_anonymous:
            return False
        if request.user.profile.role == 'admin':
            return True
        if 'booking_list' in request.user.profile.permissions:
            return True
        return False


class PermissionsBookingCreate(BasePermission):
    message = "You don't have enough permissions to do this operation. Please, contact to the administrator. P.S: " \
              "Azamat "

    def has_permission(self, request, view):
        if request.user.is_anonymous:
            return False
        if request.user.profile.role == 'admin':
            return True
        if 'booking_create' in request.user.profile.permissions:
            return True
        return False


class PermissionsBookingUpdate(BasePermission):
    message = "You don't have enough permissions to do this operation. Please, contact to the administrator. P.S: " \
              "Azamat "

    def has_permission(self, request, view):
        if request.user.is_anonymous:
            return False
        if request.user.profile.role == 'admin':
            return True
        if 'booking_update' in request.user.profile.permissions:
            return True
        return False


class PermissionsBookingDelete(BasePermission):
    message = "You don't have enough permissions to do this operation. Please, contact to the administrator. P.S: " \
              "Azamat "

    def has_permission(self, request, view):
        if request.user.is_anonymous:
            return False
        if request.user.profile.role == 'admin':
            return True
        if 'booking_delete' in request.user.profile.permissions:
            return True
        return False


class PermissionsLogList(BasePermission):
    message = "You don't have enough permissions to do this operation. Please, contact to the administrator. P.S: " \
              "Azamat 4E"

    def has_permission(self, request, view):
        if request.user.is_anonymous:
            return False
        if request.user.profile.role == 'admin':
            return True
        if 'log_list' in request.user.profile.permissions:
            return True
        return False


class PermissionsBusinessHourCreate(BasePermission):
    message = "You don't have enough permissions to do this operation. Please, contact to the administrator. P.S: " \
              "Azamat"

    def has_permission(self, request, view):
        if request.user.is_anonymous:
            return False
        if request.user.profile.role == 'admin':
            return True
        if 'bHour_create' in request.user.profile.permissions:
            return True
        return False


class PermissionsAnalyticList(BasePermission):
    message = "You don't have enough permissions to do this operation. Please, contact to the administrator. P.S: " \
              "Azamat"

    def has_permission(self, request, view):
        if request.user.is_anonymous:
            return False
        if request.user.profile.role == 'admin':
            return True
        if 'analytic_list' in request.user.profile.permissions:
            return True
        return False
