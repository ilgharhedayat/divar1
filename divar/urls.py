from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('__debug__/', include('debug_toolbar.urls')),
    path('silk/', include('silk.urls', namespace='silk')),
    path('', include('wantads.urls')),
    path('category/', include('categories.urls')),
]
