from django.urls import path

from app import views

urlpatterns = [
    path("my_signup_template/", views.my_signup_template),
]
