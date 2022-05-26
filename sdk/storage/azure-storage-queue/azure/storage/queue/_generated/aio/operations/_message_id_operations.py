# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, Callable, Dict, Optional, TypeVar

from azure.core.exceptions import ClientAuthenticationError, HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator_async import distributed_trace_async
from azure.core.utils import case_insensitive_dict

from ... import models as _models
from ..._vendor import _convert_request
from ...operations._message_id_operations import build_delete_request, build_update_request
T = TypeVar('T')
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]

class MessageIdOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~azure.storage.queue.aio.AzureQueueStorage`'s
        :attr:`message_id` attribute.
    """

    models = _models

    def __init__(self, *args, **kwargs) -> None:
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")


    @distributed_trace_async
    async def update(  # pylint: disable=inconsistent-return-statements
        self,
        pop_receipt: str,
        visibilitytimeout: int,
        timeout: Optional[int] = None,
        request_id_parameter: Optional[str] = None,
        queue_message: Optional[_models.QueueMessage] = None,
        **kwargs: Any
    ) -> None:
        """The Update operation was introduced with version 2011-08-18 of the Queue service API. The
        Update Message operation updates the visibility timeout of a message. You can also use this
        operation to update the contents of a message. A message must be in a format that can be
        included in an XML request with UTF-8 encoding, and the encoded message can be up to 64KB in
        size.

        :param pop_receipt: Required. Specifies the valid pop receipt value returned from an earlier
         call to the Get Messages or Update Message operation. Required.
        :type pop_receipt: str
        :param visibilitytimeout: Optional. Specifies the new visibility timeout value, in seconds,
         relative to server time. The default value is 30 seconds. A specified value must be larger than
         or equal to 1 second, and cannot be larger than 7 days, or larger than 2 hours on REST protocol
         versions prior to version 2011-08-18. The visibility timeout of a message can be set to a value
         later than the expiry time. Required.
        :type visibilitytimeout: int
        :param timeout: The The timeout parameter is expressed in seconds. For more information, see <a
         href="https://docs.microsoft.com/en-us/rest/api/storageservices/setting-timeouts-for-queue-service-operations>Setting
         Timeouts for Queue Service Operations.</a>. Default value is None.
        :type timeout: int
        :param request_id_parameter: Provides a client-generated, opaque value with a 1 KB character
         limit that is recorded in the analytics logs when storage analytics logging is enabled. Default
         value is None.
        :type request_id_parameter: str
        :param queue_message: A Message object which can be stored in a Queue. Default value is None.
        :type queue_message: ~azure.storage.queue.models.QueueMessage
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = kwargs.pop("params", {}) or {}

        content_type = kwargs.pop('content_type', _headers.pop('Content-Type', "application/xml"))  # type: str
        cls = kwargs.pop('cls', None)  # type: ClsType[None]

        if queue_message is not None:
            _content = self._serialize.body(queue_message, 'QueueMessage', is_xml=True)
        else:
            _content = None

        request = build_update_request(
            url=self._config.url,
            pop_receipt=pop_receipt,
            visibilitytimeout=visibilitytimeout,
            timeout=timeout,
            request_id_parameter=request_id_parameter,
            content_type=content_type,
            version=self._config.version,
            content=_content,
            template_url=self.update.metadata['url'],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request,
            stream=False,
            **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.StorageError, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        response_headers = {}
        response_headers['x-ms-request-id']=self._deserialize('str', response.headers.get('x-ms-request-id'))
        response_headers['x-ms-version']=self._deserialize('str', response.headers.get('x-ms-version'))
        response_headers['Date']=self._deserialize('rfc-1123', response.headers.get('Date'))
        response_headers['x-ms-popreceipt']=self._deserialize('str', response.headers.get('x-ms-popreceipt'))
        response_headers['x-ms-time-next-visible']=self._deserialize('rfc-1123', response.headers.get('x-ms-time-next-visible'))


        if cls:
            return cls(pipeline_response, None, response_headers)

    update.metadata = {'url': "{url}/{queueName}/messages/{messageid}"}  # type: ignore


    @distributed_trace_async
    async def delete(  # pylint: disable=inconsistent-return-statements
        self,
        pop_receipt: str,
        timeout: Optional[int] = None,
        request_id_parameter: Optional[str] = None,
        **kwargs: Any
    ) -> None:
        """The Delete operation deletes the specified message.

        :param pop_receipt: Required. Specifies the valid pop receipt value returned from an earlier
         call to the Get Messages or Update Message operation. Required.
        :type pop_receipt: str
        :param timeout: The The timeout parameter is expressed in seconds. For more information, see <a
         href="https://docs.microsoft.com/en-us/rest/api/storageservices/setting-timeouts-for-queue-service-operations>Setting
         Timeouts for Queue Service Operations.</a>. Default value is None.
        :type timeout: int
        :param request_id_parameter: Provides a client-generated, opaque value with a 1 KB character
         limit that is recorded in the analytics logs when storage analytics logging is enabled. Default
         value is None.
        :type request_id_parameter: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls = kwargs.pop('cls', None)  # type: ClsType[None]

        
        request = build_delete_request(
            url=self._config.url,
            pop_receipt=pop_receipt,
            timeout=timeout,
            request_id_parameter=request_id_parameter,
            version=self._config.version,
            template_url=self.delete.metadata['url'],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request,
            stream=False,
            **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.StorageError, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        response_headers = {}
        response_headers['x-ms-request-id']=self._deserialize('str', response.headers.get('x-ms-request-id'))
        response_headers['x-ms-version']=self._deserialize('str', response.headers.get('x-ms-version'))
        response_headers['Date']=self._deserialize('rfc-1123', response.headers.get('Date'))


        if cls:
            return cls(pipeline_response, None, response_headers)

    delete.metadata = {'url': "{url}/{queueName}/messages/{messageid}"}  # type: ignore

