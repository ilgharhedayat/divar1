from django.urls import path

from .views import (
    CategoryWantAdApiView,
    HomeApiView,
    ViewedApiView,
    WantAdRetrieveAPIView,
)

app_name = "want_ad"
urlpatterns = [
    path("", HomeApiView.as_view(), name="home"),
    path("<int:pk>/", WantAdRetrieveAPIView.as_view(), name="detail"),
    path("want_cat/<int:id>/", CategoryWantAdApiView.as_view(), name="category"),
    path("recent_seen/", ViewedApiView.as_view(), name="seen"),
]
