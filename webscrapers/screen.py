import curses

from webscrapers.utils import get_timestamp

class Screen:
    STATUS_SIZE = 5

    def __init__(self, stdscr):
        self._stdscr = stdscr
        self._init_screen()

    def _init_screen(self):
        # Config
        curses.curs_set(0)
        curses.noecho()

        curses.use_default_colors()
        curses.start_color()
        curses.init_pair(1, curses.COLOR_RED, -1)
        curses.init_pair(2, curses.COLOR_GREEN, -1)

        self._stdscr.clear()

        MAX_ROW, MAX_COL = self._stdscr.getmaxyx()

        self._status_win = self._stdscr.subwin(Screen.STATUS_SIZE, MAX_COL, 0, 0)
        self._logging_win = self._stdscr.subwin(Screen.STATUS_SIZE, 0)

        self._status_win.box()
        self._status_win.addstr("Status: ")
        
        self._logging_win.box()
        self._logging_win.addstr("Logs: ")
        self._log_message_win = self._logging_win.subwin(MAX_ROW - (Screen.STATUS_SIZE + 2), MAX_COL - 2, Screen.STATUS_SIZE + 1, 1)
        self._log_message_win.scrollok(True)

        self._stdscr.refresh()
        return

    def update_status(self, is_button_disabled, price_difference):
        timestamp = get_timestamp()

        self._status_win.move(1, 1)
        self._status_win.addstr(f"The button is: ")
        if is_button_disabled:
            self._status_win.addstr(f"DISABLED", curses.color_pair(1))
        else:
            self._status_win.addstr(f"ENABLED", curses.color_pair(2))
        self._status_win.move(2, 1)
        self._status_win.addstr(f"Price difference is: ")
        if float(price_difference) < 20:
            self._status_win.addstr(f"{price_difference}", curses.color_pair(2))
        else:
            self._status_win.addstr(f"{price_difference}", curses.color_pair(1))
        self._status_win.move(3, 1)
        self._status_win.addstr(f"Last update at: {timestamp}")
        self._status_win.refresh()

        message = f"The button is disabled? {is_button_disabled}, price difference from baseline: {price_difference}"
        self.update_log(message)
        self.update_log(f"Last update at: {timestamp}")
        return

    def update_log(self, message):
        self._log_message_win.addstr(f"{get_timestamp()} - {message} \n")
        self._log_message_win.refresh()
        return