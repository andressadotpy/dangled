from re import S
from monitor import DomainMonitor

from colorama import Back, Style

class Domain:

    def __init__(self, name: str) -> None:
        self.name = name

    def monitor(self) -> None:
        print(Back.WHITE + f"{self.name}" + Style.RESET_ALL)
        monitor = DomainMonitor(self.name)
        monitor.monitor_all()

    def __str__(self) -> str:
        return f"{self.name}"