import os
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')

def test_resilio_package(host):
    resilio = host.package('resilio-sync')
    assert resilio.is_installed

def test_resilio_service_running(host):
    rslsync = host.service('resilio-sync')
    assert rslsync.is_running
    assert rslsync.is_enabled

def test_resilio_listening(host):
    rslsync = host.socket('tcp://127.0.0.1:8888')
    assert rslsync.is_listening
