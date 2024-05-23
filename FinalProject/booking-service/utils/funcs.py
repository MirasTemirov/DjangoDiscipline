from account import serializers as account_serializers
import string
import random
from log import serializers as log_serializers
from datetime import datetime


def jwt_response_payload_handler(token, user=None, request=None):
    """
    add user data to jwt token
    """
    if user and request:
        logger(
            operation_type='login',
            operation_data='account',
            user=user.id,
            description="success auth of user with id '" + str(user.id) + "'"
        )  # log
        user.last_login = datetime.now()
        user.save()

    return {
        'token': token,
        'user': account_serializers.AccountGetSerializer(user).data
    }


def generate_password(length=8):
    dict = string.ascii_lowercase + string.ascii_uppercase + string.digits
    password = ""
    for _ in range(length):
        ind = random.randint(0, len(dict) - 1)
        password += dict[ind]
    return password


def logger(operation_type, operation_data, user, description=None):
    serializer = log_serializers.LogPostSerializer(
        data={
            "type": operation_type,
            "data": operation_data,
            "user": user,
            "description": description
        }
    )
    if serializer.is_valid():
        serializer.save()
