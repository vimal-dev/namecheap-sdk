from pprint import pp

from app.dependencies import get_namecheap_ssl_client
from namecheap_sdk.schemas.request.ssl import GetSSLInfoRequest


def get_ssl_info():
    # Example: Get information about an SSL certificate
    ssl_client = get_namecheap_ssl_client()
    request = GetSSLInfoRequest(
        CertificateID=335617341, Returncertificate=True, Returntype="Individual"
    )
    response = ssl_client.get_info(request)
    return response


if __name__ == "__main__":
    result = get_ssl_info()
    pp(result)
