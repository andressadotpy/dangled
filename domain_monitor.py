from dangling import DanglingRecord
import dns.resolver


class DomainMonitor:

    def __init__(self, domain_name: str) -> None:
        self.domain_name = domain_name
        self.records_to_be_monitor = [
            self.monitorA,
            self.monitorAAAA,
            self.monitorCNAME,
            self.monitorMX,
            self.monitorNS,
            self.monitorTXT,
        ]
    
    def monitorA(self) -> list:
        try:
            data = []
            for rdata in dns.resolver.resolve(self.domain_name, 'A'):
                data.append(rdata.address)
            return data
        except Exception as e:
            self._handle_errors(e)

    def monitorAAAA(self) -> list:
        try:
            data = []
            for rdata in dns.resolver.resolve(self.domain_name, 'AAAA'):
                data.append(rdata.address)
            return data
        except Exception as e:
            self._handle_errors(e)    

    def monitorCNAME(self) -> list:
        try:
            data = []
            for rdata in dns.resolver.resolve(self.domain_name, 'CNAME'):
                data.append(rdata.target)
            return data
        except Exception as e:
            self._handle_errors(e)

    def monitorMX(self) -> list:
        try:
            data = []
            for rdata in dns.resolver.resolve(self.domain_name, 'MX'):
                data.append(rdata.exchange)
            return data
        except Exception as e:
            self._handle_errors(e)

    def monitorNS(self) -> list:
        try:
            data = []
            for rdata in dns.resolver.resolve(self.domain_name, 'NS'):
                data.append(rdata.target)
            return data
        except Exception as e:
            self._handle_errors(e)

    def monitorTXT(self):
        try:
            data = []
            for rdata in dns.resolver.resolve(self.domain_name, 'TXT'):
                data.append(self._decoded_rdata(rdata))
            return data
        except Exception as e:
            self._handle_errors(e)

    def monitor_all(self) -> None:
        for monitor_function in self.records_to_be_monitor:
            print(f'{monitor_function}: ', monitor_function())

    def _decoded_rdata(self, rdata: str):
        return rdata.strings[0].decode('UTF-8')

    def _handle_errors(self, error):
        if error == dns.resolver.NoAnswer:
            return []
        elif error == dns.resolver.Timeout:
            raise dns.resolver.Timeout
        elif error == dns.resolver.NXDOMAIN:
            raise DanglingRecord('This record must be dangling and is a risky dangling record.')        