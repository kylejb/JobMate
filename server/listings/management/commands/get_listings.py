from listings.services import IndeedScraper
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Collect Indeed Job Listing data."

    def handle(self, *args, **kwargs):
        x = IndeedScraper()
        self.stdout.write(f"{x} Task complete.")
