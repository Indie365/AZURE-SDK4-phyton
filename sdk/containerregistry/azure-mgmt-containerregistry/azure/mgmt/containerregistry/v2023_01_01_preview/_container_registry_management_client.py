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
from ._configuration import ContainerRegistryManagementClientConfiguration
from .operations import (
    CacheRulesOperations,
    ConnectedRegistriesOperations,
    CredentialSetsOperations,
    ExportPipelinesOperations,
    ImportPipelinesOperations,
    Operations,
    PipelineRunsOperations,
    PrivateEndpointConnectionsOperations,
    RegistriesOperations,
    ReplicationsOperations,
    ScopeMapsOperations,
    TokensOperations,
    WebhooksOperations,
)

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from azure.core.credentials import TokenCredential


class ContainerRegistryManagementClient:  # pylint: disable=client-accepts-api-version-keyword,too-many-instance-attributes
    """ContainerRegistryManagementClient.

    :ivar cache_rules: CacheRulesOperations operations
    :vartype cache_rules:
     azure.mgmt.containerregistry.v2023_01_01_preview.operations.CacheRulesOperations
    :ivar connected_registries: ConnectedRegistriesOperations operations
    :vartype connected_registries:
     azure.mgmt.containerregistry.v2023_01_01_preview.operations.ConnectedRegistriesOperations
    :ivar credential_sets: CredentialSetsOperations operations
    :vartype credential_sets:
     azure.mgmt.containerregistry.v2023_01_01_preview.operations.CredentialSetsOperations
    :ivar export_pipelines: ExportPipelinesOperations operations
    :vartype export_pipelines:
     azure.mgmt.containerregistry.v2023_01_01_preview.operations.ExportPipelinesOperations
    :ivar registries: RegistriesOperations operations
    :vartype registries:
     azure.mgmt.containerregistry.v2023_01_01_preview.operations.RegistriesOperations
    :ivar import_pipelines: ImportPipelinesOperations operations
    :vartype import_pipelines:
     azure.mgmt.containerregistry.v2023_01_01_preview.operations.ImportPipelinesOperations
    :ivar operations: Operations operations
    :vartype operations: azure.mgmt.containerregistry.v2023_01_01_preview.operations.Operations
    :ivar pipeline_runs: PipelineRunsOperations operations
    :vartype pipeline_runs:
     azure.mgmt.containerregistry.v2023_01_01_preview.operations.PipelineRunsOperations
    :ivar private_endpoint_connections: PrivateEndpointConnectionsOperations operations
    :vartype private_endpoint_connections:
     azure.mgmt.containerregistry.v2023_01_01_preview.operations.PrivateEndpointConnectionsOperations
    :ivar replications: ReplicationsOperations operations
    :vartype replications:
     azure.mgmt.containerregistry.v2023_01_01_preview.operations.ReplicationsOperations
    :ivar scope_maps: ScopeMapsOperations operations
    :vartype scope_maps:
     azure.mgmt.containerregistry.v2023_01_01_preview.operations.ScopeMapsOperations
    :ivar tokens: TokensOperations operations
    :vartype tokens: azure.mgmt.containerregistry.v2023_01_01_preview.operations.TokensOperations
    :ivar webhooks: WebhooksOperations operations
    :vartype webhooks:
     azure.mgmt.containerregistry.v2023_01_01_preview.operations.WebhooksOperations
    :param credential: Credential needed for the client to connect to Azure. Required.
    :type credential: ~azure.core.credentials.TokenCredential
    :param subscription_id: The ID of the target subscription. The value must be an UUID. Required.
    :type subscription_id: str
    :param base_url: Service URL. Default value is "https://management.azure.com".
    :type base_url: str
    :keyword api_version: Api Version. Default value is "2023-01-01-preview". Note that overriding
     this default value may result in unsupported behavior.
    :paramtype api_version: str
    :keyword int polling_interval: Default waiting time between two polls for LRO operations if no
     Retry-After header is present.
    """

    def __init__(
        self,
        credential: "TokenCredential",
        subscription_id: str,
        base_url: str = "https://management.azure.com",
        **kwargs: Any
    ) -> None:
        self._config = ContainerRegistryManagementClientConfiguration(
            credential=credential, subscription_id=subscription_id, **kwargs
        )
        self._client = ARMPipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in _models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)
        self._serialize.client_side_validation = False
        self.cache_rules = CacheRulesOperations(self._client, self._config, self._serialize, self._deserialize)
        self.connected_registries = ConnectedRegistriesOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.credential_sets = CredentialSetsOperations(self._client, self._config, self._serialize, self._deserialize)
        self.export_pipelines = ExportPipelinesOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.registries = RegistriesOperations(self._client, self._config, self._serialize, self._deserialize)
        self.import_pipelines = ImportPipelinesOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.operations = Operations(self._client, self._config, self._serialize, self._deserialize)
        self.pipeline_runs = PipelineRunsOperations(self._client, self._config, self._serialize, self._deserialize)
        self.private_endpoint_connections = PrivateEndpointConnectionsOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.replications = ReplicationsOperations(self._client, self._config, self._serialize, self._deserialize)
        self.scope_maps = ScopeMapsOperations(self._client, self._config, self._serialize, self._deserialize)
        self.tokens = TokensOperations(self._client, self._config, self._serialize, self._deserialize)
        self.webhooks = WebhooksOperations(self._client, self._config, self._serialize, self._deserialize)

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

    def __enter__(self) -> "ContainerRegistryManagementClient":
        self._client.__enter__()
        return self

    def __exit__(self, *exc_details) -> None:
        self._client.__exit__(*exc_details)
