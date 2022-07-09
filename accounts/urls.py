from django.urls import include, path

from accounts.api.urls import urlpatterns

from .views import (
    AdminCreateView,
    AdminUserListView,
    LogoutView,
    UserDeleteView,
    UserLoginView,
)

app_name = "accounts"

urlpatterns = [
    path("login/", UserLoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("admin_list/", AdminUserListView.as_view(), name="admin_list"),
    path("admin_create/", AdminCreateView.as_view(), name="admin_create"),
    path("delete/<int:pk>/", UserDeleteView.as_view(), name="delete"),
    path("api/", include(urlpatterns)),
]
