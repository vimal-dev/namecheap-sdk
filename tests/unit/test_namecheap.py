
import httpx
import pytest

from namecheap_sdk.client.client import NamecheapClient
from namecheap_sdk.namecheap import Namecheap


def test_import():
    assert Namecheap is not None

# ---------------------------------------------------
# Test Initialization
# ---------------------------------------------------   
def test_intialization(config):
    def handler(request: httpx.Request):
        return httpx.Response(500, text="Server Error")

    client = httpx.Client(
        base_url=config.endpoint,
        timeout=config.timeout,
        transport=httpx.MockTransport(handler)
    )
    nc = NamecheapClient(config, client=client)
    namecheap = Namecheap(config)
    assert namecheap.config == config
    assert isinstance(namecheap.client, NamecheapClient)
    assert namecheap.ssl is not None