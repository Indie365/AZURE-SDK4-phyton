# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from copy import deepcopy
from typing import Any, Awaitable, TYPE_CHECKING

from azure.core.rest import AsyncHttpResponse, HttpRequest
from azure.mgmt.core import AsyncARMPipelineClient

from .. import models as _models
from .._serialization import Deserializer, Serializer
from ._configuration import AzureMediaServicesConfiguration
from .operations import (
    AccountFiltersOperations,
    AssetFiltersOperations,
    AssetsOperations,
    ContentKeyPoliciesOperations,
    JobsOperations,
    LiveEventsOperations,
    LiveOutputsOperations,
    LocationsOperations,
    MediaServicesOperationResultsOperations,
    MediaServicesOperationStatusesOperations,
    MediaservicesOperations,
    OperationResultsOperations,
    OperationStatusesOperations,
    Operations,
    PrivateEndpointConnectionsOperations,
    PrivateLinkResourcesOperations,
    StreamingEndpointsOperations,
    StreamingLocatorsOperations,
    StreamingPoliciesOperations,
    TracksOperations,
    TransformsOperations,
)

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from azure.core.credentials_async import AsyncTokenCredential


class AzureMediaServices:  # pylint: disable=client-accepts-api-version-keyword,too-many-instance-attributes
    """This Swagger was generated by the API Framework.

    :ivar account_filters: AccountFiltersOperations operations
    :vartype account_filters: azure.mgmt.media.aio.operations.AccountFiltersOperations
    :ivar operations: Operations operations
    :vartype operations: azure.mgmt.media.aio.operations.Operations
    :ivar mediaservices: MediaservicesOperations operations
    :vartype mediaservices: azure.mgmt.media.aio.operations.MediaservicesOperations
    :ivar private_link_resources: PrivateLinkResourcesOperations operations
    :vartype private_link_resources: azure.mgmt.media.aio.operations.PrivateLinkResourcesOperations
    :ivar private_endpoint_connections: PrivateEndpointConnectionsOperations operations
    :vartype private_endpoint_connections:
     azure.mgmt.media.aio.operations.PrivateEndpointConnectionsOperations
    :ivar locations: LocationsOperations operations
    :vartype locations: azure.mgmt.media.aio.operations.LocationsOperations
    :ivar media_services_operation_statuses: MediaServicesOperationStatusesOperations operations
    :vartype media_services_operation_statuses:
     azure.mgmt.media.aio.operations.MediaServicesOperationStatusesOperations
    :ivar media_services_operation_results: MediaServicesOperationResultsOperations operations
    :vartype media_services_operation_results:
     azure.mgmt.media.aio.operations.MediaServicesOperationResultsOperations
    :ivar assets: AssetsOperations operations
    :vartype assets: azure.mgmt.media.aio.operations.AssetsOperations
    :ivar asset_filters: AssetFiltersOperations operations
    :vartype asset_filters: azure.mgmt.media.aio.operations.AssetFiltersOperations
    :ivar tracks: TracksOperations operations
    :vartype tracks: azure.mgmt.media.aio.operations.TracksOperations
    :ivar operation_statuses: OperationStatusesOperations operations
    :vartype operation_statuses: azure.mgmt.media.aio.operations.OperationStatusesOperations
    :ivar operation_results: OperationResultsOperations operations
    :vartype operation_results: azure.mgmt.media.aio.operations.OperationResultsOperations
    :ivar content_key_policies: ContentKeyPoliciesOperations operations
    :vartype content_key_policies: azure.mgmt.media.aio.operations.ContentKeyPoliciesOperations
    :ivar transforms: TransformsOperations operations
    :vartype transforms: azure.mgmt.media.aio.operations.TransformsOperations
    :ivar jobs: JobsOperations operations
    :vartype jobs: azure.mgmt.media.aio.operations.JobsOperations
    :ivar streaming_policies: StreamingPoliciesOperations operations
    :vartype streaming_policies: azure.mgmt.media.aio.operations.StreamingPoliciesOperations
    :ivar streaming_locators: StreamingLocatorsOperations operations
    :vartype streaming_locators: azure.mgmt.media.aio.operations.StreamingLocatorsOperations
    :ivar live_events: LiveEventsOperations operations
    :vartype live_events: azure.mgmt.media.aio.operations.LiveEventsOperations
    :ivar live_outputs: LiveOutputsOperations operations
    :vartype live_outputs: azure.mgmt.media.aio.operations.LiveOutputsOperations
    :ivar streaming_endpoints: StreamingEndpointsOperations operations
    :vartype streaming_endpoints: azure.mgmt.media.aio.operations.StreamingEndpointsOperations
    :param credential: Credential needed for the client to connect to Azure. Required.
    :type credential: ~azure.core.credentials_async.AsyncTokenCredential
    :param subscription_id: The unique identifier for a Microsoft Azure subscription. Required.
    :type subscription_id: str
    :param base_url: Service URL. Default value is "https://management.azure.com".
    :type base_url: str
    :keyword int polling_interval: Default waiting time between two polls for LRO operations if no
     Retry-After header is present.
    """

    def __init__(
        self,
        credential: "AsyncTokenCredential",
        subscription_id: str,
        base_url: str = "https://management.azure.com",
        **kwargs: Any
    ) -> None:
        self._config = AzureMediaServicesConfiguration(credential=credential, subscription_id=subscription_id, **kwargs)
        self._client = AsyncARMPipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in _models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)
        self._serialize.client_side_validation = False
        self.account_filters = AccountFiltersOperations(self._client, self._config, self._serialize, self._deserialize)
        self.operations = Operations(self._client, self._config, self._serialize, self._deserialize)
        self.mediaservices = MediaservicesOperations(self._client, self._config, self._serialize, self._deserialize)
        self.private_link_resources = PrivateLinkResourcesOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.private_endpoint_connections = PrivateEndpointConnectionsOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.locations = LocationsOperations(self._client, self._config, self._serialize, self._deserialize)
        self.media_services_operation_statuses = MediaServicesOperationStatusesOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.media_services_operation_results = MediaServicesOperationResultsOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.assets = AssetsOperations(self._client, self._config, self._serialize, self._deserialize)
        self.asset_filters = AssetFiltersOperations(self._client, self._config, self._serialize, self._deserialize)
        self.tracks = TracksOperations(self._client, self._config, self._serialize, self._deserialize)
        self.operation_statuses = OperationStatusesOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.operation_results = OperationResultsOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.content_key_policies = ContentKeyPoliciesOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.transforms = TransformsOperations(self._client, self._config, self._serialize, self._deserialize)
        self.jobs = JobsOperations(self._client, self._config, self._serialize, self._deserialize)
        self.streaming_policies = StreamingPoliciesOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.streaming_locators = StreamingLocatorsOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.live_events = LiveEventsOperations(self._client, self._config, self._serialize, self._deserialize)
        self.live_outputs = LiveOutputsOperations(self._client, self._config, self._serialize, self._deserialize)
        self.streaming_endpoints = StreamingEndpointsOperations(
            self._client, self._config, self._serialize, self._deserialize
        )

    def _send_request(self, request: HttpRequest, **kwargs: Any) -> Awaitable[AsyncHttpResponse]:
        """Runs the network request through the client's chained policies.

        >>> from azure.core.rest import HttpRequest
        >>> request = HttpRequest("GET", "https://www.example.org/")
        <HttpRequest [GET], url: 'https://www.example.org/'>
        >>> response = await client._send_request(request)
        <AsyncHttpResponse: 200 OK>

        For more information on this code flow, see https://aka.ms/azsdk/dpcodegen/python/send_request

        :param request: The network request you want to make. Required.
        :type request: ~azure.core.rest.HttpRequest
        :keyword bool stream: Whether the response payload will be streamed. Defaults to False.
        :return: The response of your network call. Does not do error handling on your response.
        :rtype: ~azure.core.rest.AsyncHttpResponse
        """

        request_copy = deepcopy(request)
        request_copy.url = self._client.format_url(request_copy.url)
        return self._client.send_request(request_copy, **kwargs)

    async def close(self) -> None:
        await self._client.close()

    async def __aenter__(self) -> "AzureMediaServices":
        await self._client.__aenter__()
        return self

    async def __aexit__(self, *exc_details) -> None:
        await self._client.__aexit__(*exc_details)
