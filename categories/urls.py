from django.urls import path, include
from categories.api.urls import urlpatterns

# from .views import  ()
urlpatterns = [
    path('api/', include(urlpatterns))
]
