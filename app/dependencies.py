import os

from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file


def get_namecheap_ssl_client():
    from namecheap_sdk import Namecheap, NamecheapConfig

    config = NamecheapConfig(
        api_user=os.getenv("API_USER", "demo"),
        api_key=os.getenv("API_KEY", "demo"),
        username=os.getenv("API_USERNAME", "demo"),
        client_ip=os.getenv("CLIENT_IP", "127.0.0.1"),
        sandbox=os.getenv("SANDBOX", "false").lower() == "true",  # Set to False for production
    )
    namecheap_client = Namecheap(config)
    return namecheap_client.ssl
