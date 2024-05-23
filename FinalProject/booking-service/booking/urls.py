from django.urls import path
from . import views


urlpatterns = [
    path('', views.BookingList.as_view()),
    path('<int:booking_id>', views.BookingDetail.as_view()),
    path('business-hour', views.BusinessHourList.as_view())
]
