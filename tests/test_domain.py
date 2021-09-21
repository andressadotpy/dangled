from unittest.mock import patch
from domain import Domain


@patch('domain.DomainMonitor.monitor_all')
def test_monitor_all_by_the_client(mocked_monitor_all):
    domain = Domain('andressa.dev')
    domain.monitor()
    assert mocked_monitor_all.called_once_with(domain)