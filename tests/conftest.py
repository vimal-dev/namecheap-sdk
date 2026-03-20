import pytest

from namecheap_sdk.schemas.config import NamecheapConfig


@pytest.fixture
def config():
    return NamecheapConfig(
        api_user="testuser",
        api_key="testkey",
        username="testuser",
        client_ip="127.0.0.1",
        sandbox=True,
    )


@pytest.fixture
def mock_success_xml():
    return """
    <ApiResponse Status="OK">
        <CommandResponse>
            <Test>Success</Test>
        </CommandResponse>
    </ApiResponse>
    """
