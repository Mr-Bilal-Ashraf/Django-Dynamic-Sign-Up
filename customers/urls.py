from django.conf.urls.static import static
from django.urls import path, include
from django.conf import settings
from django.contrib import admin

from rest_framework.routers import DefaultRouter

from customers import views


router = DefaultRouter()
router.register(r"signup-templates", views.SignUpTemplateView)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
