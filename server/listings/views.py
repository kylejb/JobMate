from listings.models import Listing
from listings.serializers import ListingSerializer
from rest_framework import viewsets


class ListingView(viewsets.ModelViewSet):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer

    def get_queryset(self):

        search_query = self.request.query_params.get("search", None)

        if search_query is not None:
            self.queryset = self.queryset.filter(title=search_query)

        return self.queryset
