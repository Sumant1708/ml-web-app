# api/urls.py
from django.urls import path
from .views import predict

urlpatterns = [
    path('predict/', predict),
]
