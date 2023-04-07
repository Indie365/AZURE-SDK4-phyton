# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from enum import Enum
from azure.core import CaseInsensitiveEnumMeta


class AccessProtocol(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """AccessProtocol."""

    SMB = "SMB"
    """Server Message Block protocol(SMB)."""
    NFS = "NFS"
    """Network File System protocol(NFS)."""


class AddressType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Type of address."""

    NONE = "None"
    """Address type not known."""
    RESIDENTIAL = "Residential"
    """Residential Address."""
    COMMERCIAL = "Commercial"
    """Commercial Address."""


class AddressValidationStatus(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The address validation status."""

    VALID = "Valid"
    """Address provided is valid."""
    INVALID = "Invalid"
    """Address provided is invalid or not supported."""
    AMBIGUOUS = "Ambiguous"
    """Address provided is ambiguous, please choose one of the alternate addresses returned."""


class ClassDiscriminator(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Indicates the type of job details."""

    DATA_BOX = "DataBox"
    """Data Box orders."""
    DATA_BOX_DISK = "DataBoxDisk"
    """Data Box Disk orders."""
    DATA_BOX_HEAVY = "DataBoxHeavy"
    """Data Box Heavy orders."""
    DATA_BOX_CUSTOMER_DISK = "DataBoxCustomerDisk"
    """Data Box Customer Disk orders."""


class CopyStatus(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The Status of the copy."""

    NOT_STARTED = "NotStarted"
    """Data copy hasn't started yet."""
    IN_PROGRESS = "InProgress"
    """Data copy is in progress."""
    COMPLETED = "Completed"
    """Data copy completed."""
    COMPLETED_WITH_ERRORS = "CompletedWithErrors"
    """Data copy completed with errors."""
    FAILED = "Failed"
    """Data copy failed. No data was copied."""
    NOT_RETURNED = "NotReturned"
    """No copy triggered as device was not returned."""
    HARDWARE_ERROR = "HardwareError"
    """The Device has hit hardware issues."""
    DEVICE_FORMATTED = "DeviceFormatted"
    """Data copy failed. The Device was formatted by user."""
    DEVICE_METADATA_MODIFIED = "DeviceMetadataModified"
    """Data copy failed. Device metadata was modified by user."""
    STORAGE_ACCOUNT_NOT_ACCESSIBLE = "StorageAccountNotAccessible"
    """Data copy failed. Storage Account was not accessible during copy."""
    UNSUPPORTED_DATA = "UnsupportedData"
    """Data copy failed. The Device data content is not supported."""
    DRIVE_NOT_RECEIVED = "DriveNotReceived"
    """No copy triggered as device was not received."""
    UNSUPPORTED_DRIVE = "UnsupportedDrive"
    """No copy triggered as device type is not supported."""
    OTHER_SERVICE_ERROR = "OtherServiceError"
    """Copy failed due to service error."""
    OTHER_USER_ERROR = "OtherUserError"
    """Copy failed due to user error."""
    DRIVE_NOT_DETECTED = "DriveNotDetected"
    """Copy failed due to disk detection error."""
    DRIVE_CORRUPTED = "DriveCorrupted"
    """Copy failed due to corrupted drive."""
    METADATA_FILES_MODIFIED_OR_REMOVED = "MetadataFilesModifiedOrRemoved"
    """Copy failed due to modified  or removed metadata files."""


class CustomerResolutionCode(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """CustomerResolutionCode."""

    NONE = "None"
    """No Resolution Yet"""
    MOVE_TO_CLEAN_UP_DEVICE = "MoveToCleanUpDevice"
    """Clean the device"""
    RESUME = "Resume"
    """Resume the job to same stage"""


class DataAccountType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Type of the account."""

    STORAGE_ACCOUNT = "StorageAccount"
    """Storage Accounts ."""
    MANAGED_DISK = "ManagedDisk"
    """Azure Managed disk storage."""


class DatacenterAddressType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Data center address type."""

    DATACENTER_ADDRESS_LOCATION = "DatacenterAddressLocation"
    """Data center address location."""
    DATACENTER_ADDRESS_INSTRUCTION = "DatacenterAddressInstruction"
    """Data center address instruction."""


class DataCenterCode(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """DataCenter code."""

    INVALID = "Invalid"
    BY2 = "BY2"
    BY1 = "BY1"
    ORK70 = "ORK70"
    AM2 = "AM2"
    AMS20 = "AMS20"
    BY21 = "BY21"
    BY24 = "BY24"
    MWH01 = "MWH01"
    AMS06 = "AMS06"
    SSE90 = "SSE90"
    SYD03 = "SYD03"
    SYD23 = "SYD23"
    CBR20 = "CBR20"
    YTO20 = "YTO20"
    CWL20 = "CWL20"
    LON24 = "LON24"
    BOM01 = "BOM01"
    BL20 = "BL20"
    BL7 = "BL7"
    SEL20 = "SEL20"
    TYO01 = "TYO01"
    BN1 = "BN1"
    SN5 = "SN5"
    CYS04 = "CYS04"
    TYO22 = "TYO22"
    YTO21 = "YTO21"
    YQB20 = "YQB20"
    FRA22 = "FRA22"
    MAA01 = "MAA01"
    CPQ02 = "CPQ02"
    CPQ20 = "CPQ20"
    SIN20 = "SIN20"
    HKG20 = "HKG20"
    SG2 = "SG2"
    MEL23 = "MEL23"
    SEL21 = "SEL21"
    OSA20 = "OSA20"
    SHA03 = "SHA03"
    BJB = "BJB"
    JNB22 = "JNB22"
    JNB21 = "JNB21"
    MNZ21 = "MNZ21"
    SN8 = "SN8"
    AUH20 = "AUH20"
    ZRH20 = "ZRH20"
    PUS20 = "PUS20"
    AD_HOC = "AdHoc"
    CH1 = "CH1"
    DSM05 = "DSM05"
    BN7 = "BN7"
    SN6 = "SN6"
    PAR22 = "PAR22"


class DoubleEncryption(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Defines secondary layer of software-based encryption enablement."""

    ENABLED = "Enabled"
    """Software-based encryption is enabled."""
    DISABLED = "Disabled"
    """Software-based encryption is disabled."""


class FilterFileType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Type of the filter file."""

    AZURE_BLOB = "AzureBlob"
    """Filter file is of the type AzureBlob."""
    AZURE_FILE = "AzureFile"
    """Filter file is of the type AzureFiles."""


class JobDeliveryType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Delivery type of Job."""

    NON_SCHEDULED = "NonScheduled"
    """Non Scheduled job."""
    SCHEDULED = "Scheduled"
    """Scheduled job."""


class KekType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Type of encryption key used for key encryption."""

    MICROSOFT_MANAGED = "MicrosoftManaged"
    """Key encryption key is managed by Microsoft."""
    CUSTOMER_MANAGED = "CustomerManaged"
    """Key encryption key is managed by the Customer."""


class LogCollectionLevel(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Level of the logs to be collected."""

    ERROR = "Error"
    """Only Errors will be collected in the logs."""
    VERBOSE = "Verbose"
    """Verbose logging (includes Errors, CRC, size information and others)."""


class NotificationStageName(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Name of the stage."""

    DEVICE_PREPARED = "DevicePrepared"
    """Notification at device prepared stage."""
    DISPATCHED = "Dispatched"
    """Notification at device dispatched stage."""
    DELIVERED = "Delivered"
    """Notification at device delivered stage."""
    PICKED_UP = "PickedUp"
    """Notification at device picked up from user stage."""
    AT_AZURE_DC = "AtAzureDC"
    """Notification at device received at Azure datacenter stage."""
    DATA_COPY = "DataCopy"
    """Notification at data copy started stage."""
    CREATED = "Created"
    """Notification at job created stage."""
    SHIPPED_TO_CUSTOMER = "ShippedToCustomer"
    """Notification at shipped devices to customer stage."""


class OverallValidationStatus(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Overall validation status."""

    ALL_VALID_TO_PROCEED = "AllValidToProceed"
    """Every input request is valid."""
    INPUTS_REVISIT_REQUIRED = "InputsRevisitRequired"
    """Some input requests are not valid."""
    CERTAIN_INPUT_VALIDATIONS_SKIPPED = "CertainInputValidationsSkipped"
    """Certain input validations skipped."""


class ShareDestinationFormatType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Type of the share."""

    UNKNOWN_TYPE = "UnknownType"
    """Unknown format."""
    HCS = "HCS"
    """Storsimple data format."""
    BLOCK_BLOB = "BlockBlob"
    """Azure storage block blob format."""
    PAGE_BLOB = "PageBlob"
    """Azure storage page blob format."""
    AZURE_FILE = "AzureFile"
    """Azure storage file format."""
    MANAGED_DISK = "ManagedDisk"
    """Azure Compute Disk."""


class SkuDisabledReason(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Reason why the Sku is disabled."""

    NONE = "None"
    """SKU is not disabled."""
    COUNTRY = "Country"
    """SKU is not available in the requested country."""
    REGION = "Region"
    """SKU is not available to push data to the requested Azure region."""
    FEATURE = "Feature"
    """Required features are not enabled for the SKU."""
    OFFER_TYPE = "OfferType"
    """Subscription does not have required offer types for the SKU."""
    NO_SUBSCRIPTION_INFO = "NoSubscriptionInfo"
    """Subscription has not registered to Microsoft.DataBox and Service does not have the subscription
    #: notification."""


class SkuName(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """SkuName."""

    DATA_BOX = "DataBox"
    """Data Box."""
    DATA_BOX_DISK = "DataBoxDisk"
    """Data Box Disk."""
    DATA_BOX_HEAVY = "DataBoxHeavy"
    """Data Box Heavy."""
    DATA_BOX_CUSTOMER_DISK = "DataBoxCustomerDisk"
    """Data Box Customer Disk"""


class StageName(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Name of the stage which is in progress."""

    DEVICE_ORDERED = "DeviceOrdered"
    """An order has been created."""
    DEVICE_PREPARED = "DevicePrepared"
    """A device has been prepared for the order."""
    DISPATCHED = "Dispatched"
    """Device has been dispatched to the user of the order."""
    DELIVERED = "Delivered"
    """Device has been delivered to the user of the order."""
    PICKED_UP = "PickedUp"
    """Device has been picked up from user and in transit to Azure datacenter."""
    AT_AZURE_DC = "AtAzureDC"
    """Device has been received at Azure datacenter from the user."""
    DATA_COPY = "DataCopy"
    """Data copy from the device at Azure datacenter."""
    COMPLETED = "Completed"
    """Order has completed."""
    COMPLETED_WITH_ERRORS = "CompletedWithErrors"
    """Order has completed with errors."""
    CANCELLED = "Cancelled"
    """Order has been cancelled."""
    FAILED_ISSUE_REPORTED_AT_CUSTOMER = "Failed_IssueReportedAtCustomer"
    """Order has failed due to issue reported by user."""
    FAILED_ISSUE_DETECTED_AT_AZURE_DC = "Failed_IssueDetectedAtAzureDC"
    """Order has failed due to issue detected at Azure datacenter."""
    ABORTED = "Aborted"
    """Order has been aborted."""
    COMPLETED_WITH_WARNINGS = "CompletedWithWarnings"
    """Order has completed with warnings."""
    READY_TO_DISPATCH_FROM_AZURE_DC = "ReadyToDispatchFromAzureDC"
    """Device is ready to be handed to customer from Azure DC."""
    READY_TO_RECEIVE_AT_AZURE_DC = "ReadyToReceiveAtAzureDC"
    """Device can be dropped off at Azure DC."""
    CREATED = "Created"
    """Job created by the customer."""
    SHIPPED_TO_AZURE_DC = "ShippedToAzureDC"
    """User shipped the device to AzureDC."""
    AWAITING_SHIPMENT_DETAILS = "AwaitingShipmentDetails"
    """Awaiting shipment details of device from customer."""
    PREPARING_TO_SHIP_FROM_AZURE_DC = "PreparingToShipFromAzureDC"
    """Preparing the device to ship to customer."""
    SHIPPED_TO_CUSTOMER = "ShippedToCustomer"
    """Shipped the device to customer."""


class StageStatus(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Status of the job stage."""

    NONE = "None"
    """No status available yet."""
    IN_PROGRESS = "InProgress"
    """Stage is in progress."""
    SUCCEEDED = "Succeeded"
    """Stage has succeeded."""
    FAILED = "Failed"
    """Stage has failed."""
    CANCELLED = "Cancelled"
    """Stage has been cancelled."""
    CANCELLING = "Cancelling"
    """Stage is cancelling."""
    SUCCEEDED_WITH_ERRORS = "SucceededWithErrors"
    """Stage has succeeded with errors."""
    WAITING_FOR_CUSTOMER_ACTION = "WaitingForCustomerAction"
    """Stage is stuck until customer takes some action."""
    SUCCEEDED_WITH_WARNINGS = "SucceededWithWarnings"
    """Stage has succeeded with warnings."""
    WAITING_FOR_CUSTOMER_ACTION_FOR_KEK = "WaitingForCustomerActionForKek"
    """Stage is waiting for customer action for kek action items."""
    WAITING_FOR_CUSTOMER_ACTION_FOR_CLEAN_UP = "WaitingForCustomerActionForCleanUp"
    """Stage is waiting for customer action for clean up."""
    CUSTOMER_ACTION_PERFORMED_FOR_CLEAN_UP = "CustomerActionPerformedForCleanUp"
    """Stage has performed customer action for clean up."""


class TransferConfigurationType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Type of the configuration for transfer."""

    TRANSFER_ALL = "TransferAll"
    """Transfer all the data."""
    TRANSFER_USING_FILTER = "TransferUsingFilter"
    """Transfer using filter."""


class TransferType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Type of the transfer."""

    IMPORT_TO_AZURE = "ImportToAzure"
    """Import data to azure."""
    EXPORT_FROM_AZURE = "ExportFromAzure"
    """Export data from azure."""


class TransportShipmentTypes(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Transport Shipment Type supported for given region."""

    CUSTOMER_MANAGED = "CustomerManaged"
    """Shipment Logistics is handled by the customer."""
    MICROSOFT_MANAGED = "MicrosoftManaged"
    """Shipment Logistics is handled by Microsoft."""


class ValidationInputDiscriminator(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Identifies the type of validation request."""

    VALIDATE_ADDRESS = "ValidateAddress"
    """Identify request and response of address validation."""
    VALIDATE_SUBSCRIPTION_IS_ALLOWED_TO_CREATE_JOB = "ValidateSubscriptionIsAllowedToCreateJob"
    """Identify request and response for validation of subscription permission to create job."""
    VALIDATE_PREFERENCES = "ValidatePreferences"
    """Identify request and response of preference validation."""
    VALIDATE_CREATE_ORDER_LIMIT = "ValidateCreateOrderLimit"
    """Identify request and response of create order limit for subscription validation."""
    VALIDATE_SKU_AVAILABILITY = "ValidateSkuAvailability"
    """Identify request and response of active job limit for sku availability."""
    VALIDATE_DATA_TRANSFER_DETAILS = "ValidateDataTransferDetails"
    """Identify request and response of data transfer details validation."""


class ValidationStatus(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Create order limit validation status."""

    VALID = "Valid"
    """Validation is successful"""
    INVALID = "Invalid"
    """Validation is not successful"""
    SKIPPED = "Skipped"
    """Validation is skipped"""
