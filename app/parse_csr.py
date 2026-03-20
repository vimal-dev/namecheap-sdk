
from pprint import pp

from app.dependencies import get_namecheap_ssl_client
from namecheap_sdk.schemas.request.ssl import ParseCSRRequest, CertificateProductEnum

def parse_csr():
    '''
    Parse the provided CSR and return the details.
    '''
    ssl_client = get_namecheap_ssl_client()
    request = ParseCSRRequest(
        CertificateType=CertificateProductEnum.POSITIVE_SSL, 
        csr="""-----BEGIN CERTIFICATE REQUEST-----
MIIFGzCCAwMCAQAwgaUxEjAQBgNVBAgMCVJhamFzdGhhbjEsMCoGA1UECgwjQ2xv
dWRUZWNodGlxIFRlY2hub2xvZ2llcyBQdnQuIGx0ZC4xDzANBgNVBAcMBkphaXB1
cjEmMCQGCSqGSIb3DQEJARYXcmFqZXNoQGNsb3VkdGVjaHRpcS5jb20xGzAZBgNV
BAMMEiouY2xvdWR0ZWNodGlxLmNvbTELMAkGA1UECwwCSVQwggIiMA0GCSqGSIb3
DQEBAQUAA4ICDwAwggIKAoICAQDMEKzEj0ITIzb/mPJRDj+rx0dqilRdmtJx7LuL
a9DanA+wDQpl0CWycLUgUf6zVJw7OECOk6eRK2I5lDSV4EqY1R1KheY7cjU0jIx8
BeQ50mqiEIo4r6H4NK59juq23w+Mm/sDFEH9JWnbKGYPMORzoCkDdKphHG51/J0W
rXTDa20pxvN70c+gPsUstU9rpeEIwjY2DlxYNi2yjlOZFajWHiHyaj5/pc9ONi/p
HRpe17d96adGqSK2jVH/U6vZcreaUNWUIUB4RYSE7WlyQtPXF0F3bL7MIvPdDJd9
KXGshMBmRl91jZ/GiW/fhmwQBXT3OQhBMV9uQCLQMfZlyjPsm8Bh9E+xKQqgKfd8
SG8BmXqkg8G9OJj/DM+S6mlrf5+YrPdMbaRbJu8vyh/oNjl+6j51GujYY23X/+2h
eGun65Y9H+QlkyStk/KkYJGcABYUiPYA2q7zVR8zultJNCE3qT845o0kZ4FxSZyz
HuDei2QY66FRGn/LaMt02Fgb7GL3l6fTzNTYpUNCneguVwDmDjmnzMsVXIXNu8cS
3TIhy2Yv3cramg8mPuFFqoJD6Qz+4LlahP0RE4RuZXUO9zNUgYpHrR9au8k+FD5I
yhHflwcEskURyfmvEluDfihLlbR0r9VTGogAgCNvtLzW2k30P/rz8/eBAnSUP4WO
Qi+IyQIDAQABoDAwLgYJKoZIhvcNAQkOMSEwHzAdBgNVHREEFjAUghIqLmNsb3Vk
dGVjaHRpcS5jb20wDQYJKoZIhvcNAQELBQADggIBAIj2SkYSkPTPe1a9ZBYloJDM
BOF3/nWfYoaJVP9kJVCd3GPyMe1rHpFll5SK1IGlkxrOTqVCvKgniyyzqQHbab/0
VXAzTau3gRBftYBq+YgKuVJMGQS/Ixi3uR00FZlXmzJDPL3kcBmBat1WHnP0f/eC
xRjn4RTr52kgRpn8cv6YR0zygR9PEDbthhK4cJLmJLDMCefxFpqbfLu3HDliIEGc
2MOA7vDHRsMatbqu0lhW0Kxwaso6/5xlsImpP8GZ+VaRaqhffaQsFYtyuiEq/8fu
29z5QwYOP0yjePjJ7X5vBzANFUvBKdoGIGzxXSkVGZsri6gUAK3WS7WAIM+zXCeJ
QaenHXzdQoDMYispYjsSAFJnjuT4xznpBnDxRwtlSuExirOmBBRAqBXzdxX2DpsX
SF4iTZdaJj50b12JaSizwJqSRhMEGzunZdomyAo8muGdc/o6P/C9VYZrvDgIfC63
u0WSMNN+o9aF7APt9ixnzSxO+SZHq+3QR5tJzDv6livj6eqzEFzMutS4zvYo3Vo3
VTj1wbc1eZMqrI5sSb0EEXIpS+WHW8BVIESkmm9oL/gcjzSccv66oVe6bCpk7EWy
qXGa7A7WtX3PKGoCReZU5Vbl/xjN+76oFPQFwKmEmKZyJqVh3M7c7q0FVqCJsD6u
TYdYYkW8VQ0glbyjzsF1
-----END CERTIFICATE REQUEST-----"""
    )
    response = ssl_client.parse_csr(request)
    return response


if __name__ == "__main__":
    result = parse_csr()
    pp(result)