from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=50)
    website = models.URLField(max_length=50)
    foundation = models.PositiveIntegerField()

class Developers (models.Model):
    name = models.CharField(max_length=50)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)