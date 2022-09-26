from django.urls import path
from . import views

urlpatterns = [
    # path('package/health', views.get_package_all),
    path('package/health/<str:name>/<str:version>', views.get_package_detail),
    # path('vulnerabilities', views.get_vulnerability_all),
    # path('vulnerabilities/<str:id>', views.get_vulnerability_detail),
    path('package/releases/<str:package_name>', views.get_releases),
]
