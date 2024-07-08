from users.apps import UsersConfig
from django.urls import path
from users.views import UserUpdate, UserList

app_name = UsersConfig.name


urlpatterns = [
    path('', UserList.as_view(),name='users_list'),
    path('update/<int:pk>', UserUpdate.as_view(), name='user_update'),
]

