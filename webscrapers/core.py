import time
import subprocess
import re

from webscrapers.screen import Screen
from webscrapers.browser import Browser


class Core:
    def __init__(self, wrapped_screen, url, baseline_price, use_firefox=True, headless=True, delay_tries = 10, delay_success = 10):
        self._url = url
        self._baseline_price = baseline_price
        self._delay_tries = delay_tries
        self._delay_success = delay_success
        
        self._screen = Screen(wrapped_screen)
        self._screen.update_log(f"Initializing browser...")
        self._browser = Browser(use_firefox=use_firefox, headless=headless)
        return
    
    def send_notification(self, message):
        subprocess.Popen(['notify-send', message])
        return

    def check_if_button_is_disabled(self, soup):
        """May move to scraper class url dependent"""
        pattern = re.compile("disabled")
        button_content = soup.find(attrs={'class':"js-article-add-to-cart"})
        result = pattern.search(str(button_content))
        return bool(result)


    def check_current_price(self, soup):
        """May move to scraper class url dependent"""
        price_class = soup.find("div", attrs={'id':"precio-main"})
        if price_class:
            return price_class['data-price']
        return None


    def update_screen(self, is_button_disabled, current_price):
        price_difference = str(float(current_price) - float(self._baseline_price))

        self._screen.update_status(is_button_disabled, price_difference)

        if not is_button_disabled:
            if float(price_difference) < 30.0:
                self._screen.update_log("*** BUY BUY BUY ***")
                subprocess.call(["xdg-open", self._url])
                self.send_notification("*** BUY BUY BUY ***")
            time.sleep(self._delay_success)

        time.sleep(self._delay_tries)
        return
    
    def run(self):
        while (True):
            self._screen.update_log(f"Parsing url: {self._url}")

            response = self._browser.parse_web(self._url)
            if response == None:
                self._screen.update_log("Browser returned None response")
                time.sleep(self._delay_tries)
                continue

            is_button_disabled = self.check_if_button_is_disabled(response.soup)
            current_price = self.check_current_price(response.soup)

            if current_price:
                self.update_screen(is_button_disabled, current_price)
            else:
                self._screen.update_log(f"Ignoring update, not price found")
                time.sleep(self._delay_tries)