from django.urls import path

from .views import CategoryApiView

app_name = "categories"
urlpatterns = [path("", CategoryApiView.as_view())]
