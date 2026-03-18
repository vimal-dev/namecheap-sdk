import pytest

from namecheap_sdk.schemas.base import APIResponse

# ---------------------------------------------------
# Test APIResponse Schema
# ---------------------------------------------------
def test_config_missing_fields():
    from pydantic import ValidationError

    with pytest.raises(ValidationError):
        APIResponse()

# ---------------------------------------------------
# Test APIResponse Schema with various status and error configurations
# ---------------------------------------------------
def test_config_ok_response():
    response = APIResponse(
        Status="OK",
        RequestedCommand="TestCommand",
        Server="TestServer",
        ExecutionTime="0.123",
    )
    assert response.is_ok
    assert not response.is_error
    assert response.error_messages() == []


def test_config_error_response():
    response = APIResponse(
        Status="ERROR",
        RequestedCommand="TestCommand",
        Server="TestServer",
        ExecutionTime="0.123",
        Errors={"Error": {"Number": "123", "text": "Test error message"}},
    )
    assert not response.is_ok
    assert response.is_error
    assert response.error_messages() == ["Test error message"]


def test_config_error_response_multiple():
    response = APIResponse(
        Status="ERROR",
        RequestedCommand="TestCommand",
        Server="TestServer",
        ExecutionTime="0.123",
        Errors={"Error": [{"Number": "123", "text": "Test error message"}, {"Number": "456", "text": "Another error message"}]},
    )
    assert not response.is_ok
    assert response.is_error
    assert response.error_messages() == ["Test error message", "Another error message"]
