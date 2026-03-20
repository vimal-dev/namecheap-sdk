from pprint import pp

from app.dependencies import get_namecheap_ssl_client
from namecheap_sdk.schemas.request.ssl import ListSSLRequest


def list_ssl():
    # Example: List SSL certificates
    ssl_client = get_namecheap_ssl_client()
    list_request = ListSSLRequest(ListType="ALL", SearchTerm="cloudtecht")
    response = ssl_client.list(list_request)
    return response


if __name__ == "__main__":
    result = list_ssl()
    pp(result)
