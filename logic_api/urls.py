# example/urls.py
from django.urls import path
from logic_api import test_api


urlpatterns = [
    path('test_api/', test_api.test_api_request),
]