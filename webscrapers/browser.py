import re
import requests

from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

from bs4 import BeautifulSoup as bs4

class Browser:
    TIMEOUT = 10

    def __init__(self, use_firefox=True, headless=True):
        self._use_firefox = use_firefox
        self._headless = headless
        self._init_browser()
    
    def _init_browser(self):
        if self._use_firefox:
            opts = FirefoxOptions()
        else:
            opts = ChromeOptions()

        if self._headless:
                opts.add_argument("--headless")

        if self._use_firefox:
            self._browser = webdriver.Firefox(options=opts)
        else:
            self._browser = webdriver.Chrome(options=opts)
        self._browser.implicitly_wait(Browser.TIMEOUT)
    
    def parse_web(self, url):
        self._browser.get(url)
        soup = bs4(self._browser.page_source, 'html.parser')
        return soup

    def check_if_button_is_disabled(self, soup):
        pattern = re.compile("disabled")
        button_content = soup.find(attrs={'class':"js-article-add-to-cart"})
        result = pattern.search(str(button_content))
        return bool(result)


    def check_current_price(self, soup):
        price_class = soup.find("div", attrs={'id':"precio-main"})
        return price_class['data-price']
    
   