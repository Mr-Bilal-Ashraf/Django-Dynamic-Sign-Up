from django.conf.urls.static import static
from django.urls import include, path
from django.conf import settings
from django.contrib import admin

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("app.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
