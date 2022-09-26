from rest_framework.response import Response
from rest_framework.decorators import api_view
from packages.models import Package
from .serializers import PackageSerializer
import requests


@api_view(['GET'])
def get_package_detail(request, **kwargs):

    package = Package.objects.get(
        name=kwargs['name'], version=kwargs['version'])
    serializer = PackageSerializer(package)
    return Response(serializer.data)


@api_view(['GET'])
def get_releases(request, **kwargs):
    response = {}
    package_name = kwargs['package_name']
    url_string = str.format('https://registry.npmjs.org/{}', package_name)

    r = requests.get(url_string)

    if r.status_code == 200:
        releases = list(r.json()['versions'].keys())
        response['data'] = {
            "name": package_name,
            "latest": releases[-1],
            "releases": releases
        }
    else:
        response['data'] = {}

    return Response(response['data'])
