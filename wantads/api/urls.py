from .views import HomeApiView

from django.urls import path

app_name = 'api'
urlpatterns = [
    path('', HomeApiView.as_view(), name='home'),
]
