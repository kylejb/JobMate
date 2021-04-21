from listings.services import IndeedScraper
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Collect Indeed Job Listing data."

    def handle(self, *args, **kwargs):
        IndeedScraper.run(
            "https://www.indeed.com/jobs?q=software+engineer&l=New+York,+NY&fromage=1"
        )
        self.stdout.write("Task complete.")
