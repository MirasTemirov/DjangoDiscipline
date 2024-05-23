from django.urls import path
from . import views


urlpatterns = [
   path('', views.AccountList.as_view()),
   path('<int:user_id>', views.AccountDetail.as_view()),
   path('<int:user_id>/reset-password', views.AccountResetPassword.as_view()),
   path('me', views.AccountProfileInfo.as_view()),
   path('profile', views.AccountProfile.as_view()),
   path('password', views.AccountPassword.as_view()),
]
