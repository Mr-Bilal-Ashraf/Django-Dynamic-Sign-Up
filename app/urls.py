from django.urls import path

from app import views

urlpatterns = [
    path("signup-templates/<int:pk>/", views.SignUpTemplateView.as_view()),
    path("signup-templates/", views.SignUpTemplateView.as_view()),
]
