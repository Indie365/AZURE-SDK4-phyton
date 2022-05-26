# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from copy import deepcopy
from typing import Any, Awaitable

from msrest import Deserializer, Serializer

from azure.core import AsyncPipelineClient
from azure.core.rest import AsyncHttpResponse, HttpRequest

from .. import models
from ._configuration import AzureQueueStorageConfiguration
from .operations import MessageIdOperations, MessagesOperations, QueueOperations, ServiceOperations

class AzureQueueStorage:  # pylint: disable=client-accepts-api-version-keyword
    """AzureQueueStorage.

    :ivar service: ServiceOperations operations
    :vartype service: azure.storage.queue.aio.operations.ServiceOperations
    :ivar queue: QueueOperations operations
    :vartype queue: azure.storage.queue.aio.operations.QueueOperations
    :ivar messages: MessagesOperations operations
    :vartype messages: azure.storage.queue.aio.operations.MessagesOperations
    :ivar message_id: MessageIdOperations operations
    :vartype message_id: azure.storage.queue.aio.operations.MessageIdOperations
    :param url: The URL of the service account, queue or message that is the target of the desired
     operation. Required.
    :type url: str
    :param base_url: Service URL. Required. Default value is "".
    :type base_url: str
    :keyword version: Specifies the version of the operation to use for this request. Default value
     is "2018-03-28". Note that overriding this default value may result in unsupported behavior.
    :paramtype version: str
    """

    def __init__(
        self,
        url: str,
        base_url: str = "",
        **kwargs: Any
    ) -> None:
        self._config = AzureQueueStorageConfiguration(url=url, **kwargs)
        self._client = AsyncPipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)
        self._serialize.client_side_validation = False
        self.service = ServiceOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.queue = QueueOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.messages = MessagesOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.message_id = MessageIdOperations(
            self._client, self._config, self._serialize, self._deserialize
        )


    def _send_request(
        self,
        request: HttpRequest,
        **kwargs: Any
    ) -> Awaitable[AsyncHttpResponse]:
        """Runs the network request through the client's chained policies.

        >>> from azure.core.rest import HttpRequest
        >>> request = HttpRequest("GET", "https://www.example.org/")
        <HttpRequest [GET], url: 'https://www.example.org/'>
        >>> response = await client._send_request(request)
        <AsyncHttpResponse: 200 OK>

        For more information on this code flow, see https://aka.ms/azsdk/python/protocol/quickstart

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

    async def __aenter__(self) -> "AzureQueueStorage":
        await self._client.__aenter__()
        return self

    async def __aexit__(self, *exc_details) -> None:
        await self._client.__aexit__(*exc_details)
