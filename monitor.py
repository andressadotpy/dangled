from records import A, AAAA, CNAME, MX, NS, TXT


class DomainMonitor:

    def __init__(self, domain_name: str) -> None:
        self.domain_name = domain_name
        self.records_to_monitor = [
            A,
            AAAA,
            CNAME,
            MX,
            NS,
            TXT,
        ]
    
    def monitor_all(self) -> dict:
        for record in self.records_to_monitor:
            record(self.domain_name).monitor()