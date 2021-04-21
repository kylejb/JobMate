from listings.models import Listing
from rest_framework import serializers


class ListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Listing

        fields = [
            "company",
            "date_listed",
            "description",
            "tech_stack",
            "location",
            "required_experience",
            "salary",
            "title",
            "url",
        ]
