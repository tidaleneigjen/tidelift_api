from rest_framework.response import Response
from rest_framework.decorators import api_view
from packages.models import Package, Vulnerability
from .serializers import PackageSerializer, VulnerabilitySerializer


@api_view(['GET'])
def get_licenses(request):
    licenses = [
        {
            "name": "dummy",
            "license": "MIT"
        },
        {
            "name": "tiny-tarball",
            "license": "ISC"
        },
        {
            "name": "axios",
            "license": "MIT"
        }
    ]

    licenses = Package.objects.all()
    serializer = PackageSerializer(licenses, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_vulunerabilities(request):
    vulnerabilities = [
        {
            "id": "v2017-001",
            "name": "dummy",
            "version": "0.9",
            "description": "this is a dummy cve",
            "created": "1504558984"
        },
        {
            "id": "v2017-002",
            "name": "dummy",
            "version": "0.8",
            "description": "another cve",
            "created": "1504550442"
        },
        {
            "id": "v2017-003",
            "name": "dummy",
            "version": "0.8",
            "description": "another, one",
            "created": "1504560442"
        }
    ]

    vulnerabilities = Vulnerability.objects.all()
    serializer = VulnerabilitySerializer(vulnerabilities, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_health(request, **kwargs):
    package = Package.objects.get(name='dummy')
    vuln = Vulnerability.objects.filter(name='dummy')
    
    serializer = HealthSerializer(package)

    return Response(serializer.data)
