"""jobmate_api URL Configuration."""
from django.contrib import admin
from django.conf.urls import url
from rest_framework import routers
from listings.views import ListingView

router = routers.SimpleRouter()
router.register(r"listings", ListingView)

urlpatterns = [
    url("admin/", admin.site.urls),
]

urlpatterns += router.urls
