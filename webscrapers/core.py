import time
import subprocess

from webscrapers.screen import Screen
from webscrapers.browser import Browser


class Core:
    def __init__(self, wrapped_screen, url, baseline_price, use_firefox=True, headless=True, delay_tries = 10, delay_success = 50):
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

    def run(self):
        while (True):
            self._screen.update_log(f"Parsing url: {self._url}")

            soup = self._browser.parse_web(self._url)

            is_button_disabled = self._browser.check_if_button_is_disabled(soup)
            current_price = self._browser.check_current_price(soup)

            price_difference = str(float(current_price) - float(self._baseline_price))

            self._screen.update_status(is_button_disabled, price_difference)

            if not is_button_disabled:
                self._screen.update_log("*** BUY BUY BUY ***")
                subprocess.call(["xdg-open", self._url])
                self.send_notification("*** BUY BUY BUY ***")
                time.sleep(self._delay_success)

            time.sleep(self._delay_tries)