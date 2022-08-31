import time
import string
from bs4 import BeautifulSoup

import logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s :: %(levelname)s :: %(message)s')

from .common import webscraping_tools


class ScrapeAppPage:

    """
    This class is used to extract app information from the aptoide website when given a specific url string for an application. 
    It compiles the relevant information as property methods. 
    After initial compiling, running the extract method will return the following in string format:
        - app name
        - app version
        - version release date
        - number of downloads 
        - app description
        - app requirements for android devices

    """

    def __init__(self, log=False):

        self.log = log

    def extract(self, url: str):

        extracted_dict = {}

        self.url = url

        # Extract the raw page HTML and parse with bs4
        if self.log:
            logging.info(f"Extracting raw page info from URL: {self.url}.")

        try:
            self.app_page = BeautifulSoup(webscraping_tools.user_agent_randomiser(self.url).content, 'html.parser')
            if self.log:
                time.sleep(1)
                logging.info(f"Raw page info for {self.url} successfully extracted.")
        except: 
            raise ValueError("Supplied URL returned no response")

        self._extract_main_div_html(div_name='header-desktop__HeaderContainer-xc5gow-0 eBfMrO')
        self._app_version_div_container(div_name='mini-versions__Version-sc-19sko2j-4 ikysfs')
        self._stats_div_container(div_name='mini-stats__Row-sc-188veh1-2 kSzdYC')
        self._description_container(div_name='description__Paragraph-sc-45j1b1-1 daWyZe')

        extracted_dict = {
            'app_name': self.app_name, 
            'app_version': self.app_version, 
            'app_downloads': self.app_downloads, 
            'app_description': self.app_description, 
            'app_release_date': self.app_release_date, 
            'app_requirements': self.app_requirements
        }

        return extracted_dict

    @staticmethod
    def _check_response(div_name: str, method: object):
        """
        Static helper method that checks if the HTML response is None
        """
        if not method:
            raise ValueError(f"Main container could not be extracted using supplied div-class name: {div_name}.")

    def _extract_main_div_html(self, div_name: str):

        # Filter the raw HTML to include just the main div container
        # Risk here using div name as this may change server-side
        self.div_container_main_html = self.app_page.find('div', {'class': div_name})
        self._check_response(div_name=div_name, method=self.div_container_main_html)

    def _app_version_div_container(self, div_name: str) -> str:

        self.app_version_container = self.app_page.find('div', {'class': div_name})
        self._check_response(div_name=div_name, method=self.app_version_container)

    def _stats_div_container(self, div_name: str):

        self.stats_container = self.app_page.find('div', {'class': div_name})
        self._check_response(div_name=div_name, method=self.stats_container)

    def _description_container(self, div_name: str):

        self.desc_container = self.app_page.find('p', {'class': div_name})
        self._check_response(div_name=div_name, method=self.desc_container)

    @property
    def app_name(self) -> str:
        return self.div_container_main_html.find("h1").text

    @property
    def app_version(self) -> str:
        return self.app_version_container.find_all('div')[0].text

    @property
    def app_release_date(self) -> str:
        return ''.join(char for char in self.app_version_container.find_all('div')[1].text if char in string.digits + "-")

    @property
    def app_downloads(self) -> str:
        return self.stats_container.find_all('div')[0].text.split(' ')[0]

    @property
    def app_size(self) -> str:
        return self.stats_container.find_all('div')[2].text.split(' ')[0]

    @property
    def app_requirements(self) -> str:
        return self.stats_container.find_all('div')[4].text

    @property
    def app_description(self) -> str:

        paragraphs = []
        for paragraph in self.desc_container:
            if len(paragraph) > 2:
                paragraphs.append(paragraph.text)

        return '\n'.join(paragraphs)
