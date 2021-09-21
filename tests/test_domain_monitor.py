from domain import Domain
from unittest.mock import patch
import dns.resolver

from domain_monitor import DomainMonitor


def test_if_record_A_exists():
    monitor = DomainMonitor('andressa.dev')
    monitor.monitorA()
    assert len(monitor.monitorA()) == 1

def test_monitor_all():
    monitor = DomainMonitor('andressa.dev')
    assert monitor.monitor_all() == None

@patch('domain_monitor.DomainMonitor._handle_errors')
def test_response_nxdomain_for_non_existant_domain(mocked_handle_errors):
    monitor = DomainMonitor('andressacabistani.dev')
    monitor.monitorA()
    assert mocked_handle_errors.called_once_with(dns.resolver.NXDOMAIN)

@patch('domain_monitor.DomainMonitor._handle_errors')
def test_if_record_AAAA_get_no_answer(mocked_handle_errors):
    monitor = DomainMonitor('andressa.dev')
    monitor.monitorAAAA()
    assert mocked_handle_errors.called_once_with(dns.resolver.NoAnswer)

@patch('domain_monitor.DomainMonitor._handle_errors')
def test_if_record_MX_get_no_answer(mocked_handle_errors):
    monitor = DomainMonitor('andressa.dev')
    monitor.monitorMX()
    assert mocked_handle_errors.called_once_with(dns.resolver.NoAnswer)