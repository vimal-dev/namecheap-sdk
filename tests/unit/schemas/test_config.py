from namecheap_sdk.schemas.config import NamecheapConfig
from pydantic import ValidationError
import pytest


def test_valid_config(config):
    assert config.api_user == "testuser"
    assert config.api_key == "testkey"
    assert config.username == "testuser"
    assert str(config.client_ip) == "127.0.0.1"


def test_config_defaults():
    cfg = NamecheapConfig(
        api_user="u",
        api_key="k",
        username="u",
        client_ip="127.0.0.1",
    )
    assert cfg.sandbox is False
    assert cfg.timeout == 30


def test_config_sandbox_endpoint(config):
    assert config.sandbox is True
    assert config.endpoint == "https://api.sandbox.namecheap.com/xml.response"

def test_invalid_ip():
    with pytest.raises(ValidationError):
        NamecheapConfig(
            api_user="user",
            api_key="key",
            username="user",
            client_ip="invalid-ip",
        )


def test_config_production_endpoint():
    cfg = NamecheapConfig(
        api_user="u",
        api_key="k",
        username="u",
        client_ip="127.0.0.1",
    )
    assert cfg.sandbox is False
    assert cfg.endpoint == "https://api.namecheap.com/xml.response"


def test_invalid_timeout():
    from pydantic import ValidationError

    with pytest.raises(ValidationError):
        NamecheapConfig(
            api_user="user",
            api_key="key",
            username="user",
            client_ip="127.0.0.1",
            timeout="abc",
        )

def test_config_missing_fields():
    from pydantic import ValidationError
    with pytest.raises(ValidationError):
        NamecheapConfig()


def test_config_serialization(config):
    data = config.model_dump()
    assert "endpoint" in data
    assert data["endpoint"].startswith("https://")

def test_endpoint_changes_with_sandbox():
    config = NamecheapConfig(
        api_user="user",
        api_key="key",
        username="user",
        client_ip="127.0.0.1",
    )

    assert config.endpoint == "https://api.namecheap.com/xml.response"
    config.sandbox = True
    assert config.endpoint == "https://api.sandbox.namecheap.com/xml.response"

@pytest.mark.parametrize("field,value", [
    ("api_user", 123),
    ("api_key", 123),
    ("username", 123),
    ("client_ip", "123"),
    ("sandbox", "123"),
    ("timeout", "-10"),
])
def test_invalid_types(field, value):
    data = {
        "api_user": "user",
        "api_key": "key",
        "username": "user",
        "client_ip": "127.0.0.1",
        field: value,
    }

    with pytest.raises(ValidationError):
        NamecheapConfig(**data)


@pytest.mark.parametrize("field", [
    "api_user",
    "api_key",
    "username",
    "client_ip",
])
def test_missing_required_fields(field):
    data = {
        "api_user": "user",
        "api_key": "key",
        "username": "user",
        "client_ip": "127.0.0.1",
    }

    data.pop(field)

    with pytest.raises(ValidationError):
        NamecheapConfig(**data)