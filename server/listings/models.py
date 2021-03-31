"""Listing Model."""
from django.db import models


class FrontendFramework(models.Model):
    framework = models.CharField(max_length=100)

    def __str__(self):
        return f"FrontendFramework({self.framework})"


class BackendFramework(models.Model):
    framework = models.CharField(max_length=100)

    def __str__(self):
        return f"BackendFramework({self.framework})"


class TechStack(models.Model):
    frontend_framework = models.ForeignKey(FrontendFramework, on_delete=models.CASCADE)
    backend_framework = models.ForeignKey(BackendFramework, on_delete=models.CASCADE)

    def __str__(self):
        return f"TechStack({self.frontend_framework.framework} {self.backend_framework.framework})"


class Listing(models.Model):
    """Base Listing Model."""

    company = models.CharField(max_length=50)
    date_listed = models.DateField()
    description = models.TextField()
    tech_stack = models.ForeignKey(TechStack, on_delete=models.CASCADE)
    location = models.CharField(max_length=25)
    required_experience = models.CharField(max_length=25)
    salary = models.CharField(max_length=7)
    title = models.CharField(max_length=100)
    url = models.TextField()
    created_at = models.DateField()

    def __str__(self):
        return f"Listing(<id={self.id} title={self.title} company={self.company} />)"
