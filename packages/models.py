from django.db import models


class Package(models.Model):
    name = models.CharField(max_length=200)
    version = models.CharField(max_length=200)
    license = models.CharField(max_length=200)

    class Meta:
        unique_together = ('name', 'version',)

    def __str__(self):
        return self.name


class Vulnerability(models.Model):
    package = models.ForeignKey(Package, on_delete=models.CASCADE, related_name="vulnerabilities")
    id = models.CharField(max_length=200, primary_key=True)
    description = models.CharField(max_length=200)
    created = models.CharField(max_length=200)

    def __str__(self):
        return self.id

    class Meta:
      ordering = ['id']
