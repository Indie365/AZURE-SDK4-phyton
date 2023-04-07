# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from enum import Enum
from azure.core import CaseInsensitiveEnumMeta


class BillingFrequency(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The frequency with which the cost gets billed."""

    MONTHLY = "monthly"


class PhoneNumberAssignmentType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Represents the assignment type of the offering."""

    PERSON = "person"
    APPLICATION = "application"


class PhoneNumberCapabilityType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Capability value for calling."""

    NONE = "none"
    INBOUND = "inbound"
    OUTBOUND = "outbound"
    INBOUND_OUTBOUND = "inbound+outbound"


class PhoneNumberOperationStatus(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Status of operation."""

    NOT_STARTED = "notStarted"
    RUNNING = "running"
    SUCCEEDED = "succeeded"
    FAILED = "failed"


class PhoneNumberOperationType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The type of operation, e.g. Search."""

    PURCHASE = "purchase"
    RELEASE_PHONE_NUMBER = "releasePhoneNumber"
    SEARCH = "search"
    UPDATE_PHONE_NUMBER_CAPABILITIES = "updatePhoneNumberCapabilities"


class PhoneNumberType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Represents the number type of the offering."""

    GEOGRAPHIC = "geographic"
    TOLL_FREE = "tollFree"
