from namecheap_sdk.client.client import NamecheapClient
from namecheap_sdk.namecheap import Namecheap


def test_import():
    assert Namecheap is not None

# ---------------------------------------------------
# Test Initialization
# ---------------------------------------------------   
def test_intialization(config):
    namecheap = Namecheap(config)
    assert namecheap.config == config
    assert isinstance(namecheap.client, NamecheapClient)
    assert namecheap.ssl is not None