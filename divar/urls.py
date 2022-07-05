from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("__debug__/", include("debug_toolbar.urls")),
    path("silk/", include("silk.urls", namespace="silk")),
    path("", include("wantads.urls", namespace="want_ad")),
    path("category/", include("categories.urls")),
]
