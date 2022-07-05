from django.urls import include, path

from categories.api.urls import urlpatterns

# from .views import  ()
urlpatterns = [path("api/", include(urlpatterns))]
