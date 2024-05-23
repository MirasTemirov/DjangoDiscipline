from django.urls import path
from . import views


urlpatterns = [
    path('group', views.GroupList.as_view()),
    path('group/<int:group_id>', views.GroupDetail.as_view()),
    path('group/analytics', views.GroupAnalytics.as_view()),
    path('object', views.ObjectList.as_view()),
    path('object/<int:object_id>', views.ObjectDetail.as_view()),
    path('object/analytics', views.ObjectAnalytics.as_view()),
]
