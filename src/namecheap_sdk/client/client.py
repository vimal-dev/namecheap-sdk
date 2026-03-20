from typing import Any, Dict, Optional
import xmltodict
import httpx

from namecheap_sdk.client.contract import ClientContract
from namecheap_sdk.schemas.config import NamecheapConfig


class NamecheapClient(ClientContract):
    def __init__(
        self,
        config: NamecheapConfig,
        client: Optional[httpx.Client] = None,
    ):
        self.config = config
        self.client = client or httpx.Client(
            base_url=config.endpoint,
            timeout=config.timeout,
        )

    # 🔹 Public API call
    def call(self, command: str, params: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        payload = self._build_params(command, params)
        return self._request(payload)

    # 🔹 Build params (isolated logic)
    def _build_params(self, command: str, params: Optional[Dict[str, Any]]) -> Dict[str, Any]:
        base_params = {
            "ApiUser": self.config.api_user,
            "ApiKey": self.config.api_key,
            "UserName": self.config.username,
            "ClientIp": str(self.config.client_ip),  # ensure string
            "Command": command,
        }

        if params:
            base_params.update(params)

        return base_params

    # 🔹 HTTP layer
    def _request(self, params: Dict[str, Any]) -> Dict[str, Any]:
        response = self.client.get("", params=params)
        response.raise_for_status()
        # print(f"Request params: {params}")  # Debug log
        # print(f"Raw response: {response.text}")  # Debug log
        return self._parse_xml(response.text)

    # 🔹 XML parsing (reusable)
    def _parse_xml(self, xml: str) -> Dict[str, Any]:
        try:
            data = xmltodict.parse(
                xml_input=xml,
                attr_prefix="",
                cdata_key="text",
            )
        except Exception as e:
            raise ValueError("Invalid XML response") from e

        if "ApiResponse" not in data:
            raise ValueError("Invalid Namecheap response format")
        # print(f"Parsed XML data: {data}")  # Debug log
        return data["ApiResponse"]

    def close(self):
        self.client.close()
