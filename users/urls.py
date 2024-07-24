from django.urls import path


from users.apps import UsersConfig
from users.views import UserUpdateView, UserDetailView, UserCreateView, UserDeleteView, UserListView


app_name = UsersConfig.name

urlpatterns = [
    path('user/', UserListView.as_view(), name='user_list'),
    path('user/create/', UserCreateView.as_view(), name='user_create'),
    path('user/<int:pk>/', UserDetailView.as_view(), name='user_detail'),
    path('user/<int:pk>/update/', UserUpdateView.as_view(), name='user_update'),
    path('user/<int:pk>/delete/', UserDeleteView.as_view(), name='user_delete'),
]
