from django.db import models


class Package(models.Model):
    name = models.CharField(max_length=200)
    license = models.CharField(max_length=200)


class Vulnerability(models.Model):
    id = models.CharField(max_length=200, primary_key=True)
    description = models.CharField(max_length=200)
    version = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    package = models.ForeignKey(Package, on_delete=models.CASCADE)
