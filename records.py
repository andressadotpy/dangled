from abc import ABCMeta, abstractmethod

from colorama import Back, Style

import dns.resolver
from exceptions import DanglingRecord

class Record(metaclass=ABCMeta):
    def __init__(self, domain_name: str) -> None:
        self.domain_name = domain_name
        self.data = []
    
    @abstractmethod
    def monitor(self) -> list:
        return []

    def _handle_errors(self, error):
        if isinstance(error, dns.resolver.NoAnswer):
            print("There's no data for this record type.")
        if isinstance(error, dns.resolver.Timeout):
            print("Your domain is timing out, needs to be checked.")
        if isinstance(error, dns.resolver.NXDOMAIN):
            print(Back.RED +
                """
                VULNERABILITY ISSUE:
                This domain doesn't exist anymore.
                Please delete all records pointing for this domain.
                """ + 
                Style.RESET_ALL)    


class A(Record):
    def monitor(self) -> list:
        print(Back.MAGENTA + "A record:" + Style.RESET_ALL)
        try:
            for rdata in dns.resolver.resolve(self.domain_name, 'A'):
                self.data.append(rdata.address)
            print(Back.MAGENTA + f"{self.data}" + Style.RESET_ALL)
            return self.data
        except Exception as e:
            self._handle_errors(e)


class AAAA(Record):
    def monitor(self) -> list:
        print(Back.CYAN + "AAAA record:" + Style.RESET_ALL)
        try:
            for rdata in dns.resolver.resolve(self.domain_name, 'AAAA'):
                self.data.append(rdata.address)
            print(Back.CYAN      + f"{self.data}" + Style.RESET_ALL)
            return self.data
        except Exception as e:
            self._handle_errors(e)  


class CNAME(Record):
    def monitor(self) -> list:
        print(Back.MAGENTA + "CNAME record:" + Style.RESET_ALL)
        try:
            for rdata in dns.resolver.resolve(self.domain_name, 'CNAME'):
                self.data.append(rdata.target)
            print(Back.MAGENTA + f"{self.data}" + Style.RESET_ALL)
            return self.data
        except Exception as e:
            self._handle_errors(e)


class MX(Record):
    def monitor(self) -> list:
        print(Back.CYAN + "MX record:" + Style.RESET_ALL)
        try:
            for rdata in dns.resolver.resolve(self.domain_name, 'MX'):
                self.data.append(rdata.exchange)
            print(Back.CYAN + f"{self.data}" + Style.RESET_ALL)
            return self.data
        except Exception as e:
            self._handle_errors(e)


class NS(Record):
    def monitor(self) -> list:
        print(Back.MAGENTA + "NS record:" + Style.RESET_ALL)
        try:
            for rdata in dns.resolver.resolve(self.domain_name, 'NS'):
                self.data.append(rdata.target)
            print(Back.MAGENTA + f"{self.data}" + Style.RESET_ALL)
            return self.data
        except Exception as e:
            self._handle_errors(e)


class TXT(Record):
    def monitor(self):
        print(Back.CYAN + "TXT record:" + Style.RESET_ALL)
        try:
            for rdata in dns.resolver.resolve(self.domain_name, 'TXT'):
                self.data.append(self._decoded_rdata(rdata))
            print(Back.CYAN + f"{self.data}" + Style.RESET_ALL)
            return self.data
        except Exception as e:
            self._handle_errors(e)

    def _decoded_rdata(self, rdata: str):
        return rdata.strings[0].decode('UTF-8')