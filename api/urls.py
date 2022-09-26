from django.urls import path
from . import views

urlpatterns = [
    path('licenses', views.get_licenses),
    path('vulnerabilities', views.get_vulunerabilities),
    path('package/health', views.get_health)
]
