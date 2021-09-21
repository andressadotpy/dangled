from domain_monitor import DomainMonitor


class Domain:

    def __init__(self, name: str) -> None:
        self.name = name

    def monitor(self) -> None:
        monitor = DomainMonitor(self.name)
        monitor.monitor_all()