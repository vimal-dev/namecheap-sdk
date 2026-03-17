from pydantic import BaseModel, computed_field, Field, IPvAnyAddress


class NamecheapConfig(BaseModel):
    api_user: str = Field(..., min_length=1)
    api_key: str = Field(..., min_length=1)
    username: str = Field(..., min_length=1)
    client_ip: IPvAnyAddress = Field(..., description="Client IP address")
    sandbox: bool = Field(default=False)
    timeout: int = Field(default=30, gt=0)

    @computed_field
    @property
    def endpoint(self) -> str:
        if self.sandbox:
            return "https://api.sandbox.namecheap.com/xml.response"
        return "https://api.namecheap.com/xml.response"