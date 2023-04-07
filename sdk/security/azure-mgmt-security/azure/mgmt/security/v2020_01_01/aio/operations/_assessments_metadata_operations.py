# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import sys
from typing import Any, AsyncIterable, Callable, Dict, IO, Optional, TypeVar, Union, overload
import urllib.parse

from azure.core.async_paging import AsyncItemPaged, AsyncList
from azure.core.exceptions import (
    ClientAuthenticationError,
    HttpResponseError,
    ResourceExistsError,
    ResourceNotFoundError,
    ResourceNotModifiedError,
    map_error,
)
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator import distributed_trace
from azure.core.tracing.decorator_async import distributed_trace_async
from azure.core.utils import case_insensitive_dict
from azure.mgmt.core.exceptions import ARMErrorFormat

from ... import models as _models
from ..._vendor import _convert_request
from ...operations._assessments_metadata_operations import (
    build_create_in_subscription_request,
    build_delete_in_subscription_request,
    build_get_in_subscription_request,
    build_get_request,
    build_list_by_subscription_request,
    build_list_request,
)

if sys.version_info >= (3, 8):
    from typing import Literal  # pylint: disable=no-name-in-module, ungrouped-imports
else:
    from typing_extensions import Literal  # type: ignore  # pylint: disable=ungrouped-imports
T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]


class AssessmentsMetadataOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~azure.mgmt.security.v2020_01_01.aio.SecurityCenter`'s
        :attr:`assessments_metadata` attribute.
    """

    models = _models

    def __init__(self, *args, **kwargs) -> None:
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    @distributed_trace
    def list(self, **kwargs: Any) -> AsyncIterable["_models.SecurityAssessmentMetadata"]:
        """Get metadata information on all assessment types.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either SecurityAssessmentMetadata or the result of
         cls(response)
        :rtype:
         ~azure.core.async_paging.AsyncItemPaged[~azure.mgmt.security.v2020_01_01.models.SecurityAssessmentMetadata]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: Literal["2020-01-01"] = kwargs.pop("api_version", _params.pop("api-version", "2020-01-01"))
        cls: ClsType[_models.SecurityAssessmentMetadataList] = kwargs.pop("cls", None)

        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        def prepare_request(next_link=None):
            if not next_link:

                request = build_list_request(
                    api_version=api_version,
                    template_url=self.list.metadata["url"],
                    headers=_headers,
                    params=_params,
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)

            else:
                # make call to next link with the client's api-version
                _parsed_next_link = urllib.parse.urlparse(next_link)
                _next_request_params = case_insensitive_dict(
                    {
                        key: [urllib.parse.quote(v) for v in value]
                        for key, value in urllib.parse.parse_qs(_parsed_next_link.query).items()
                    }
                )
                _next_request_params["api-version"] = self._config.api_version
                request = HttpRequest(
                    "GET", urllib.parse.urljoin(next_link, _parsed_next_link.path), params=_next_request_params
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)
                request.method = "GET"
            return request

        async def extract_data(pipeline_response):
            deserialized = self._deserialize("SecurityAssessmentMetadataList", pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)  # type: ignore
            return deserialized.next_link or None, AsyncList(list_of_elem)

        async def get_next(next_link=None):
            request = prepare_request(next_link)

            _stream = False
            pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
                request, stream=_stream, **kwargs
            )
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response, error_format=ARMErrorFormat)

            return pipeline_response

        return AsyncItemPaged(get_next, extract_data)

    list.metadata = {"url": "/providers/Microsoft.Security/assessmentMetadata"}

    @distributed_trace_async
    async def get(self, assessment_metadata_name: str, **kwargs: Any) -> _models.SecurityAssessmentMetadata:
        """Get metadata information on an assessment type.

        :param assessment_metadata_name: The Assessment Key - Unique key for the assessment type.
         Required.
        :type assessment_metadata_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: SecurityAssessmentMetadata or the result of cls(response)
        :rtype: ~azure.mgmt.security.v2020_01_01.models.SecurityAssessmentMetadata
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: Literal["2020-01-01"] = kwargs.pop("api_version", _params.pop("api-version", "2020-01-01"))
        cls: ClsType[_models.SecurityAssessmentMetadata] = kwargs.pop("cls", None)

        request = build_get_request(
            assessment_metadata_name=assessment_metadata_name,
            api_version=api_version,
            template_url=self.get.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        _stream = False
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize("SecurityAssessmentMetadata", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get.metadata = {"url": "/providers/Microsoft.Security/assessmentMetadata/{assessmentMetadataName}"}

    @distributed_trace
    def list_by_subscription(self, **kwargs: Any) -> AsyncIterable["_models.SecurityAssessmentMetadata"]:
        """Get metadata information on all assessment types in a specific subscription.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either SecurityAssessmentMetadata or the result of
         cls(response)
        :rtype:
         ~azure.core.async_paging.AsyncItemPaged[~azure.mgmt.security.v2020_01_01.models.SecurityAssessmentMetadata]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: Literal["2020-01-01"] = kwargs.pop("api_version", _params.pop("api-version", "2020-01-01"))
        cls: ClsType[_models.SecurityAssessmentMetadataList] = kwargs.pop("cls", None)

        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        def prepare_request(next_link=None):
            if not next_link:

                request = build_list_by_subscription_request(
                    subscription_id=self._config.subscription_id,
                    api_version=api_version,
                    template_url=self.list_by_subscription.metadata["url"],
                    headers=_headers,
                    params=_params,
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)

            else:
                # make call to next link with the client's api-version
                _parsed_next_link = urllib.parse.urlparse(next_link)
                _next_request_params = case_insensitive_dict(
                    {
                        key: [urllib.parse.quote(v) for v in value]
                        for key, value in urllib.parse.parse_qs(_parsed_next_link.query).items()
                    }
                )
                _next_request_params["api-version"] = self._config.api_version
                request = HttpRequest(
                    "GET", urllib.parse.urljoin(next_link, _parsed_next_link.path), params=_next_request_params
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)
                request.method = "GET"
            return request

        async def extract_data(pipeline_response):
            deserialized = self._deserialize("SecurityAssessmentMetadataList", pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)  # type: ignore
            return deserialized.next_link or None, AsyncList(list_of_elem)

        async def get_next(next_link=None):
            request = prepare_request(next_link)

            _stream = False
            pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
                request, stream=_stream, **kwargs
            )
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response, error_format=ARMErrorFormat)

            return pipeline_response

        return AsyncItemPaged(get_next, extract_data)

    list_by_subscription.metadata = {
        "url": "/subscriptions/{subscriptionId}/providers/Microsoft.Security/assessmentMetadata"
    }

    @distributed_trace_async
    async def get_in_subscription(
        self, assessment_metadata_name: str, **kwargs: Any
    ) -> _models.SecurityAssessmentMetadata:
        """Get metadata information on an assessment type in a specific subscription.

        :param assessment_metadata_name: The Assessment Key - Unique key for the assessment type.
         Required.
        :type assessment_metadata_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: SecurityAssessmentMetadata or the result of cls(response)
        :rtype: ~azure.mgmt.security.v2020_01_01.models.SecurityAssessmentMetadata
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: Literal["2020-01-01"] = kwargs.pop("api_version", _params.pop("api-version", "2020-01-01"))
        cls: ClsType[_models.SecurityAssessmentMetadata] = kwargs.pop("cls", None)

        request = build_get_in_subscription_request(
            assessment_metadata_name=assessment_metadata_name,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            template_url=self.get_in_subscription.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        _stream = False
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize("SecurityAssessmentMetadata", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_in_subscription.metadata = {
        "url": "/subscriptions/{subscriptionId}/providers/Microsoft.Security/assessmentMetadata/{assessmentMetadataName}"
    }

    @overload
    async def create_in_subscription(
        self,
        assessment_metadata_name: str,
        assessment_metadata: _models.SecurityAssessmentMetadata,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.SecurityAssessmentMetadata:
        """Create metadata information on an assessment type in a specific subscription.

        :param assessment_metadata_name: The Assessment Key - Unique key for the assessment type.
         Required.
        :type assessment_metadata_name: str
        :param assessment_metadata: AssessmentMetadata object. Required.
        :type assessment_metadata: ~azure.mgmt.security.v2020_01_01.models.SecurityAssessmentMetadata
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: SecurityAssessmentMetadata or the result of cls(response)
        :rtype: ~azure.mgmt.security.v2020_01_01.models.SecurityAssessmentMetadata
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def create_in_subscription(
        self,
        assessment_metadata_name: str,
        assessment_metadata: IO,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.SecurityAssessmentMetadata:
        """Create metadata information on an assessment type in a specific subscription.

        :param assessment_metadata_name: The Assessment Key - Unique key for the assessment type.
         Required.
        :type assessment_metadata_name: str
        :param assessment_metadata: AssessmentMetadata object. Required.
        :type assessment_metadata: IO
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: SecurityAssessmentMetadata or the result of cls(response)
        :rtype: ~azure.mgmt.security.v2020_01_01.models.SecurityAssessmentMetadata
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace_async
    async def create_in_subscription(
        self,
        assessment_metadata_name: str,
        assessment_metadata: Union[_models.SecurityAssessmentMetadata, IO],
        **kwargs: Any
    ) -> _models.SecurityAssessmentMetadata:
        """Create metadata information on an assessment type in a specific subscription.

        :param assessment_metadata_name: The Assessment Key - Unique key for the assessment type.
         Required.
        :type assessment_metadata_name: str
        :param assessment_metadata: AssessmentMetadata object. Is either a SecurityAssessmentMetadata
         type or a IO type. Required.
        :type assessment_metadata: ~azure.mgmt.security.v2020_01_01.models.SecurityAssessmentMetadata
         or IO
        :keyword content_type: Body Parameter content-type. Known values are: 'application/json'.
         Default value is None.
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: SecurityAssessmentMetadata or the result of cls(response)
        :rtype: ~azure.mgmt.security.v2020_01_01.models.SecurityAssessmentMetadata
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: Literal["2020-01-01"] = kwargs.pop("api_version", _params.pop("api-version", "2020-01-01"))
        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[_models.SecurityAssessmentMetadata] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(assessment_metadata, (IO, bytes)):
            _content = assessment_metadata
        else:
            _json = self._serialize.body(assessment_metadata, "SecurityAssessmentMetadata")

        request = build_create_in_subscription_request(
            assessment_metadata_name=assessment_metadata_name,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            content_type=content_type,
            json=_json,
            content=_content,
            template_url=self.create_in_subscription.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        _stream = False
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize("SecurityAssessmentMetadata", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    create_in_subscription.metadata = {
        "url": "/subscriptions/{subscriptionId}/providers/Microsoft.Security/assessmentMetadata/{assessmentMetadataName}"
    }

    @distributed_trace_async
    async def delete_in_subscription(  # pylint: disable=inconsistent-return-statements
        self, assessment_metadata_name: str, **kwargs: Any
    ) -> None:
        """Delete metadata information on an assessment type in a specific subscription, will cause the
        deletion of all the assessments of that type in that subscription.

        :param assessment_metadata_name: The Assessment Key - Unique key for the assessment type.
         Required.
        :type assessment_metadata_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: Literal["2020-01-01"] = kwargs.pop("api_version", _params.pop("api-version", "2020-01-01"))
        cls: ClsType[None] = kwargs.pop("cls", None)

        request = build_delete_in_subscription_request(
            assessment_metadata_name=assessment_metadata_name,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            template_url=self.delete_in_subscription.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        _stream = False
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    delete_in_subscription.metadata = {
        "url": "/subscriptions/{subscriptionId}/providers/Microsoft.Security/assessmentMetadata/{assessmentMetadataName}"
    }
