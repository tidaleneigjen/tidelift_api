from django.urls import path
from . import views

urlpatterns = [
    path('package/health/<str:name>/<str:version>', views.get_package_detail),
    path('package/releases/<str:package_name>', views.get_releases),
]
