from typing import Dict

from namecheap_sdk.client.client import NamecheapClient
from namecheap_sdk.schemas.base import APIResponse
from namecheap_sdk.schemas.request.ssl import (
    ActivateCertificateRequest,
    CreateSSLRequest,
    EditDCVRequest,
    GetSSLInfoRequest,
    ListSSLRequest,
    ParseCSRRequest,
    PurchaseMoreSANSRequest,
    ReSendApproverEmailRequest,
    ReSendFullfillmentEmailRequest,
    RenewSSLRequest,
    RevokeCertificateRequest,
)


class SSLService:
    """
    SSL Service:
        This service is used to execute the ssl related actions.
        create, list, get_info, activate, renew and reissue ssl certificates.
    """

    def __init__(self, client: NamecheapClient):
        self.client = client

    def create(self, payload: CreateSSLRequest) -> APIResponse[Dict]:
        """
        Create a new SSL certificate order.
        """
        result = self.client.call(
            "namecheap.ssl.create",
            payload.model_dump(by_alias=True, exclude_none=True),
        )
        return APIResponse[Dict](**result)

    def list(self, payload: ListSSLRequest) -> APIResponse[Dict]:
        """
        Get a list of SSL certificates associated with the account.
        """
        result = self.client.call(
            "namecheap.ssl.getList",
            payload.model_dump(by_alias=True, exclude_none=True),
        )
        return APIResponse[Dict](**result)

    def get_info(self, payload: GetSSLInfoRequest) -> APIResponse[Dict]:
        """
        Get detailed information about the requested SSL certificate.
        """
        result = self.client.call(
            "namecheap.ssl.getInfo",
            payload.model_dump(by_alias=True, exclude_none=True),
        )
        return APIResponse[Dict](**result)

    def parse_csr(self, payload: ParseCSRRequest) -> APIResponse[Dict]:
        """
        Parse the provided CSR and return the details.
        """
        result = self.client.call(
            "namecheap.ssl.parseCSR",
            payload.model_dump(by_alias=True, exclude_none=True),
        )
        return APIResponse[Dict](**result)

    def re_send_approver_email(self, payload: ReSendApproverEmailRequest) -> APIResponse[Dict]:
        """
        Resend the approver email for the requested SSL certificate.
        'Retries' HTTP/ DNS validation after the file is uploaded / CNAME record created.
        """
        result = self.client.call(
            "namecheap.ssl.resendApproverEmail",
            payload.model_dump(by_alias=True, exclude_none=True),
        )
        return APIResponse[Dict](**result)

    def re_send_fullfillment_email(
        self, payload: ReSendFullfillmentEmailRequest
    ) -> APIResponse[Dict]:
        """
        Resend the fullfillment email for the requested SSL certificate.
        """
        result = self.client.call(
            "namecheap.ssl.resendfulfillmentemail",
            payload.model_dump(by_alias=True, exclude_none=True),
        )
        return APIResponse[Dict](**result)

    def purchase_more_sans(self, payload: PurchaseMoreSANSRequest) -> APIResponse[Dict]:
        """
        Purchase more Subject Alternative Names for the requested SSL certificate.
        """
        result = self.client.call(
            "namecheap.ssl.purchasemoresans",
            payload.model_dump(by_alias=True, exclude_none=True),
        )
        return APIResponse[Dict](**result)

    def revoke_certificate(self, payload: RevokeCertificateRequest) -> APIResponse[Dict]:
        """
        Revoke the requested SSL certificate.
        """
        result = self.client.call(
            "namecheap.ssl.revokecertificate",
            payload.model_dump(by_alias=True, exclude_none=True),
        )
        return APIResponse[Dict](**result)

    def renew(self, payload: RenewSSLRequest) -> APIResponse[Dict]:
        """
        Renew an existing SSL certificate.
        """
        result = self.client.call(
            "namecheap.ssl.renew",
            payload.model_dump(by_alias=True, exclude_none=True),
        )
        return APIResponse[Dict](**result)

    def edit_dcv(self, payload: EditDCVRequest) -> APIResponse[Dict]:
        """
        Edit the Domain Control Validation (DCV) method for the requested SSL certificate.
        """
        result = self.client.call(
            "namecheap.ssl.editDCVMethod",
            payload.model_dump(by_alias=True, exclude_none=True),
        )
        return APIResponse[Dict](**result)

    def activate(self, payload: ActivateCertificateRequest) -> APIResponse[Dict]:
        """Activate the requested SSL certificate."""
        result = self.client.call(
            "namecheap.ssl.activate",
            payload.model_dump(by_alias=True, exclude_none=True),
        )
        return APIResponse[Dict](**result)

    def reissue(self, payload: ActivateCertificateRequest) -> APIResponse[Dict]:
        """Reissue the requested SSL certificate."""
        result = self.client.call(
            "namecheap.ssl.reissue",
            payload.model_dump(by_alias=True, exclude_none=True),
        )
        return APIResponse[Dict](**result)
