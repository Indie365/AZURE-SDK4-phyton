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
    AccessReviewDefaultSettingsOperations,
    AccessReviewInstanceContactedReviewersOperations,
    AccessReviewInstanceDecisionsOperations,
    AccessReviewInstanceMyDecisionsOperations,
    AccessReviewInstanceOperations,
    AccessReviewInstancesAssignedForMyApprovalOperations,
    AccessReviewInstancesOperations,
    AccessReviewScheduleDefinitionsAssignedForMyApprovalOperations,
    AccessReviewScheduleDefinitionsOperations,
    Operations,
    TenantLevelAccessReviewInstanceContactedReviewersOperations,
)

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from azure.core.credentials import TokenCredential


class AuthorizationManagementClient:  # pylint: disable=client-accepts-api-version-keyword,too-many-instance-attributes
    """Access reviews service provides the workflow for running access reviews on different kind of
    resources.

    :ivar operations: Operations operations
    :vartype operations: azure.mgmt.authorization.v2021_07_01_preview.operations.Operations
    :ivar access_review_schedule_definitions: AccessReviewScheduleDefinitionsOperations operations
    :vartype access_review_schedule_definitions:
     azure.mgmt.authorization.v2021_07_01_preview.operations.AccessReviewScheduleDefinitionsOperations
    :ivar access_review_instances: AccessReviewInstancesOperations operations
    :vartype access_review_instances:
     azure.mgmt.authorization.v2021_07_01_preview.operations.AccessReviewInstancesOperations
    :ivar access_review_instance: AccessReviewInstanceOperations operations
    :vartype access_review_instance:
     azure.mgmt.authorization.v2021_07_01_preview.operations.AccessReviewInstanceOperations
    :ivar access_review_instance_decisions: AccessReviewInstanceDecisionsOperations operations
    :vartype access_review_instance_decisions:
     azure.mgmt.authorization.v2021_07_01_preview.operations.AccessReviewInstanceDecisionsOperations
    :ivar access_review_instance_contacted_reviewers:
     AccessReviewInstanceContactedReviewersOperations operations
    :vartype access_review_instance_contacted_reviewers:
     azure.mgmt.authorization.v2021_07_01_preview.operations.AccessReviewInstanceContactedReviewersOperations
    :ivar access_review_default_settings: AccessReviewDefaultSettingsOperations operations
    :vartype access_review_default_settings:
     azure.mgmt.authorization.v2021_07_01_preview.operations.AccessReviewDefaultSettingsOperations
    :ivar access_review_schedule_definitions_assigned_for_my_approval:
     AccessReviewScheduleDefinitionsAssignedForMyApprovalOperations operations
    :vartype access_review_schedule_definitions_assigned_for_my_approval:
     azure.mgmt.authorization.v2021_07_01_preview.operations.AccessReviewScheduleDefinitionsAssignedForMyApprovalOperations
    :ivar access_review_instances_assigned_for_my_approval:
     AccessReviewInstancesAssignedForMyApprovalOperations operations
    :vartype access_review_instances_assigned_for_my_approval:
     azure.mgmt.authorization.v2021_07_01_preview.operations.AccessReviewInstancesAssignedForMyApprovalOperations
    :ivar access_review_instance_my_decisions: AccessReviewInstanceMyDecisionsOperations operations
    :vartype access_review_instance_my_decisions:
     azure.mgmt.authorization.v2021_07_01_preview.operations.AccessReviewInstanceMyDecisionsOperations
    :ivar tenant_level_access_review_instance_contacted_reviewers:
     TenantLevelAccessReviewInstanceContactedReviewersOperations operations
    :vartype tenant_level_access_review_instance_contacted_reviewers:
     azure.mgmt.authorization.v2021_07_01_preview.operations.TenantLevelAccessReviewInstanceContactedReviewersOperations
    :param credential: Credential needed for the client to connect to Azure. Required.
    :type credential: ~azure.core.credentials.TokenCredential
    :param subscription_id: The ID of the target subscription. Required.
    :type subscription_id: str
    :param base_url: Service URL. Default value is "https://management.azure.com".
    :type base_url: str
    :keyword api_version: Api Version. Default value is "2021-07-01-preview". Note that overriding
     this default value may result in unsupported behavior.
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
        self.operations = Operations(self._client, self._config, self._serialize, self._deserialize)
        self.access_review_schedule_definitions = AccessReviewScheduleDefinitionsOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.access_review_instances = AccessReviewInstancesOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.access_review_instance = AccessReviewInstanceOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.access_review_instance_decisions = AccessReviewInstanceDecisionsOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.access_review_instance_contacted_reviewers = AccessReviewInstanceContactedReviewersOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.access_review_default_settings = AccessReviewDefaultSettingsOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.access_review_schedule_definitions_assigned_for_my_approval = (
            AccessReviewScheduleDefinitionsAssignedForMyApprovalOperations(
                self._client, self._config, self._serialize, self._deserialize
            )
        )
        self.access_review_instances_assigned_for_my_approval = AccessReviewInstancesAssignedForMyApprovalOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.access_review_instance_my_decisions = AccessReviewInstanceMyDecisionsOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.tenant_level_access_review_instance_contacted_reviewers = (
            TenantLevelAccessReviewInstanceContactedReviewersOperations(
                self._client, self._config, self._serialize, self._deserialize
            )
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
