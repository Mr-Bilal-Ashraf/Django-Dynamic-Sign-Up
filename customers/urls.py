from django.conf.urls.static import static
from django.urls import path, include
from django.conf import settings
from django.contrib import admin

from rest_framework.routers import DefaultRouter

from customers import views


router = DefaultRouter()
router.register(r"signup-templates", views.SignUpTemplateView)
router.register(r"tenant", views.TenantViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
    path(
        "tenant/<int:pk>/update_tenant_template/<int:template_id>/",
        views.TenantViewSet.as_view({"patch": "update_tenant_template"}),
        name="update_tenant_template",
    ),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
