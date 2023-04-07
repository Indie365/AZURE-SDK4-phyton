# coding=utf-8
# pylint: disable=too-many-lines
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

import sys
from typing import Any, List, Optional, TYPE_CHECKING

from ... import _serialization

if sys.version_info >= (3, 9):
    from collections.abc import MutableMapping
else:
    from typing import MutableMapping  # type: ignore  # pylint: disable=ungrouped-imports

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from .. import models as _models
JSON = MutableMapping[str, Any]  # pylint: disable=unsubscriptable-object


class ClassicAdministrator(_serialization.Model):
    """Classic Administrators.

    :ivar id: The ID of the administrator.
    :vartype id: str
    :ivar name: The name of the administrator.
    :vartype name: str
    :ivar type: The type of the administrator.
    :vartype type: str
    :ivar email_address: The email address of the administrator.
    :vartype email_address: str
    :ivar role: The role of the administrator.
    :vartype role: str
    """

    _attribute_map = {
        "id": {"key": "id", "type": "str"},
        "name": {"key": "name", "type": "str"},
        "type": {"key": "type", "type": "str"},
        "email_address": {"key": "properties.emailAddress", "type": "str"},
        "role": {"key": "properties.role", "type": "str"},
    }

    def __init__(
        self,
        *,
        id: Optional[str] = None,  # pylint: disable=redefined-builtin
        name: Optional[str] = None,
        type: Optional[str] = None,
        email_address: Optional[str] = None,
        role: Optional[str] = None,
        **kwargs: Any
    ) -> None:
        """
        :keyword id: The ID of the administrator.
        :paramtype id: str
        :keyword name: The name of the administrator.
        :paramtype name: str
        :keyword type: The type of the administrator.
        :paramtype type: str
        :keyword email_address: The email address of the administrator.
        :paramtype email_address: str
        :keyword role: The role of the administrator.
        :paramtype role: str
        """
        super().__init__(**kwargs)
        self.id = id
        self.name = name
        self.type = type
        self.email_address = email_address
        self.role = role


class ClassicAdministratorListResult(_serialization.Model):
    """ClassicAdministrator list result information.

    :ivar value: An array of administrators.
    :vartype value: list[~azure.mgmt.authorization.v2015_07_01.models.ClassicAdministrator]
    :ivar next_link: The URL to use for getting the next set of results.
    :vartype next_link: str
    """

    _attribute_map = {
        "value": {"key": "value", "type": "[ClassicAdministrator]"},
        "next_link": {"key": "nextLink", "type": "str"},
    }

    def __init__(
        self,
        *,
        value: Optional[List["_models.ClassicAdministrator"]] = None,
        next_link: Optional[str] = None,
        **kwargs: Any
    ) -> None:
        """
        :keyword value: An array of administrators.
        :paramtype value: list[~azure.mgmt.authorization.v2015_07_01.models.ClassicAdministrator]
        :keyword next_link: The URL to use for getting the next set of results.
        :paramtype next_link: str
        """
        super().__init__(**kwargs)
        self.value = value
        self.next_link = next_link


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


class ErrorDetail(_serialization.Model):
    """The error detail.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar code: The error code.
    :vartype code: str
    :ivar message: The error message.
    :vartype message: str
    :ivar target: The error target.
    :vartype target: str
    :ivar details: The error details.
    :vartype details: list[~azure.mgmt.authorization.v2015_07_01.models.ErrorDetail]
    :ivar additional_info: The error additional info.
    :vartype additional_info:
     list[~azure.mgmt.authorization.v2015_07_01.models.ErrorAdditionalInfo]
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
        "details": {"key": "details", "type": "[ErrorDetail]"},
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


class ErrorResponse(_serialization.Model):
    """Common error response for all Azure Resource Manager APIs to return error details for failed
    operations. (This also follows the OData error response format.).

    :ivar error: The error object.
    :vartype error: ~azure.mgmt.authorization.v2015_07_01.models.ErrorDetail
    """

    _attribute_map = {
        "error": {"key": "error", "type": "ErrorDetail"},
    }

    def __init__(self, *, error: Optional["_models.ErrorDetail"] = None, **kwargs: Any) -> None:
        """
        :keyword error: The error object.
        :paramtype error: ~azure.mgmt.authorization.v2015_07_01.models.ErrorDetail
        """
        super().__init__(**kwargs)
        self.error = error


class Permission(_serialization.Model):
    """Role definition permissions.

    :ivar actions: Allowed actions.
    :vartype actions: list[str]
    :ivar not_actions: Denied actions.
    :vartype not_actions: list[str]
    """

    _attribute_map = {
        "actions": {"key": "actions", "type": "[str]"},
        "not_actions": {"key": "notActions", "type": "[str]"},
    }

    def __init__(
        self, *, actions: Optional[List[str]] = None, not_actions: Optional[List[str]] = None, **kwargs: Any
    ) -> None:
        """
        :keyword actions: Allowed actions.
        :paramtype actions: list[str]
        :keyword not_actions: Denied actions.
        :paramtype not_actions: list[str]
        """
        super().__init__(**kwargs)
        self.actions = actions
        self.not_actions = not_actions


class PermissionGetResult(_serialization.Model):
    """Permissions information.

    :ivar value: An array of permissions.
    :vartype value: list[~azure.mgmt.authorization.v2015_07_01.models.Permission]
    :ivar next_link: The URL to use for getting the next set of results.
    :vartype next_link: str
    """

    _attribute_map = {
        "value": {"key": "value", "type": "[Permission]"},
        "next_link": {"key": "nextLink", "type": "str"},
    }

    def __init__(
        self, *, value: Optional[List["_models.Permission"]] = None, next_link: Optional[str] = None, **kwargs: Any
    ) -> None:
        """
        :keyword value: An array of permissions.
        :paramtype value: list[~azure.mgmt.authorization.v2015_07_01.models.Permission]
        :keyword next_link: The URL to use for getting the next set of results.
        :paramtype next_link: str
        """
        super().__init__(**kwargs)
        self.value = value
        self.next_link = next_link


class ProviderOperation(_serialization.Model):
    """Operation.

    :ivar name: The operation name.
    :vartype name: str
    :ivar display_name: The operation display name.
    :vartype display_name: str
    :ivar description: The operation description.
    :vartype description: str
    :ivar origin: The operation origin.
    :vartype origin: str
    :ivar properties: The operation properties.
    :vartype properties: JSON
    """

    _attribute_map = {
        "name": {"key": "name", "type": "str"},
        "display_name": {"key": "displayName", "type": "str"},
        "description": {"key": "description", "type": "str"},
        "origin": {"key": "origin", "type": "str"},
        "properties": {"key": "properties", "type": "object"},
    }

    def __init__(
        self,
        *,
        name: Optional[str] = None,
        display_name: Optional[str] = None,
        description: Optional[str] = None,
        origin: Optional[str] = None,
        properties: Optional[JSON] = None,
        **kwargs: Any
    ) -> None:
        """
        :keyword name: The operation name.
        :paramtype name: str
        :keyword display_name: The operation display name.
        :paramtype display_name: str
        :keyword description: The operation description.
        :paramtype description: str
        :keyword origin: The operation origin.
        :paramtype origin: str
        :keyword properties: The operation properties.
        :paramtype properties: JSON
        """
        super().__init__(**kwargs)
        self.name = name
        self.display_name = display_name
        self.description = description
        self.origin = origin
        self.properties = properties


class ProviderOperationsMetadata(_serialization.Model):
    """Provider Operations metadata.

    :ivar id: The provider id.
    :vartype id: str
    :ivar name: The provider name.
    :vartype name: str
    :ivar type: The provider type.
    :vartype type: str
    :ivar display_name: The provider display name.
    :vartype display_name: str
    :ivar resource_types: The provider resource types.
    :vartype resource_types: list[~azure.mgmt.authorization.v2015_07_01.models.ResourceType]
    :ivar operations: The provider operations.
    :vartype operations: list[~azure.mgmt.authorization.v2015_07_01.models.ProviderOperation]
    """

    _attribute_map = {
        "id": {"key": "id", "type": "str"},
        "name": {"key": "name", "type": "str"},
        "type": {"key": "type", "type": "str"},
        "display_name": {"key": "displayName", "type": "str"},
        "resource_types": {"key": "resourceTypes", "type": "[ResourceType]"},
        "operations": {"key": "operations", "type": "[ProviderOperation]"},
    }

    def __init__(
        self,
        *,
        id: Optional[str] = None,  # pylint: disable=redefined-builtin
        name: Optional[str] = None,
        type: Optional[str] = None,
        display_name: Optional[str] = None,
        resource_types: Optional[List["_models.ResourceType"]] = None,
        operations: Optional[List["_models.ProviderOperation"]] = None,
        **kwargs: Any
    ) -> None:
        """
        :keyword id: The provider id.
        :paramtype id: str
        :keyword name: The provider name.
        :paramtype name: str
        :keyword type: The provider type.
        :paramtype type: str
        :keyword display_name: The provider display name.
        :paramtype display_name: str
        :keyword resource_types: The provider resource types.
        :paramtype resource_types: list[~azure.mgmt.authorization.v2015_07_01.models.ResourceType]
        :keyword operations: The provider operations.
        :paramtype operations: list[~azure.mgmt.authorization.v2015_07_01.models.ProviderOperation]
        """
        super().__init__(**kwargs)
        self.id = id
        self.name = name
        self.type = type
        self.display_name = display_name
        self.resource_types = resource_types
        self.operations = operations


class ProviderOperationsMetadataListResult(_serialization.Model):
    """Provider operations metadata list.

    :ivar value: The list of providers.
    :vartype value: list[~azure.mgmt.authorization.v2015_07_01.models.ProviderOperationsMetadata]
    :ivar next_link: The URL to use for getting the next set of results.
    :vartype next_link: str
    """

    _attribute_map = {
        "value": {"key": "value", "type": "[ProviderOperationsMetadata]"},
        "next_link": {"key": "nextLink", "type": "str"},
    }

    def __init__(
        self,
        *,
        value: Optional[List["_models.ProviderOperationsMetadata"]] = None,
        next_link: Optional[str] = None,
        **kwargs: Any
    ) -> None:
        """
        :keyword value: The list of providers.
        :paramtype value: list[~azure.mgmt.authorization.v2015_07_01.models.ProviderOperationsMetadata]
        :keyword next_link: The URL to use for getting the next set of results.
        :paramtype next_link: str
        """
        super().__init__(**kwargs)
        self.value = value
        self.next_link = next_link


class ResourceType(_serialization.Model):
    """Resource Type.

    :ivar name: The resource type name.
    :vartype name: str
    :ivar display_name: The resource type display name.
    :vartype display_name: str
    :ivar operations: The resource type operations.
    :vartype operations: list[~azure.mgmt.authorization.v2015_07_01.models.ProviderOperation]
    """

    _attribute_map = {
        "name": {"key": "name", "type": "str"},
        "display_name": {"key": "displayName", "type": "str"},
        "operations": {"key": "operations", "type": "[ProviderOperation]"},
    }

    def __init__(
        self,
        *,
        name: Optional[str] = None,
        display_name: Optional[str] = None,
        operations: Optional[List["_models.ProviderOperation"]] = None,
        **kwargs: Any
    ) -> None:
        """
        :keyword name: The resource type name.
        :paramtype name: str
        :keyword display_name: The resource type display name.
        :paramtype display_name: str
        :keyword operations: The resource type operations.
        :paramtype operations: list[~azure.mgmt.authorization.v2015_07_01.models.ProviderOperation]
        """
        super().__init__(**kwargs)
        self.name = name
        self.display_name = display_name
        self.operations = operations


class RoleAssignment(_serialization.Model):
    """Role Assignments.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar id: The role assignment ID.
    :vartype id: str
    :ivar name: The role assignment name.
    :vartype name: str
    :ivar type: The role assignment type.
    :vartype type: str
    :ivar properties: Role assignment properties.
    :vartype properties:
     ~azure.mgmt.authorization.v2015_07_01.models.RoleAssignmentPropertiesWithScope
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
        "properties": {"key": "properties", "type": "RoleAssignmentPropertiesWithScope"},
    }

    def __init__(
        self, *, properties: Optional["_models.RoleAssignmentPropertiesWithScope"] = None, **kwargs: Any
    ) -> None:
        """
        :keyword properties: Role assignment properties.
        :paramtype properties:
         ~azure.mgmt.authorization.v2015_07_01.models.RoleAssignmentPropertiesWithScope
        """
        super().__init__(**kwargs)
        self.id = None
        self.name = None
        self.type = None
        self.properties = properties


class RoleAssignmentCreateParameters(_serialization.Model):
    """Role assignment create parameters.

    All required parameters must be populated in order to send to Azure.

    :ivar properties: Role assignment properties. Required.
    :vartype properties: ~azure.mgmt.authorization.v2015_07_01.models.RoleAssignmentProperties
    """

    _validation = {
        "properties": {"required": True},
    }

    _attribute_map = {
        "properties": {"key": "properties", "type": "RoleAssignmentProperties"},
    }

    def __init__(self, *, properties: "_models.RoleAssignmentProperties", **kwargs: Any) -> None:
        """
        :keyword properties: Role assignment properties. Required.
        :paramtype properties: ~azure.mgmt.authorization.v2015_07_01.models.RoleAssignmentProperties
        """
        super().__init__(**kwargs)
        self.properties = properties


class RoleAssignmentFilter(_serialization.Model):
    """Role Assignments filter.

    :ivar principal_id: Returns role assignment of the specific principal.
    :vartype principal_id: str
    """

    _attribute_map = {
        "principal_id": {"key": "principalId", "type": "str"},
    }

    def __init__(self, *, principal_id: Optional[str] = None, **kwargs: Any) -> None:
        """
        :keyword principal_id: Returns role assignment of the specific principal.
        :paramtype principal_id: str
        """
        super().__init__(**kwargs)
        self.principal_id = principal_id


class RoleAssignmentListResult(_serialization.Model):
    """Role assignment list operation result.

    :ivar value: Role assignment list.
    :vartype value: list[~azure.mgmt.authorization.v2015_07_01.models.RoleAssignment]
    :ivar next_link: The URL to use for getting the next set of results.
    :vartype next_link: str
    """

    _attribute_map = {
        "value": {"key": "value", "type": "[RoleAssignment]"},
        "next_link": {"key": "nextLink", "type": "str"},
    }

    def __init__(
        self, *, value: Optional[List["_models.RoleAssignment"]] = None, next_link: Optional[str] = None, **kwargs: Any
    ) -> None:
        """
        :keyword value: Role assignment list.
        :paramtype value: list[~azure.mgmt.authorization.v2015_07_01.models.RoleAssignment]
        :keyword next_link: The URL to use for getting the next set of results.
        :paramtype next_link: str
        """
        super().__init__(**kwargs)
        self.value = value
        self.next_link = next_link


class RoleAssignmentProperties(_serialization.Model):
    """Role assignment properties.

    All required parameters must be populated in order to send to Azure.

    :ivar role_definition_id: The role definition ID used in the role assignment. Required.
    :vartype role_definition_id: str
    :ivar principal_id: The principal ID assigned to the role. This maps to the ID inside the
     Active Directory. It can point to a user, service principal, or security group. Required.
    :vartype principal_id: str
    """

    _validation = {
        "role_definition_id": {"required": True},
        "principal_id": {"required": True},
    }

    _attribute_map = {
        "role_definition_id": {"key": "roleDefinitionId", "type": "str"},
        "principal_id": {"key": "principalId", "type": "str"},
    }

    def __init__(self, *, role_definition_id: str, principal_id: str, **kwargs: Any) -> None:
        """
        :keyword role_definition_id: The role definition ID used in the role assignment. Required.
        :paramtype role_definition_id: str
        :keyword principal_id: The principal ID assigned to the role. This maps to the ID inside the
         Active Directory. It can point to a user, service principal, or security group. Required.
        :paramtype principal_id: str
        """
        super().__init__(**kwargs)
        self.role_definition_id = role_definition_id
        self.principal_id = principal_id


class RoleAssignmentPropertiesWithScope(_serialization.Model):
    """Role assignment properties with scope.

    :ivar scope: The role assignment scope.
    :vartype scope: str
    :ivar role_definition_id: The role definition ID.
    :vartype role_definition_id: str
    :ivar principal_id: The principal ID.
    :vartype principal_id: str
    """

    _attribute_map = {
        "scope": {"key": "scope", "type": "str"},
        "role_definition_id": {"key": "roleDefinitionId", "type": "str"},
        "principal_id": {"key": "principalId", "type": "str"},
    }

    def __init__(
        self,
        *,
        scope: Optional[str] = None,
        role_definition_id: Optional[str] = None,
        principal_id: Optional[str] = None,
        **kwargs: Any
    ) -> None:
        """
        :keyword scope: The role assignment scope.
        :paramtype scope: str
        :keyword role_definition_id: The role definition ID.
        :paramtype role_definition_id: str
        :keyword principal_id: The principal ID.
        :paramtype principal_id: str
        """
        super().__init__(**kwargs)
        self.scope = scope
        self.role_definition_id = role_definition_id
        self.principal_id = principal_id


class RoleDefinition(_serialization.Model):
    """Role definition.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar id: The role definition ID.
    :vartype id: str
    :ivar name: The role definition name.
    :vartype name: str
    :ivar type: The role definition type.
    :vartype type: str
    :ivar role_name: The role name.
    :vartype role_name: str
    :ivar description: The role definition description.
    :vartype description: str
    :ivar role_type: The role type.
    :vartype role_type: str
    :ivar permissions: Role definition permissions.
    :vartype permissions: list[~azure.mgmt.authorization.v2015_07_01.models.Permission]
    :ivar assignable_scopes: Role definition assignable scopes.
    :vartype assignable_scopes: list[str]
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
        "role_name": {"key": "properties.roleName", "type": "str"},
        "description": {"key": "properties.description", "type": "str"},
        "role_type": {"key": "properties.type", "type": "str"},
        "permissions": {"key": "properties.permissions", "type": "[Permission]"},
        "assignable_scopes": {"key": "properties.assignableScopes", "type": "[str]"},
    }

    def __init__(
        self,
        *,
        role_name: Optional[str] = None,
        description: Optional[str] = None,
        role_type: Optional[str] = None,
        permissions: Optional[List["_models.Permission"]] = None,
        assignable_scopes: Optional[List[str]] = None,
        **kwargs: Any
    ) -> None:
        """
        :keyword role_name: The role name.
        :paramtype role_name: str
        :keyword description: The role definition description.
        :paramtype description: str
        :keyword role_type: The role type.
        :paramtype role_type: str
        :keyword permissions: Role definition permissions.
        :paramtype permissions: list[~azure.mgmt.authorization.v2015_07_01.models.Permission]
        :keyword assignable_scopes: Role definition assignable scopes.
        :paramtype assignable_scopes: list[str]
        """
        super().__init__(**kwargs)
        self.id = None
        self.name = None
        self.type = None
        self.role_name = role_name
        self.description = description
        self.role_type = role_type
        self.permissions = permissions
        self.assignable_scopes = assignable_scopes


class RoleDefinitionFilter(_serialization.Model):
    """Role Definitions filter.

    :ivar role_name: Returns role definition with the specific name.
    :vartype role_name: str
    """

    _attribute_map = {
        "role_name": {"key": "roleName", "type": "str"},
    }

    def __init__(self, *, role_name: Optional[str] = None, **kwargs: Any) -> None:
        """
        :keyword role_name: Returns role definition with the specific name.
        :paramtype role_name: str
        """
        super().__init__(**kwargs)
        self.role_name = role_name


class RoleDefinitionListResult(_serialization.Model):
    """Role definition list operation result.

    :ivar value: Role definition list.
    :vartype value: list[~azure.mgmt.authorization.v2015_07_01.models.RoleDefinition]
    :ivar next_link: The URL to use for getting the next set of results.
    :vartype next_link: str
    """

    _attribute_map = {
        "value": {"key": "value", "type": "[RoleDefinition]"},
        "next_link": {"key": "nextLink", "type": "str"},
    }

    def __init__(
        self, *, value: Optional[List["_models.RoleDefinition"]] = None, next_link: Optional[str] = None, **kwargs: Any
    ) -> None:
        """
        :keyword value: Role definition list.
        :paramtype value: list[~azure.mgmt.authorization.v2015_07_01.models.RoleDefinition]
        :keyword next_link: The URL to use for getting the next set of results.
        :paramtype next_link: str
        """
        super().__init__(**kwargs)
        self.value = value
        self.next_link = next_link
