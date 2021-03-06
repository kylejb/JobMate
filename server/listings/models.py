"""Listing Model."""
from django.db import models


class Listing(models.Model):
    """Base Listing Model."""

    company = models.CharField(max_length=50)
    date_listed = models.DateField()
    description = models.TextField()
    languages = models.CharField(max_length=200)
    location = models.CharField(max_length=25)
    required_experience = models.CharField(max_length=25)
    salary = models.CharField(max_length=7)
    title = models.CharField(max_length=100)
    url = models.TextField()
    created_at = models.DateField()

    def __str__(self):
        return f"Listing(<id={self.id} title={self.title} company={self.company} />)"
