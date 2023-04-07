# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import sys
from typing import Any, Callable, Dict, IO, Iterable, Optional, TypeVar, Union, overload

from azure.core.exceptions import (
    ClientAuthenticationError,
    HttpResponseError,
    ResourceExistsError,
    ResourceNotFoundError,
    ResourceNotModifiedError,
    map_error,
)
from azure.core.paging import ItemPaged
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpResponse
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator import distributed_trace
from azure.core.utils import case_insensitive_dict
from azure.mgmt.core.exceptions import ARMErrorFormat

from .. import models as _models
from ..._serialization import Serializer
from .._vendor import _convert_request, _format_url_section

if sys.version_info >= (3, 8):
    from typing import Literal  # pylint: disable=no-name-in-module, ungrouped-imports
else:
    from typing_extensions import Literal  # type: ignore  # pylint: disable=ungrouped-imports
T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

_SERIALIZER = Serializer()
_SERIALIZER.client_side_validation = False


def build_list_request(subscription_id: str, *, filter: Optional[str] = None, **kwargs: Any) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version: Literal["2021-12-01-preview"] = kwargs.pop(
        "api_version", _params.pop("api-version", "2021-12-01-preview")
    )
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop(
        "template_url",
        "/subscriptions/{subscriptionId}/providers/Microsoft.Authorization/accessReviewScheduleDefinitions",
    )  # pylint: disable=line-too-long
    path_format_arguments = {
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, "str"),
    }

    _url: str = _format_url_section(_url, **path_format_arguments)  # type: ignore

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")
    if filter is not None:
        _params["$filter"] = _SERIALIZER.query("filter", filter, "str", skip_quote=True)

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=_url, params=_params, headers=_headers, **kwargs)


def build_get_by_id_request(schedule_definition_id: str, subscription_id: str, **kwargs: Any) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version: Literal["2021-12-01-preview"] = kwargs.pop(
        "api_version", _params.pop("api-version", "2021-12-01-preview")
    )
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop(
        "template_url",
        "/subscriptions/{subscriptionId}/providers/Microsoft.Authorization/accessReviewScheduleDefinitions/{scheduleDefinitionId}",
    )  # pylint: disable=line-too-long
    path_format_arguments = {
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, "str"),
        "scheduleDefinitionId": _SERIALIZER.url("schedule_definition_id", schedule_definition_id, "str"),
    }

    _url: str = _format_url_section(_url, **path_format_arguments)  # type: ignore

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=_url, params=_params, headers=_headers, **kwargs)


def build_delete_by_id_request(schedule_definition_id: str, subscription_id: str, **kwargs: Any) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version: Literal["2021-12-01-preview"] = kwargs.pop(
        "api_version", _params.pop("api-version", "2021-12-01-preview")
    )
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop(
        "template_url",
        "/subscriptions/{subscriptionId}/providers/Microsoft.Authorization/accessReviewScheduleDefinitions/{scheduleDefinitionId}",
    )  # pylint: disable=line-too-long
    path_format_arguments = {
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, "str"),
        "scheduleDefinitionId": _SERIALIZER.url("schedule_definition_id", schedule_definition_id, "str"),
    }

    _url: str = _format_url_section(_url, **path_format_arguments)  # type: ignore

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="DELETE", url=_url, params=_params, headers=_headers, **kwargs)


def build_create_or_update_by_id_request(
    schedule_definition_id: str, subscription_id: str, **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version: Literal["2021-12-01-preview"] = kwargs.pop(
        "api_version", _params.pop("api-version", "2021-12-01-preview")
    )
    content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop(
        "template_url",
        "/subscriptions/{subscriptionId}/providers/Microsoft.Authorization/accessReviewScheduleDefinitions/{scheduleDefinitionId}",
    )  # pylint: disable=line-too-long
    path_format_arguments = {
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, "str"),
        "scheduleDefinitionId": _SERIALIZER.url("schedule_definition_id", schedule_definition_id, "str"),
    }

    _url: str = _format_url_section(_url, **path_format_arguments)  # type: ignore

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    if content_type is not None:
        _headers["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="PUT", url=_url, params=_params, headers=_headers, **kwargs)


def build_stop_request(schedule_definition_id: str, subscription_id: str, **kwargs: Any) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version: Literal["2021-12-01-preview"] = kwargs.pop(
        "api_version", _params.pop("api-version", "2021-12-01-preview")
    )
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop(
        "template_url",
        "/subscriptions/{subscriptionId}/providers/Microsoft.Authorization/accessReviewScheduleDefinitions/{scheduleDefinitionId}/stop",
    )  # pylint: disable=line-too-long
    path_format_arguments = {
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, "str"),
        "scheduleDefinitionId": _SERIALIZER.url("schedule_definition_id", schedule_definition_id, "str"),
    }

    _url: str = _format_url_section(_url, **path_format_arguments)  # type: ignore

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="POST", url=_url, params=_params, headers=_headers, **kwargs)


class AccessReviewScheduleDefinitionsOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~azure.mgmt.authorization.v2021_12_01_preview.AuthorizationManagementClient`'s
        :attr:`access_review_schedule_definitions` attribute.
    """

    models = _models

    def __init__(self, *args, **kwargs):
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    @distributed_trace
    def list(self, filter: Optional[str] = None, **kwargs: Any) -> Iterable["_models.AccessReviewScheduleDefinition"]:
        """Get access review schedule definitions.

        :param filter: The filter to apply on the operation. Other than standard filters, one custom
         filter option is supported : 'assignedToMeToReview()'. When one specified
         $filter=assignedToMeToReview(), only items that are assigned to the calling user to review are
         returned. Default value is None.
        :type filter: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either AccessReviewScheduleDefinition or the result of
         cls(response)
        :rtype:
         ~azure.core.paging.ItemPaged[~azure.mgmt.authorization.v2021_12_01_preview.models.AccessReviewScheduleDefinition]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: Literal["2021-12-01-preview"] = kwargs.pop(
            "api_version", _params.pop("api-version", "2021-12-01-preview")
        )
        cls: ClsType[_models.AccessReviewScheduleDefinitionListResult] = kwargs.pop("cls", None)

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
                    subscription_id=self._config.subscription_id,
                    filter=filter,
                    api_version=api_version,
                    template_url=self.list.metadata["url"],
                    headers=_headers,
                    params=_params,
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)

            else:
                request = HttpRequest("GET", next_link)
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)
                request.method = "GET"
            return request

        def extract_data(pipeline_response):
            deserialized = self._deserialize("AccessReviewScheduleDefinitionListResult", pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)  # type: ignore
            return deserialized.next_link or None, iter(list_of_elem)

        def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response: PipelineResponse = self._client._pipeline.run(  # pylint: disable=protected-access
                request, stream=False, **kwargs
            )
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                error = self._deserialize.failsafe_deserialize(_models.ErrorDefinition, pipeline_response)
                raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

            return pipeline_response

        return ItemPaged(get_next, extract_data)

    list.metadata = {
        "url": "/subscriptions/{subscriptionId}/providers/Microsoft.Authorization/accessReviewScheduleDefinitions"
    }

    @distributed_trace
    def get_by_id(self, schedule_definition_id: str, **kwargs: Any) -> _models.AccessReviewScheduleDefinition:
        """Get single access review definition.

        :param schedule_definition_id: The id of the access review schedule definition. Required.
        :type schedule_definition_id: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: AccessReviewScheduleDefinition or the result of cls(response)
        :rtype: ~azure.mgmt.authorization.v2021_12_01_preview.models.AccessReviewScheduleDefinition
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

        api_version: Literal["2021-12-01-preview"] = kwargs.pop(
            "api_version", _params.pop("api-version", "2021-12-01-preview")
        )
        cls: ClsType[_models.AccessReviewScheduleDefinition] = kwargs.pop("cls", None)

        request = build_get_by_id_request(
            schedule_definition_id=schedule_definition_id,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            template_url=self.get_by_id.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response: PipelineResponse = self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorDefinition, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize("AccessReviewScheduleDefinition", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_by_id.metadata = {
        "url": "/subscriptions/{subscriptionId}/providers/Microsoft.Authorization/accessReviewScheduleDefinitions/{scheduleDefinitionId}"
    }

    @distributed_trace
    def delete_by_id(  # pylint: disable=inconsistent-return-statements
        self, schedule_definition_id: str, **kwargs: Any
    ) -> None:
        """Delete access review schedule definition.

        :param schedule_definition_id: The id of the access review schedule definition. Required.
        :type schedule_definition_id: str
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

        api_version: Literal["2021-12-01-preview"] = kwargs.pop(
            "api_version", _params.pop("api-version", "2021-12-01-preview")
        )
        cls: ClsType[None] = kwargs.pop("cls", None)

        request = build_delete_by_id_request(
            schedule_definition_id=schedule_definition_id,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            template_url=self.delete_by_id.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response: PipelineResponse = self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200, 204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorDefinition, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    delete_by_id.metadata = {
        "url": "/subscriptions/{subscriptionId}/providers/Microsoft.Authorization/accessReviewScheduleDefinitions/{scheduleDefinitionId}"
    }

    @overload
    def create_or_update_by_id(
        self,
        schedule_definition_id: str,
        properties: _models.AccessReviewScheduleDefinitionProperties,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.AccessReviewScheduleDefinition:
        """Create or Update access review schedule definition.

        :param schedule_definition_id: The id of the access review schedule definition. Required.
        :type schedule_definition_id: str
        :param properties: Access review schedule definition properties. Required.
        :type properties:
         ~azure.mgmt.authorization.v2021_12_01_preview.models.AccessReviewScheduleDefinitionProperties
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: AccessReviewScheduleDefinition or the result of cls(response)
        :rtype: ~azure.mgmt.authorization.v2021_12_01_preview.models.AccessReviewScheduleDefinition
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    def create_or_update_by_id(
        self, schedule_definition_id: str, properties: IO, *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.AccessReviewScheduleDefinition:
        """Create or Update access review schedule definition.

        :param schedule_definition_id: The id of the access review schedule definition. Required.
        :type schedule_definition_id: str
        :param properties: Access review schedule definition properties. Required.
        :type properties: IO
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: AccessReviewScheduleDefinition or the result of cls(response)
        :rtype: ~azure.mgmt.authorization.v2021_12_01_preview.models.AccessReviewScheduleDefinition
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace
    def create_or_update_by_id(
        self,
        schedule_definition_id: str,
        properties: Union[_models.AccessReviewScheduleDefinitionProperties, IO],
        **kwargs: Any
    ) -> _models.AccessReviewScheduleDefinition:
        """Create or Update access review schedule definition.

        :param schedule_definition_id: The id of the access review schedule definition. Required.
        :type schedule_definition_id: str
        :param properties: Access review schedule definition properties. Is either a
         AccessReviewScheduleDefinitionProperties type or a IO type. Required.
        :type properties:
         ~azure.mgmt.authorization.v2021_12_01_preview.models.AccessReviewScheduleDefinitionProperties
         or IO
        :keyword content_type: Body Parameter content-type. Known values are: 'application/json'.
         Default value is None.
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: AccessReviewScheduleDefinition or the result of cls(response)
        :rtype: ~azure.mgmt.authorization.v2021_12_01_preview.models.AccessReviewScheduleDefinition
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

        api_version: Literal["2021-12-01-preview"] = kwargs.pop(
            "api_version", _params.pop("api-version", "2021-12-01-preview")
        )
        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[_models.AccessReviewScheduleDefinition] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(properties, (IO, bytes)):
            _content = properties
        else:
            _json = self._serialize.body(properties, "AccessReviewScheduleDefinitionProperties")

        request = build_create_or_update_by_id_request(
            schedule_definition_id=schedule_definition_id,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            content_type=content_type,
            json=_json,
            content=_content,
            template_url=self.create_or_update_by_id.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response: PipelineResponse = self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorDefinition, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize("AccessReviewScheduleDefinition", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    create_or_update_by_id.metadata = {
        "url": "/subscriptions/{subscriptionId}/providers/Microsoft.Authorization/accessReviewScheduleDefinitions/{scheduleDefinitionId}"
    }

    @distributed_trace
    def stop(  # pylint: disable=inconsistent-return-statements
        self, schedule_definition_id: str, **kwargs: Any
    ) -> None:
        """Stop access review definition.

        :param schedule_definition_id: The id of the access review schedule definition. Required.
        :type schedule_definition_id: str
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

        api_version: Literal["2021-12-01-preview"] = kwargs.pop(
            "api_version", _params.pop("api-version", "2021-12-01-preview")
        )
        cls: ClsType[None] = kwargs.pop("cls", None)

        request = build_stop_request(
            schedule_definition_id=schedule_definition_id,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            template_url=self.stop.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response: PipelineResponse = self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorDefinition, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    stop.metadata = {
        "url": "/subscriptions/{subscriptionId}/providers/Microsoft.Authorization/accessReviewScheduleDefinitions/{scheduleDefinitionId}/stop"
    }
