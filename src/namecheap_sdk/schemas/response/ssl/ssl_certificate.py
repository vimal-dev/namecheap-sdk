from pydantic import BaseModel, Field
from typing import Optional


class SSLCertificate(BaseModel):
    certificate_id: int = Field(..., alias="CertificateID")
    created: str = Field(..., alias="Created")
    ssl_type: str = Field(..., alias="SSLType")
    years: int = Field(..., alias="Years")
    status: str = Field(..., alias="Status")