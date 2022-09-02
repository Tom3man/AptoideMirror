import os
import sys
import inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
repo_dir = os.path.dirname(currentdir)
sys.path.insert(0, repo_dir) 

from aptoide_mirror.scrapers.aptoide_scraper import ScrapeAppPage 

from datetime import datetime
import random
import unittest


class TestScrapeAppPage(unittest.TestCase):

    """
    Test class used to test the ScrapeAppPage class by use of set URLs for the aptoid website. Upon creating a class instance one of these URLs is selected at random.
    """

    @classmethod
    def setUpClass(cls):

        test_urls = {
            "https://binemongame.en.aptoide.com/app": "Binemon",
            "https://supermonsterball.en.aptoide.com/app": "Super Monster Ball - Shoot the ball",
            "https://my-talking-tom-2-outfit7-limited.en.aptoide.com/app": "My Talking Tom 2"
        }

        url, TestScrapeAppPage.app_name = random.choice(list(test_urls.items()))

        TestScrapeAppPage.inst = ScrapeAppPage(url)
        TestScrapeAppPage.inst.extract()

    def test_app_title(self):

        app_name_scrape = TestScrapeAppPage.inst.app_name
        self.assertEqual(TestScrapeAppPage.app_name, app_name_scrape)

    def test_app_downloads(self):

        app_downloads = TestScrapeAppPage.inst.app_downloads
        self.assertIsInstance(app_downloads, int)

    def test_release_date(self):

        release_date_str = TestScrapeAppPage.inst.app_release_date

        release_date_dt = datetime.strptime(release_date_str, '%d-%m-%Y')

        self.assertIsInstance(release_date_dt, datetime)

    def test_version(self):

        app_version = TestScrapeAppPage.inst.app_version

        self.assertTrue(app_version)

    def test_description(self):

        app_description = TestScrapeAppPage.inst.app_description
        self.assertTrue(len(app_description) > 10)


if __name__ == '__main__':
    unittest.main()
