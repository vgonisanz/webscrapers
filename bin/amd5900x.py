#!/usr/bin/env python
# coding: utf-8

import sys
import signal
from curses import wrapper

from webscrapers.core import Core

url = 'https://www.pccomponentes.com/amd-ryzen-9-5900x-37-ghz'
#url = 'https://www.pccomponentes.com/lenovo-legion-5-15imh05-intel-core-i7-10750h-8gb-512gb-ssd-gtx1650-156'   # This is available
baseline_price = "569.90"

def signal_handler(sig, frame):
    print('You pressed Ctrl+C!')
    sys.exit(0)


def main(wrapped_screen):
    signal.signal(signal.SIGINT, signal_handler)

    core = Core(wrapped_screen, url, baseline_price)
    core.run()
    return

if __name__ == "__main__":
    wrapper(main)