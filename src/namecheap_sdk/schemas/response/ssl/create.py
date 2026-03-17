from typing import Optional

from pydantic import BaseModel, Field

from namecheap_sdk.schemas.response.ssl.ssl_certificate import SSLCertificate

class SSLCreateResult(BaseModel):
    is_success: bool = Field(..., alias="IsSuccess")
    order_id: int = Field(..., alias="OrderId")
    transaction_id: int = Field(..., alias="TransactionId")
    charged_amount: str = Field(..., alias="ChargedAmount")

    ssl_certificate: Optional[SSLCertificate] = Field(
        None,
        alias="SSLCertificate"
    )
