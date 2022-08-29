import random
from bs4 import BeautifulSoup
import requests

import logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s :: %(levelname)s :: %(message)s')

USER_AGENT_LIST = [
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:77.0) Gecko/20100101 Firefox/77.0',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',]


def user_agent_randomiser(url: str, log=False) -> object:

    """
    Function that takes as input a url and uses a random selection from the list below to return a request from the url

    args:
        url - string of url
        
    returns:
        requests response will need to be assigned to a variable
    
    example: soup1 = BeautifulSoup(--output from this--, 'html.parser')
    """

    user_agent = random.choice(USER_AGENT_LIST) 
    if log:
        logging.info(f"Initiating request of url {url} using user agent: {user_agent}")

    headers = {'User-Agent': user_agent}
    
    return requests.get(url, headers=headers)
