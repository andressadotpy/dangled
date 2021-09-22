import dns.resolver

from records import A, AAAA, MX
from unittest.mock import patch

def test_if_record_A_exists():
    result = A('andressa.dev').monitor()
    assert len(result) != 0

@patch('records.Record._handle_errors')
def test_response_nxdomain_for_non_existant_domain(mocked_handle_errors):
    monitor = A('andressacabistani.dev')
    monitor.monitor()
    assert mocked_handle_errors.called_once_with(dns.resolver.NXDOMAIN)

@patch('records.Record._handle_errors')
def test_if_record_AAAA_get_no_answer(mocked_handle_errors):
    monitor = AAAA('andressa.dev')
    monitor.monitor()
    assert mocked_handle_errors.called_once_with(dns.resolver.NoAnswer)

@patch('records.Record._handle_errors')
def test_if_record_MX_get_no_answer(mocked_handle_errors):
    monitor = MX('andressa.dev')
    monitor.monitor()
    assert mocked_handle_errors.called_once_with(dns.resolver.NoAnswer)