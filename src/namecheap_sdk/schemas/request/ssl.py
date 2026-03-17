from enum import Enum
from pydantic import BaseModel, Field, PositiveInt, model_validator
from typing import Annotated, List, Literal, Optional, Union

from namecheap_sdk.schemas.base import APIRequest


class CertificateTypeEnum(str, Enum):
    INDIVIDUAL = "Individual"
    PKCS7 = "PKCS7"


class DCVMethodEnum(str, Enum):
    HTTP_CSR_HASH = "HTTP_CSR_HASH"
    CNAME_CSR_HASH = "CNAME_CSR_HASH"


class CertificateProductEnum(str, Enum):
    POSITIVE_SSL = "PositiveSSL"
    ESSENTIAL_SSL = "EssentialSSL"
    INSTANT_SSL = "InstantSSL"
    INSTANT_SSL_PRO = "InstantSSL Pro"
    PREMIUM_SSL = "PremiumSSL"
    EV_SSL = "EV SSL"

    POSITIVE_SSL_WILDCARD = "PositiveSSL Wildcard"
    ESSENTIAL_SSL_WILDCARD = "EssentialSSL Wildcard"
    PREMIUM_SSL_WILDCARD = "PremiumSSL Wildcard"

    POSITIVE_SSL_MULTI_DOMAIN = "PositiveSSL Multi Domain"
    MULTI_DOMAIN_SSL = "Multi Domain SSL"
    UNIFIED_COMMUNICATIONS = "Unified Communications"
    EV_MULTI_DOMAIN_SSL = "EV Multi Domain SSL"


class CreateSSLRequest(APIRequest):
    years: PositiveInt = Field(
        ...,
        alias="Years",
        description="Number of years for the SSL certificate",
    )
    certificate_product: CertificateProductEnum = Field(
        ..., alias="Type", description="Type of SSL certificate to create"
    )
    sans_to_add: Optional[PositiveInt] = Field(
        None,
        alias="SANStoADD",
        description="Subject Alternative Names to add to the SSL certificate",
    )
    promotion_code: Optional[str] = Field(
        None,
        alias="PromotionCode",
        max_length=20,
        description="Promotion code for the SSL certificate",
    )


class RenewSSLRequest(APIRequest):
    certificate_id: PositiveInt = Field(
        ...,
        alias="CertificateID",
        description="Unique identifier for the SSL certificate",
    )
    years: PositiveInt = Field(
        ...,
        alias="Years",
        description="Number of years for the SSL certificate",
    )
    certificate_product: CertificateProductEnum = Field(
        ..., alias="SSLType", description="Type of SSL certificate to create"
    )
    promotion_code: Optional[str] = Field(
        None,
        alias="PromotionCode",
        max_length=20,
        description="Promotion code for the SSL certificate",
    )


class ListTypeEnum(str, Enum):
    ALL = "ALL"
    PROCESSING = "Processing"
    EMAIL_SENT = "EmailSent"
    TECHNICAL_PROBLEM = "TechnicalProblem"
    IN_PROGRESS = "InProgress"
    COMPLETED = "Completed"
    DEACTIVATED = "Deactivated"
    ACTIVE = "Active"
    CANCELLED = "Cancelled"
    NEW_PURCHASE = "NewPurchase"
    NEW_RENEWAL = "NewRenewal"


class SortBy(str, Enum):
    PURCHASE_DATE = "PURCHASEDATE"
    PURCHASE_DATE_DESC = "PURCHASEDATE_DESC"

    SSL_TYPE = "SSLTYPE"
    SSL_TYPE_DESC = "SSLTYPE_DESC"

    EXPIRE_DATE_TIME = "EXPIREDATETIME"
    EXPIRE_DATE_TIME_DESC = "EXPIREDATETIME_DESC"

    HOST_NAME = "Host_Name"
    HOST_NAME_DESC = "Host_Name_DESC"


class ListSSLRequest(APIRequest):
    list_type: Optional[ListTypeEnum] = Field(
        None,
        alias="ListType",
        description="Filter SSL certificates by their status",
    )
    page: Optional[PositiveInt] = Field(
        default=1, alias="Page", description="Page number for pagination"
    )
    page_size: Optional[PositiveInt] = Field(
        default=20,
        alias="PageSize",
        description="Total number of SSL certificates to display in a page. Minimum value is 10 and maximum value is 100.",
    )
    search: Optional[str] = Field(
        None,
        alias="SearchTerm",
        description="Search term for filtering SSL certificates",
    )
    sort_by: Optional[SortBy] = Field(
        None, alias="SortBy", description="Field to sort the SSL certificates by"
    )


class GetSSLInfoRequest(APIRequest):
    certificate_id: PositiveInt = Field(
        ...,
        alias="CertificateID",
        description="Unique identifier for the SSL certificate",
    )
    return_certificate: Optional[bool] = Field(
        None,
        alias="Returncertificate",
        description="A flag for returning certificate in response",
    )
    return_type: Optional[CertificateTypeEnum] = Field(
        CertificateTypeEnum.INDIVIDUAL,
        alias="Returntype",
        description="Type of returned certificate",
    )

    @model_validator(mode="after")
    def adjust_return_type(self):
        if not self.return_certificate:
            self.return_type = None
            self.return_certificate = None
        return self


class ParseCSRRequest(APIRequest):
    csr: str = Field(
        ...,
        alias="csr",
        description="Certificate Signing Request (CSR) for the SSL certificate",
    )
    certificate_product: Optional[CertificateProductEnum] = Field(
        None, alias="CertificateType", description="Type of SSL certificate to create"
    )


class ReSendApproverEmailRequest(APIRequest):
    certificate_id: PositiveInt = Field(
        ...,
        alias="CertificateID",
        description="Unique identifier for the SSL certificate",
    )


class ReSendFullfillmentEmailRequest(APIRequest):
    certificate_id: PositiveInt = Field(
        ...,
        alias="CertificateID",
        description="Unique identifier for the SSL certificate",
    )


class PurchaseMoreSANSRequest(APIRequest):
    certificate_id: PositiveInt = Field(
        ...,
        alias="CertificateID",
        description="Unique identifier for the SSL certificate",
    )
    sans_to_add: PositiveInt = Field(
        ...,
        alias="NumberOfSANSToAdd",
        description="Subject Alternative Names to add to the SSL certificate",
    )


class RevokeCertificateRequest(APIRequest):
    certificate_id: PositiveInt = Field(
        ...,
        alias="CertificateID",
        description="Unique identifier for the SSL certificate",
    )
    certificate_product: Optional[CertificateProductEnum] = Field(
        None, alias="CertificateType", description="Type of SSL certificate to create"
    )


class EditDCVRequest(APIRequest):
    certificate_id: PositiveInt = Field(
        ...,
        alias="CertificateID",
        description="Unique identifier for the SSL certificate",
    )
    dcv_method: Optional[str] = Field(
        None,
        alias="DCVMethod",
        description="Domain Control Validation method for the SSL certificate",
    )
    dns_names: Optional[List[str]] = Field(
        None, alias="DNSNames", description="List of DNS names for DCV"
    )
    dcv_methods: Optional[List[str]] = Field(
        None, alias="DCVMethods", description="List of DCV methods for each domain"
    )


class DCVMixin(BaseModel):

    approver_email: Optional[str] = Field(
        None,
        alias="ApproverEmail",
        description="Email address used for domain control validation"
    )

    dns_dc_validation: Optional[bool] = Field(
        None,
        alias="DNSDCValidation",
        description="Sets all domains in certificate requested domains to be validated through CNAME DCV method"
    )

    http_dc_validation: Optional[bool] = Field(
        None,
        alias="HTTPDCValidation",
        description="Sets all domains in certificate request to be validated through HTTP DCV. This method is not available for Wildcard certificates."
    )

    dns_names: Optional[List[str]] = Field(
        None,
        alias="DNSNames",
        description="List of domains for multi-domain certificates"
    )

    dns_approver_emails: Optional[List[str]] = Field(
        None,
        alias="DNSApproverEmails",
        description="Approver email or DCV method for each domain"
    )

    @model_validator(mode="after")
    def validate_dcv(self):

        if self.dns_names and not self.dns_approver_emails:
            raise ValueError(
                "DNSApproverEmails must be provided when DNSNames are used"
            )

        if self.dns_approver_emails and not self.dns_names:
            raise ValueError(
                "DNSNames must be provided when DNSApproverEmails are used"
            )

        if self.dns_names and self.dns_approver_emails:
            if len(self.dns_names) != len(self.dns_approver_emails):
                raise ValueError(
                    "DNSNames and DNSApproverEmails must have the same length"
                )

        return self


class BaseActivateCertificateRequest(APIRequest, DCVMixin):
    certificate_id: PositiveInt = Field(
        ...,
        alias="CertificateID",
        description="Unique identifier for the SSL certificate",
    )
    csr: str = Field(
        ...,
        alias="csr",
        description="Certificate Signing Request (CSR) for the SSL certificate",
    )
    admin_email: str = Field(
        ...,
        alias="AdminEmailAddress",
        description="Email address to send signed SSL certificate file to",
    )
    server_type: Optional[str] = Field(
        None,
        alias="WebServerType",
        description="Web server type for the SSL certificate",
    )
    unique_id: Optional[str] = Field(
        None,
        alias="UniqueValue",
        description="Unique identifier of SSL issue/reissue request. If not provided, it is created by the Namecheap system.",
    )


class ActivateReissueDVRequest(BaseActivateCertificateRequest):
    certificate_type: Literal["DV"]


class ActivateReissueOVRequest(BaseActivateCertificateRequest):
    certificate_type: Literal["OV"]

    organization_name: str = Field(..., alias="AdminOrganizationName", description="Organization name for the SSL certificate")
    organization_department: str | None = Field(None, alias="OrganizationDepartment", description="Organization department for the SSL certificate")


class ActivateReissueEVRequest(BaseActivateCertificateRequest):
    certificate_type: Literal["EV"]
    company_incorporation_country: str = Field(..., alias="CompanyIncorporationCountry", description="Country where the company is incorporated")
    company_registration_number: str = Field(..., alias="CompanyRegistrationNumber", description="Company registration number")
    organization_rep_first_name: str = Field(..., alias="OrganizationRepFirstName", description="First name of the organization representative")
    organization_rep_last_name: str = Field(..., alias="OrganizationRepLastName", description="Last name of the organization representative")
    organization_rep_phone: str = Field(..., alias="OrganizationRepPhone", description="Phone number of the organization representative")


ActivateCertificateRequest = Annotated[
    Union[
        ActivateReissueDVRequest,
        ActivateReissueOVRequest,
        ActivateReissueEVRequest
    ],
    Field(discriminator="certificate_type")
]
