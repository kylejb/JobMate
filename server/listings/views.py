from listings.models import Listing
from listings.serializers import ListingSerializer
from rest_framework import viewsets


class ListingView(viewsets.ModelViewSet):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer
