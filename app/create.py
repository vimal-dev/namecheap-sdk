from pprint import pp

from app.dependencies import get_namecheap_ssl_client
from namecheap_sdk.schemas.request.ssl import CreateSSLRequest, CertificateProductEnum


def create_ssl():
    # Example: Create a new SSL certificate
    ssl_client = get_namecheap_ssl_client()
    create_request = CreateSSLRequest(Type=CertificateProductEnum.POSITIVE_SSL, Years=1)
    response = ssl_client.create(create_request)
    return response


if __name__ == "__main__":
    result = create_ssl()
    pp(result)
