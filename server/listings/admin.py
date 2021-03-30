from django.contrib import admin

from .models import Listing, FrontendFramework, BackendFramework, TechStack


class ListingAdmin(admin.ModelAdmin):

    # list_display = ("company",)
    ...


admin.site.register(Listing, ListingAdmin)
admin.site.register(TechStack, ListingAdmin)
admin.site.register(FrontendFramework, ListingAdmin)
admin.site.register(BackendFramework, ListingAdmin)