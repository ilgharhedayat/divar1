from django.urls import path, include
from wantads.api.urls import urlpatterns
from .views import home

urlpatterns = [
    path('', home),
    path('api/', include(urlpatterns))

]
