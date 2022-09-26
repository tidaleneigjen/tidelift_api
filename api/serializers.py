from rest_framework import serializers
from packages.models import Package, Vulnerability


class VulnerabilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Vulnerability
        fields = ['id', 'description', 'created']


class PackageSerializer(serializers.ModelSerializer):
    vulnerabilities = VulnerabilitySerializer(many=True, read_only=True)

    class Meta:
        model = Package
        fields = ['name', 'version', 'license', 'vulnerabilities']
