from django.urls import path
from .views import health, upload_log

urlpatterns = [
    path("health/", health),
    path("upload/", upload_log),
]