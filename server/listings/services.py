"""Web Scraping for Listings."""
import re
import urllib.request
from datetime import datetime, timedelta
from .models import Listing

from bs4 import BeautifulSoup


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
        # filter=0 to show all
        super().__init__(
            base_url,
            default_query,
            location=default_location,
            sort=default_sort,
            age=default_age,
        )
        self._last_page = -1
        self.start = "00"

    def scrape_final_page(self, url) -> str:
        """Return last_page."""
        last_url = url + "&start=999999999"
        soup = self.init_soup(last_url)

        IndeedScraper.scrape_page(soup)

        page_counter = soup.find(id="searchCountPages").string.strip()
        last_page = page_counter.split(" ")[1]

        self._last_page = int(last_page)

    @staticmethod
    def init_soup(url):
        source = urllib.request.urlopen(url).read()
        return BeautifulSoup(source, "lxml")

    @staticmethod
    def scrape_page(soup):
        """Scrape Indeed Page.

        go to start=999999999
        do the thing on this page and temp_save the "page # of ### jobs"
            --> id=searchCountPages (Page 11 of 234 jobs)
        when we hit "page # - 1" stop when done there.

            results_col = soup.find(id="resultsCol")
        Grab divs with ids
            results_col.find_all(class_="jobsearch-SerpJobCard")

            append jobCard id to url: https://www.indeed.com/viewjob?
            extract all description stuff and store

            when all divs are read, go to next page until end.
        """
        results_col = soup.find(id="resultsCol")
        jobcards = results_col.find_all(class_="jobsearch-SerpJobCard")

        # TEMP hardcoded test
        jobcard = jobcards[1]

        # * title
        jobcard_title_obj = jobcard.find(class_="title")
        jobcard_title = jobcard_title_obj.a["title"]
        # * url
        jobcard_id = jobcard.a["id"].split("_")[1]
        show_page_url = "https://www.indeed.com/viewjob?jk=" + jobcard_id

        # * location
        jobcard_location_obj = jobcard.find(class_="recJobLoc")
        jobcard_location = jobcard_location_obj["data-rc-loc"]

        # * date_listed
        # today or x days ago... to be set in DB
        # y_record = jobcard
        listing_date = jobcard.find(class_="date date-a11y").contents[0].strip()
        print("LD", listing_date, type(listing_date))
        if listing_date == "Today":
            listing_date = datetime.today()
        else:
            days_ago = listing_date.split(" ")[0]
            listing_date = datetime.today() - timedelta(days=int(days_ago))

        # * company (company_name for now)
        #! add logic based on contents length (i.e., if a tag exists or if just innerHTML)
        # .a.contents vs .contents
        jobcard_company_obj = jobcard.find(class_="company").a.contents
        company_name = jobcard_company_obj[0].strip()

        # * description
        # navigate to show page
        job_desc, required_exp = IndeedScraper.get_job_description_and_exp(
            show_page_url
        )
        job_desc_text = job_desc.get_text()

        listing_test = Listing(
            title=jobcard_title,
            company=company_name,
            url=show_page_url,
            location=jobcard_location,
            description=job_desc_text,
            required_experience=required_exp,
            date_listed=listing_date,
        )

        listing_test.save()

    @staticmethod
    def get_job_description_and_exp(url):
        soup = IndeedScraper.init_soup(url)
        job_desc = soup.find(id="jobDescriptionText")
        job_desc_content = job_desc.get_text()
        required_experience = IndeedScraper.years_in_description(job_desc_content)
        return job_desc, required_experience

    @staticmethod
    def run(url):
        bot = IndeedScraper()
        bot.scrape_final_page(url)

        for i in range(bot._last_page):
            soup = IndeedScraper.init_soup(url + f"&start={i}0")
            bot.scrape_page(soup)

    # helper method to parse description string
    @staticmethod
    def years_in_description(description):
        # TODO - improve regex for year extraction
        # currenty looks for adjacent digit only
        # ? how can we intelligently extract when years == exp requirement in doc
        match_obj = re.search(r"[\d ()+]+(?:^|\W)years(?:$|\W)", description)
        if match_obj:
            return match_obj.group()
        return None
