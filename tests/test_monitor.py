from domain import Domain
from unittest.mock import patch
import dns.resolver

from monitor import DomainMonitor


def test_monitor_all_records():
    monitor = DomainMonitor('andressa.dev')
    result = monitor.monitor_all()
    assert isinstance(result, dict)
