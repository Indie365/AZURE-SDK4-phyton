# coding=utf-8
# pylint: disable=too-many-lines
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import Any, List, Optional, TYPE_CHECKING

from ... import _serialization

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from .. import models as _models


class Resource(_serialization.Model):
    """Describes an Azure resource.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar id: Resource Id.
    :vartype id: str
    :ivar name: Resource name.
    :vartype name: str
    :ivar type: Resource type.
    :vartype type: str
    """

    _validation = {
        "id": {"readonly": True},
        "name": {"readonly": True},
        "type": {"readonly": True},
    }

    _attribute_map = {
        "id": {"key": "id", "type": "str"},
        "name": {"key": "name", "type": "str"},
        "type": {"key": "type", "type": "str"},
    }

    def __init__(self, **kwargs: Any) -> None:
        """ """
        super().__init__(**kwargs)
        self.id = None
        self.name = None
        self.type = None


class Setting(Resource):
    """The kind of the security setting.

    You probably want to use the sub-classes and not this class directly. Known sub-classes are:
    AlertSyncSettings, DataExportSettings

    Variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: Resource Id.
    :vartype id: str
    :ivar name: Resource name.
    :vartype name: str
    :ivar type: Resource type.
    :vartype type: str
    :ivar kind: the kind of the settings string. Required. Known values are: "DataExportSettings",
     "AlertSuppressionSetting", and "AlertSyncSettings".
    :vartype kind: str or ~azure.mgmt.security.v2022_05_01.models.SettingKind
    """

    _validation = {
        "id": {"readonly": True},
        "name": {"readonly": True},
        "type": {"readonly": True},
        "kind": {"required": True},
    }

    _attribute_map = {
        "id": {"key": "id", "type": "str"},
        "name": {"key": "name", "type": "str"},
        "type": {"key": "type", "type": "str"},
        "kind": {"key": "kind", "type": "str"},
    }

    _subtype_map = {"kind": {"AlertSyncSettings": "AlertSyncSettings", "DataExportSettings": "DataExportSettings"}}

    def __init__(self, **kwargs: Any) -> None:
        """ """
        super().__init__(**kwargs)
        self.kind: Optional[str] = None


class AlertSyncSettings(Setting):
    """Represents an alert sync setting.

    Variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: Resource Id.
    :vartype id: str
    :ivar name: Resource name.
    :vartype name: str
    :ivar type: Resource type.
    :vartype type: str
    :ivar kind: the kind of the settings string. Required. Known values are: "DataExportSettings",
     "AlertSuppressionSetting", and "AlertSyncSettings".
    :vartype kind: str or ~azure.mgmt.security.v2022_05_01.models.SettingKind
    :ivar enabled: Is the alert sync setting enabled.
    :vartype enabled: bool
    """

    _validation = {
        "id": {"readonly": True},
        "name": {"readonly": True},
        "type": {"readonly": True},
        "kind": {"required": True},
    }

    _attribute_map = {
        "id": {"key": "id", "type": "str"},
        "name": {"key": "name", "type": "str"},
        "type": {"key": "type", "type": "str"},
        "kind": {"key": "kind", "type": "str"},
        "enabled": {"key": "properties.enabled", "type": "bool"},
    }

    def __init__(self, *, enabled: Optional[bool] = None, **kwargs: Any) -> None:
        """
        :keyword enabled: Is the alert sync setting enabled.
        :paramtype enabled: bool
        """
        super().__init__(**kwargs)
        self.kind: str = "AlertSyncSettings"
        self.enabled = enabled


class CloudErrorBody(_serialization.Model):
    """The error detail.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar code: The error code.
    :vartype code: str
    :ivar message: The error message.
    :vartype message: str
    :ivar target: The error target.
    :vartype target: str
    :ivar details: The error details.
    :vartype details: list[~azure.mgmt.security.v2022_05_01.models.CloudErrorBody]
    :ivar additional_info: The error additional info.
    :vartype additional_info: list[~azure.mgmt.security.v2022_05_01.models.ErrorAdditionalInfo]
    """

    _validation = {
        "code": {"readonly": True},
        "message": {"readonly": True},
        "target": {"readonly": True},
        "details": {"readonly": True},
        "additional_info": {"readonly": True},
    }

    _attribute_map = {
        "code": {"key": "code", "type": "str"},
        "message": {"key": "message", "type": "str"},
        "target": {"key": "target", "type": "str"},
        "details": {"key": "details", "type": "[CloudErrorBody]"},
        "additional_info": {"key": "additionalInfo", "type": "[ErrorAdditionalInfo]"},
    }

    def __init__(self, **kwargs: Any) -> None:
        """ """
        super().__init__(**kwargs)
        self.code = None
        self.message = None
        self.target = None
        self.details = None
        self.additional_info = None


class DataExportSettings(Setting):
    """Represents a data export setting.

    Variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: Resource Id.
    :vartype id: str
    :ivar name: Resource name.
    :vartype name: str
    :ivar type: Resource type.
    :vartype type: str
    :ivar kind: the kind of the settings string. Required. Known values are: "DataExportSettings",
     "AlertSuppressionSetting", and "AlertSyncSettings".
    :vartype kind: str or ~azure.mgmt.security.v2022_05_01.models.SettingKind
    :ivar enabled: Is the data export setting enabled.
    :vartype enabled: bool
    """

    _validation = {
        "id": {"readonly": True},
        "name": {"readonly": True},
        "type": {"readonly": True},
        "kind": {"required": True},
    }

    _attribute_map = {
        "id": {"key": "id", "type": "str"},
        "name": {"key": "name", "type": "str"},
        "type": {"key": "type", "type": "str"},
        "kind": {"key": "kind", "type": "str"},
        "enabled": {"key": "properties.enabled", "type": "bool"},
    }

    def __init__(self, *, enabled: Optional[bool] = None, **kwargs: Any) -> None:
        """
        :keyword enabled: Is the data export setting enabled.
        :paramtype enabled: bool
        """
        super().__init__(**kwargs)
        self.kind: str = "DataExportSettings"
        self.enabled = enabled


class ErrorAdditionalInfo(_serialization.Model):
    """The resource management error additional info.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar type: The additional info type.
    :vartype type: str
    :ivar info: The additional info.
    :vartype info: JSON
    """

    _validation = {
        "type": {"readonly": True},
        "info": {"readonly": True},
    }

    _attribute_map = {
        "type": {"key": "type", "type": "str"},
        "info": {"key": "info", "type": "object"},
    }

    def __init__(self, **kwargs: Any) -> None:
        """ """
        super().__init__(**kwargs)
        self.type = None
        self.info = None


class SettingsList(_serialization.Model):
    """Subscription settings list.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar value: The settings list.
    :vartype value: list[~azure.mgmt.security.v2022_05_01.models.Setting]
    :ivar next_link: The URI to fetch the next page.
    :vartype next_link: str
    """

    _validation = {
        "next_link": {"readonly": True},
    }

    _attribute_map = {
        "value": {"key": "value", "type": "[Setting]"},
        "next_link": {"key": "nextLink", "type": "str"},
    }

    def __init__(self, *, value: Optional[List["_models.Setting"]] = None, **kwargs: Any) -> None:
        """
        :keyword value: The settings list.
        :paramtype value: list[~azure.mgmt.security.v2022_05_01.models.Setting]
        """
        super().__init__(**kwargs)
        self.value = value
        self.next_link = None
