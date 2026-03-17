

from namecheap_sdk.schemas.config import NamecheapConfig
from namecheap_sdk.client.client import NamecheapClient
from namecheap_sdk.services.ssl import SSLService


class Namecheap:
    
    def __init__(self, config: NamecheapConfig):
        self.config = config
        self.client = NamecheapClient(config)
        self.ssl = SSLService(self.client)