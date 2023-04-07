# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from copy import deepcopy
from typing import Any, TYPE_CHECKING

from azure.core.rest import HttpRequest, HttpResponse
from azure.mgmt.core import ARMPipelineClient

from . import models as _models
from .._serialization import Deserializer, Serializer
from ._configuration import AuthorizationManagementClientConfiguration
from .operations import (
    DenyAssignmentsOperations,
    PermissionsOperations,
    ProviderOperationsMetadataOperations,
    RoleAssignmentsOperations,
    RoleDefinitionsOperations,
)

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from azure.core.credentials import TokenCredential


class AuthorizationManagementClient:  # pylint: disable=client-accepts-api-version-keyword
    """Role based access control provides you a way to apply granular level policy administration down
    to individual resources or resource groups. These operations enable you to get deny
    assignments. A deny assignment describes the set of actions on resources that are denied for
    Azure Active Directory users.

    :ivar deny_assignments: DenyAssignmentsOperations operations
    :vartype deny_assignments:
     azure.mgmt.authorization.v2022_04_01.operations.DenyAssignmentsOperations
    :ivar provider_operations_metadata: ProviderOperationsMetadataOperations operations
    :vartype provider_operations_metadata:
     azure.mgmt.authorization.v2022_04_01.operations.ProviderOperationsMetadataOperations
    :ivar role_assignments: RoleAssignmentsOperations operations
    :vartype role_assignments:
     azure.mgmt.authorization.v2022_04_01.operations.RoleAssignmentsOperations
    :ivar permissions: PermissionsOperations operations
    :vartype permissions: azure.mgmt.authorization.v2022_04_01.operations.PermissionsOperations
    :ivar role_definitions: RoleDefinitionsOperations operations
    :vartype role_definitions:
     azure.mgmt.authorization.v2022_04_01.operations.RoleDefinitionsOperations
    :param credential: Credential needed for the client to connect to Azure. Required.
    :type credential: ~azure.core.credentials.TokenCredential
    :param subscription_id: The ID of the target subscription. Required.
    :type subscription_id: str
    :param base_url: Service URL. Default value is "https://management.azure.com".
    :type base_url: str
    :keyword api_version: Api Version. Default value is "2022-04-01". Note that overriding this
     default value may result in unsupported behavior.
    :paramtype api_version: str
    """

    def __init__(
        self,
        credential: "TokenCredential",
        subscription_id: str,
        base_url: str = "https://management.azure.com",
        **kwargs: Any
    ) -> None:
        self._config = AuthorizationManagementClientConfiguration(
            credential=credential, subscription_id=subscription_id, **kwargs
        )
        self._client = ARMPipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in _models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)
        self._serialize.client_side_validation = False
        self.deny_assignments = DenyAssignmentsOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.provider_operations_metadata = ProviderOperationsMetadataOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.role_assignments = RoleAssignmentsOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.permissions = PermissionsOperations(self._client, self._config, self._serialize, self._deserialize)
        self.role_definitions = RoleDefinitionsOperations(
            self._client, self._config, self._serialize, self._deserialize
        )

    def _send_request(self, request: HttpRequest, **kwargs: Any) -> HttpResponse:
        """Runs the network request through the client's chained policies.

        >>> from azure.core.rest import HttpRequest
        >>> request = HttpRequest("GET", "https://www.example.org/")
        <HttpRequest [GET], url: 'https://www.example.org/'>
        >>> response = client._send_request(request)
        <HttpResponse: 200 OK>

        For more information on this code flow, see https://aka.ms/azsdk/dpcodegen/python/send_request

        :param request: The network request you want to make. Required.
        :type request: ~azure.core.rest.HttpRequest
        :keyword bool stream: Whether the response payload will be streamed. Defaults to False.
        :return: The response of your network call. Does not do error handling on your response.
        :rtype: ~azure.core.rest.HttpResponse
        """

        request_copy = deepcopy(request)
        request_copy.url = self._client.format_url(request_copy.url)
        return self._client.send_request(request_copy, **kwargs)

    def close(self) -> None:
        self._client.close()

    def __enter__(self) -> "AuthorizationManagementClient":
        self._client.__enter__()
        return self

    def __exit__(self, *exc_details: Any) -> None:
        self._client.__exit__(*exc_details)
