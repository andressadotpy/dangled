from abc import ABCMeta, abstractmethod

import dns.resolver
from exceptions import DanglingRecord

class Record:
    def __init__(self, domain_name) -> None:
        self.domain_name = domain_name
    
    @abstractmethod
    def monitor(self) -> list:
        return []

    def _handle_errors(self, error):
        if error == dns.resolver.NoAnswer:
            return []
        elif error == dns.resolver.Timeout:
            raise dns.resolver.Timeout
        elif error == dns.resolver.NXDOMAIN:
            raise DanglingRecord('This record must be dangling and is a risky dangling record.')     


class A(Record):
    def monitor(self) -> list:
        print('Monitor A record:')
        try:
            data = []
            for rdata in dns.resolver.resolve(self.domain_name, 'A'):
                data.append(rdata.address)
            return data
        except Exception as e:
            self._handle_errors(e)


class AAAA(Record):
    def monitor(self) -> list:
        print('Monitor AAAA record:')
        try:
            data = []
            for rdata in dns.resolver.resolve(self.domain_name, 'AAAA'):
                data.append(rdata.address)
            return data
        except Exception as e:
            self._handle_errors(e)    


class CNAME(Record):
    def monitor(self) -> list:
        print('Monitor CNAME record:')
        try:
            data = []
            for rdata in dns.resolver.resolve(self.domain_name, 'CNAME'):
                data.append(rdata.target)
            return data
        except Exception as e:
            self._handle_errors(e)


class MX(Record):
    def monitor(self) -> list:
        print('Monitor MX record:')
        try:
            data = []
            for rdata in dns.resolver.resolve(self.domain_name, 'MX'):
                data.append(rdata.exchange)
            return data
        except Exception as e:
            self._handle_errors(e)


class NS(Record):
    def NS(self) -> list:
        print('Monitor NS record:')
        try:
            data = []
            for rdata in dns.resolver.resolve(self.domain_name, 'NS'):
                data.append(rdata.target)
            return data
        except Exception as e:
            self._handle_errors(e)


class TXT(Record):
    def TXT(self):
        print('Monitor TXT record:')
        try:
            data = []
            for rdata in dns.resolver.resolve(self.domain_name, 'TXT'):
                data.append(self._decoded_rdata(rdata))
            return data
        except Exception as e:
            self._handle_errors(e)

    def _decoded_rdata(self, rdata: str):
        return rdata.strings[0].decode('UTF-8')