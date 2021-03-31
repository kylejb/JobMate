"""Web Scraping for Listings."""
import re


class BaseScraper:
    """Base Scraper."""

    def __init__(self, base_url, query, **kwargs):
        """Attributes for all instances of Scraper.

        Parameters:
            base_url: String representing URL path to desired resource
            query: String representing desired search result
            **kwargs: Dictionary representing QueryParameters
                - QueryParameters:
                    - location: "&l=New+York%2C+NY"
                    - sort: "&sort=date"
                    - from_age: "fromage=14"
        """
        self.base_url = base_url
        self.query = query
        self.location = kwargs.get("location")
        self.sort = kwargs.get("sort")
        self.from_age = kwargs.get("from_age")

    def __str__(self):
        domain = self.base_url.split(".")[1].capitalize()
        return f"{domain}Scraper(< query: {self.query} >)"

    def __repr__(self):
        domain = self.base_url.split(".")[1].capitalize()
        return f"{domain}Scraper(< query: {self.query} >)"


class IndeedScraper(BaseScraper):
    """Indeed Scraper."""

    def __init__(self):
        base_url = "https://www.indeed.com/jobs?q="
        default_query = "software+engineer"
        default_location = "New+York%2C+NY"
        default_sort = "sort=date"
        default_age = "fromage=14"

        super().__init__(
            base_url,
            default_query,
            location=default_location,
            sort=default_sort,
            age=default_age,
        )

    def scrape_page():
        ...

    def run():
        ...

    # helper method to parse description string
    @staticmethod
    def years_in_description(description):
        return re.match(r"""[\d ()+]+(?:^|\W)years(?:$|\W)""", description)
