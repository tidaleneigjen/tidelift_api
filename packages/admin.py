from django.contrib import admin
from .models import Package, Vulnerability


@admin.register(Package)
class PackageAdmin(admin.ModelAdmin):
    pass


@admin.register(Vulnerability)
class VulnerabilityAdmin(admin.ModelAdmin):
    pass
