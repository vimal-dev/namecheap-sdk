import pytest
import httpx

from namecheap_sdk.client.client import NamecheapClient
from namecheap_sdk.schemas.config import NamecheapConfig


# 🔹 Helper: create mock config
@pytest.fixture
def config():
    return NamecheapConfig(
        api_user="testuser",
        api_key="testkey",
        username="testuser",
        client_ip="127.0.0.1",
    )


# 🔹 Helper: mock transport
def mock_transport(handler):
    return httpx.MockTransport(handler)


# 🔹 Sample valid XML
VALID_XML = """<?xml version="1.0" encoding="UTF-8"?>
<ApiResponse Status="OK">
    <CommandResponse>
        <TestResult>Success</TestResult>
    </CommandResponse>
</ApiResponse>
"""


# ---------------------------------------------------
# SUCCESS CASE
# ---------------------------------------------------


def test_call_success(config):
    def handler(request: httpx.Request):
        assert request.method == "GET"

        # ensure params were attached
        assert request.url.params["Command"] == "test.command"
        assert request.url.params["ApiUser"] == "testuser"

        return httpx.Response(200, text=VALID_XML)

    client = httpx.Client(
        base_url=config.endpoint, timeout=config.timeout, transport=mock_transport(handler)
    )
    nc = NamecheapClient(config, client=client)

    response = nc.call("test.command", {"foo": "bar"})

    assert response["Status"] == "OK"
    assert response["CommandResponse"]["TestResult"] == "Success"


# ---------------------------------------------------
# HTTP ERROR
# ---------------------------------------------------


def test_http_error(config):
    def handler(request: httpx.Request):
        return httpx.Response(500, text="Server Error")

    client = httpx.Client(
        base_url=config.endpoint, timeout=config.timeout, transport=mock_transport(handler)
    )
    nc = NamecheapClient(config, client=client)

    with pytest.raises(httpx.HTTPStatusError):
        nc.call("test.command")


# ---------------------------------------------------
# INVALID XML
# ---------------------------------------------------


def test_invalid_xml(config):
    def handler(request: httpx.Request):
        return httpx.Response(200, text="INVALID_XML")

    client = httpx.Client(
        base_url=config.endpoint, timeout=config.timeout, transport=mock_transport(handler)
    )
    nc = NamecheapClient(config, client=client)

    with pytest.raises(ValueError, match="Invalid XML"):
        nc.call("test.command")


# ---------------------------------------------------
# MISSING ApiResponse
# ---------------------------------------------------


def test_missing_api_response(config):
    bad_xml = """<Invalid></Invalid>"""

    def handler(request: httpx.Request):
        return httpx.Response(200, text=bad_xml)

    client = httpx.Client(
        base_url=config.endpoint, timeout=config.timeout, transport=mock_transport(handler)
    )
    nc = NamecheapClient(config, client=client)

    with pytest.raises(ValueError, match="Invalid Namecheap response"):
        nc.call("test.command")


# ---------------------------------------------------
# PARAM MERGING
# ---------------------------------------------------


def test_params_merging(config):
    def handler(request: httpx.Request):
        params = request.url.params

        # custom param
        assert params["foo"] == "bar"

        # required params
        assert params["ApiUser"] == "testuser"
        assert params["Command"] == "test.command"

        return httpx.Response(200, text=VALID_XML)

    client = httpx.Client(
        base_url=config.endpoint, timeout=config.timeout, transport=mock_transport(handler)
    )
    nc = NamecheapClient(config, client=client)

    nc.call("test.command", {"foo": "bar"})


# ---------------------------------------------------
# EMPTY PARAMS
# ---------------------------------------------------


def test_call_without_params(config):
    def handler(request: httpx.Request):
        params = request.url.params

        assert params["Command"] == "test.command"
        return httpx.Response(200, text=VALID_XML)

    client = httpx.Client(
        base_url=config.endpoint, timeout=config.timeout, transport=mock_transport(handler)
    )
    nc = NamecheapClient(config, client=client)

    response = nc.call("test.command")

    assert response["Status"] == "OK"


# ---------------------------------------------------
# CLOSE CLIENT
# ---------------------------------------------------


def test_close(config):
    client = httpx.Client()
    nc = NamecheapClient(config, client=client)

    nc.close()

    assert client.is_closed is True
