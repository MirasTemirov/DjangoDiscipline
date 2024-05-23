from django.urls import path
from . import views


urlpatterns = [
    path('', views.Log.as_view())
]
