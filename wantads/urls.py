from django.urls import include, path

from wantads.api.urls import urlpatterns

from .views import home

app_name = "want_ad"
urlpatterns = [path("", home), path("api/", include(urlpatterns))]
