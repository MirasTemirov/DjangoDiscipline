from django.urls import path, include
from rest_framework_jwt.views import obtain_jwt_token


urlpatterns = [
    path('api/v1/account/', include('account.urls')),
    path('api/v1/auth/', obtain_jwt_token),
    path('api/v1/handbook/', include('handbook.urls')),
    path('api/v1/booking/', include('booking.urls')),
    path('api/v1/log/', include('log.urls'))
]
