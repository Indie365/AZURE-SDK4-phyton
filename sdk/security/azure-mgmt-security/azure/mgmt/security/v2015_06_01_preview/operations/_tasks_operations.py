# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import sys
from typing import Any, Callable, Dict, Iterable, Optional, TypeVar, Union
import urllib.parse

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

    api_version: Literal["2015-06-01-preview"] = kwargs.pop(
        "api_version", _params.pop("api-version", "2015-06-01-preview")
    )
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop("template_url", "/subscriptions/{subscriptionId}/providers/Microsoft.Security/tasks")
    path_format_arguments = {
        "subscriptionId": _SERIALIZER.url(
            "subscription_id", subscription_id, "str", pattern=r"^[0-9A-Fa-f]{8}-([0-9A-Fa-f]{4}-){3}[0-9A-Fa-f]{12}$"
        ),
    }

    _url: str = _format_url_section(_url, **path_format_arguments)  # type: ignore

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")
    if filter is not None:
        _params["$filter"] = _SERIALIZER.query("filter", filter, "str")

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=_url, params=_params, headers=_headers, **kwargs)


def build_list_by_home_region_request(
    asc_location: str, subscription_id: str, *, filter: Optional[str] = None, **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version: Literal["2015-06-01-preview"] = kwargs.pop(
        "api_version", _params.pop("api-version", "2015-06-01-preview")
    )
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop(
        "template_url", "/subscriptions/{subscriptionId}/providers/Microsoft.Security/locations/{ascLocation}/tasks"
    )  # pylint: disable=line-too-long
    path_format_arguments = {
        "subscriptionId": _SERIALIZER.url(
            "subscription_id", subscription_id, "str", pattern=r"^[0-9A-Fa-f]{8}-([0-9A-Fa-f]{4}-){3}[0-9A-Fa-f]{12}$"
        ),
        "ascLocation": _SERIALIZER.url("asc_location", asc_location, "str"),
    }

    _url: str = _format_url_section(_url, **path_format_arguments)  # type: ignore

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")
    if filter is not None:
        _params["$filter"] = _SERIALIZER.query("filter", filter, "str")

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=_url, params=_params, headers=_headers, **kwargs)


def build_get_subscription_level_task_request(
    asc_location: str, task_name: str, subscription_id: str, **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version: Literal["2015-06-01-preview"] = kwargs.pop(
        "api_version", _params.pop("api-version", "2015-06-01-preview")
    )
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop(
        "template_url",
        "/subscriptions/{subscriptionId}/providers/Microsoft.Security/locations/{ascLocation}/tasks/{taskName}",
    )  # pylint: disable=line-too-long
    path_format_arguments = {
        "subscriptionId": _SERIALIZER.url(
            "subscription_id", subscription_id, "str", pattern=r"^[0-9A-Fa-f]{8}-([0-9A-Fa-f]{4}-){3}[0-9A-Fa-f]{12}$"
        ),
        "ascLocation": _SERIALIZER.url("asc_location", asc_location, "str"),
        "taskName": _SERIALIZER.url("task_name", task_name, "str"),
    }

    _url: str = _format_url_section(_url, **path_format_arguments)  # type: ignore

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=_url, params=_params, headers=_headers, **kwargs)


def build_update_subscription_level_task_state_request(
    asc_location: str,
    task_name: str,
    task_update_action_type: Union[str, _models.TaskUpdateActionType],
    subscription_id: str,
    **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version: Literal["2015-06-01-preview"] = kwargs.pop(
        "api_version", _params.pop("api-version", "2015-06-01-preview")
    )
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop(
        "template_url",
        "/subscriptions/{subscriptionId}/providers/Microsoft.Security/locations/{ascLocation}/tasks/{taskName}/{taskUpdateActionType}",
    )  # pylint: disable=line-too-long
    path_format_arguments = {
        "subscriptionId": _SERIALIZER.url(
            "subscription_id", subscription_id, "str", pattern=r"^[0-9A-Fa-f]{8}-([0-9A-Fa-f]{4}-){3}[0-9A-Fa-f]{12}$"
        ),
        "ascLocation": _SERIALIZER.url("asc_location", asc_location, "str"),
        "taskName": _SERIALIZER.url("task_name", task_name, "str"),
        "taskUpdateActionType": _SERIALIZER.url("task_update_action_type", task_update_action_type, "str"),
    }

    _url: str = _format_url_section(_url, **path_format_arguments)  # type: ignore

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="POST", url=_url, params=_params, headers=_headers, **kwargs)


def build_list_by_resource_group_request(
    resource_group_name: str, asc_location: str, subscription_id: str, *, filter: Optional[str] = None, **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version: Literal["2015-06-01-preview"] = kwargs.pop(
        "api_version", _params.pop("api-version", "2015-06-01-preview")
    )
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop(
        "template_url",
        "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Security/locations/{ascLocation}/tasks",
    )  # pylint: disable=line-too-long
    path_format_arguments = {
        "subscriptionId": _SERIALIZER.url(
            "subscription_id", subscription_id, "str", pattern=r"^[0-9A-Fa-f]{8}-([0-9A-Fa-f]{4}-){3}[0-9A-Fa-f]{12}$"
        ),
        "resourceGroupName": _SERIALIZER.url(
            "resource_group_name", resource_group_name, "str", max_length=90, min_length=1, pattern=r"^[-\w\._\(\)]+$"
        ),
        "ascLocation": _SERIALIZER.url("asc_location", asc_location, "str"),
    }

    _url: str = _format_url_section(_url, **path_format_arguments)  # type: ignore

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")
    if filter is not None:
        _params["$filter"] = _SERIALIZER.query("filter", filter, "str")

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=_url, params=_params, headers=_headers, **kwargs)


def build_get_resource_group_level_task_request(
    resource_group_name: str, asc_location: str, task_name: str, subscription_id: str, **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version: Literal["2015-06-01-preview"] = kwargs.pop(
        "api_version", _params.pop("api-version", "2015-06-01-preview")
    )
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop(
        "template_url",
        "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Security/locations/{ascLocation}/tasks/{taskName}",
    )  # pylint: disable=line-too-long
    path_format_arguments = {
        "subscriptionId": _SERIALIZER.url(
            "subscription_id", subscription_id, "str", pattern=r"^[0-9A-Fa-f]{8}-([0-9A-Fa-f]{4}-){3}[0-9A-Fa-f]{12}$"
        ),
        "resourceGroupName": _SERIALIZER.url(
            "resource_group_name", resource_group_name, "str", max_length=90, min_length=1, pattern=r"^[-\w\._\(\)]+$"
        ),
        "ascLocation": _SERIALIZER.url("asc_location", asc_location, "str"),
        "taskName": _SERIALIZER.url("task_name", task_name, "str"),
    }

    _url: str = _format_url_section(_url, **path_format_arguments)  # type: ignore

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=_url, params=_params, headers=_headers, **kwargs)


def build_update_resource_group_level_task_state_request(
    resource_group_name: str,
    asc_location: str,
    task_name: str,
    task_update_action_type: Union[str, _models.TaskUpdateActionType],
    subscription_id: str,
    **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version: Literal["2015-06-01-preview"] = kwargs.pop(
        "api_version", _params.pop("api-version", "2015-06-01-preview")
    )
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop(
        "template_url",
        "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Security/locations/{ascLocation}/tasks/{taskName}/{taskUpdateActionType}",
    )  # pylint: disable=line-too-long
    path_format_arguments = {
        "subscriptionId": _SERIALIZER.url(
            "subscription_id", subscription_id, "str", pattern=r"^[0-9A-Fa-f]{8}-([0-9A-Fa-f]{4}-){3}[0-9A-Fa-f]{12}$"
        ),
        "resourceGroupName": _SERIALIZER.url(
            "resource_group_name", resource_group_name, "str", max_length=90, min_length=1, pattern=r"^[-\w\._\(\)]+$"
        ),
        "ascLocation": _SERIALIZER.url("asc_location", asc_location, "str"),
        "taskName": _SERIALIZER.url("task_name", task_name, "str"),
        "taskUpdateActionType": _SERIALIZER.url("task_update_action_type", task_update_action_type, "str"),
    }

    _url: str = _format_url_section(_url, **path_format_arguments)  # type: ignore

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="POST", url=_url, params=_params, headers=_headers, **kwargs)


class TasksOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~azure.mgmt.security.v2015_06_01_preview.SecurityCenter`'s
        :attr:`tasks` attribute.
    """

    models = _models

    def __init__(self, *args, **kwargs):
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    @distributed_trace
    def list(self, filter: Optional[str] = None, **kwargs: Any) -> Iterable["_models.SecurityTask"]:
        """Recommended tasks that will help improve the security of the subscription proactively.

        :param filter: OData filter. Optional. Default value is None.
        :type filter: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either SecurityTask or the result of cls(response)
        :rtype:
         ~azure.core.paging.ItemPaged[~azure.mgmt.security.v2015_06_01_preview.models.SecurityTask]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: Literal["2015-06-01-preview"] = kwargs.pop(
            "api_version", _params.pop("api-version", "2015-06-01-preview")
        )
        cls: ClsType[_models.SecurityTaskList] = kwargs.pop("cls", None)

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

        def extract_data(pipeline_response):
            deserialized = self._deserialize("SecurityTaskList", pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)  # type: ignore
            return deserialized.next_link or None, iter(list_of_elem)

        def get_next(next_link=None):
            request = prepare_request(next_link)

            _stream = False
            pipeline_response: PipelineResponse = self._client._pipeline.run(  # pylint: disable=protected-access
                request, stream=_stream, **kwargs
            )
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response, error_format=ARMErrorFormat)

            return pipeline_response

        return ItemPaged(get_next, extract_data)

    list.metadata = {"url": "/subscriptions/{subscriptionId}/providers/Microsoft.Security/tasks"}

    @distributed_trace
    def list_by_home_region(
        self, asc_location: str, filter: Optional[str] = None, **kwargs: Any
    ) -> Iterable["_models.SecurityTask"]:
        """Recommended tasks that will help improve the security of the subscription proactively.

        :param asc_location: The location where ASC stores the data of the subscription. can be
         retrieved from Get locations. Required.
        :type asc_location: str
        :param filter: OData filter. Optional. Default value is None.
        :type filter: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either SecurityTask or the result of cls(response)
        :rtype:
         ~azure.core.paging.ItemPaged[~azure.mgmt.security.v2015_06_01_preview.models.SecurityTask]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: Literal["2015-06-01-preview"] = kwargs.pop(
            "api_version", _params.pop("api-version", "2015-06-01-preview")
        )
        cls: ClsType[_models.SecurityTaskList] = kwargs.pop("cls", None)

        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        def prepare_request(next_link=None):
            if not next_link:

                request = build_list_by_home_region_request(
                    asc_location=asc_location,
                    subscription_id=self._config.subscription_id,
                    filter=filter,
                    api_version=api_version,
                    template_url=self.list_by_home_region.metadata["url"],
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

        def extract_data(pipeline_response):
            deserialized = self._deserialize("SecurityTaskList", pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)  # type: ignore
            return deserialized.next_link or None, iter(list_of_elem)

        def get_next(next_link=None):
            request = prepare_request(next_link)

            _stream = False
            pipeline_response: PipelineResponse = self._client._pipeline.run(  # pylint: disable=protected-access
                request, stream=_stream, **kwargs
            )
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response, error_format=ARMErrorFormat)

            return pipeline_response

        return ItemPaged(get_next, extract_data)

    list_by_home_region.metadata = {
        "url": "/subscriptions/{subscriptionId}/providers/Microsoft.Security/locations/{ascLocation}/tasks"
    }

    @distributed_trace
    def get_subscription_level_task(self, asc_location: str, task_name: str, **kwargs: Any) -> _models.SecurityTask:
        """Recommended tasks that will help improve the security of the subscription proactively.

        :param asc_location: The location where ASC stores the data of the subscription. can be
         retrieved from Get locations. Required.
        :type asc_location: str
        :param task_name: Name of the task object, will be a GUID. Required.
        :type task_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: SecurityTask or the result of cls(response)
        :rtype: ~azure.mgmt.security.v2015_06_01_preview.models.SecurityTask
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

        api_version: Literal["2015-06-01-preview"] = kwargs.pop(
            "api_version", _params.pop("api-version", "2015-06-01-preview")
        )
        cls: ClsType[_models.SecurityTask] = kwargs.pop("cls", None)

        request = build_get_subscription_level_task_request(
            asc_location=asc_location,
            task_name=task_name,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            template_url=self.get_subscription_level_task.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        _stream = False
        pipeline_response: PipelineResponse = self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize("SecurityTask", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_subscription_level_task.metadata = {
        "url": "/subscriptions/{subscriptionId}/providers/Microsoft.Security/locations/{ascLocation}/tasks/{taskName}"
    }

    @distributed_trace
    def update_subscription_level_task_state(  # pylint: disable=inconsistent-return-statements
        self,
        asc_location: str,
        task_name: str,
        task_update_action_type: Union[str, _models.TaskUpdateActionType],
        **kwargs: Any
    ) -> None:
        """Recommended tasks that will help improve the security of the subscription proactively.

        :param asc_location: The location where ASC stores the data of the subscription. can be
         retrieved from Get locations. Required.
        :type asc_location: str
        :param task_name: Name of the task object, will be a GUID. Required.
        :type task_name: str
        :param task_update_action_type: Type of the action to do on the task. Known values are:
         "Activate", "Dismiss", "Start", "Resolve", and "Close". Required.
        :type task_update_action_type: str or
         ~azure.mgmt.security.v2015_06_01_preview.models.TaskUpdateActionType
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

        api_version: Literal["2015-06-01-preview"] = kwargs.pop(
            "api_version", _params.pop("api-version", "2015-06-01-preview")
        )
        cls: ClsType[None] = kwargs.pop("cls", None)

        request = build_update_subscription_level_task_state_request(
            asc_location=asc_location,
            task_name=task_name,
            task_update_action_type=task_update_action_type,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            template_url=self.update_subscription_level_task_state.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        _stream = False
        pipeline_response: PipelineResponse = self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    update_subscription_level_task_state.metadata = {
        "url": "/subscriptions/{subscriptionId}/providers/Microsoft.Security/locations/{ascLocation}/tasks/{taskName}/{taskUpdateActionType}"
    }

    @distributed_trace
    def list_by_resource_group(
        self, resource_group_name: str, asc_location: str, filter: Optional[str] = None, **kwargs: Any
    ) -> Iterable["_models.SecurityTask"]:
        """Recommended tasks that will help improve the security of the subscription proactively.

        :param resource_group_name: The name of the resource group within the user's subscription. The
         name is case insensitive. Required.
        :type resource_group_name: str
        :param asc_location: The location where ASC stores the data of the subscription. can be
         retrieved from Get locations. Required.
        :type asc_location: str
        :param filter: OData filter. Optional. Default value is None.
        :type filter: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either SecurityTask or the result of cls(response)
        :rtype:
         ~azure.core.paging.ItemPaged[~azure.mgmt.security.v2015_06_01_preview.models.SecurityTask]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: Literal["2015-06-01-preview"] = kwargs.pop(
            "api_version", _params.pop("api-version", "2015-06-01-preview")
        )
        cls: ClsType[_models.SecurityTaskList] = kwargs.pop("cls", None)

        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        def prepare_request(next_link=None):
            if not next_link:

                request = build_list_by_resource_group_request(
                    resource_group_name=resource_group_name,
                    asc_location=asc_location,
                    subscription_id=self._config.subscription_id,
                    filter=filter,
                    api_version=api_version,
                    template_url=self.list_by_resource_group.metadata["url"],
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

        def extract_data(pipeline_response):
            deserialized = self._deserialize("SecurityTaskList", pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)  # type: ignore
            return deserialized.next_link or None, iter(list_of_elem)

        def get_next(next_link=None):
            request = prepare_request(next_link)

            _stream = False
            pipeline_response: PipelineResponse = self._client._pipeline.run(  # pylint: disable=protected-access
                request, stream=_stream, **kwargs
            )
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response, error_format=ARMErrorFormat)

            return pipeline_response

        return ItemPaged(get_next, extract_data)

    list_by_resource_group.metadata = {
        "url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Security/locations/{ascLocation}/tasks"
    }

    @distributed_trace
    def get_resource_group_level_task(
        self, resource_group_name: str, asc_location: str, task_name: str, **kwargs: Any
    ) -> _models.SecurityTask:
        """Recommended tasks that will help improve the security of the subscription proactively.

        :param resource_group_name: The name of the resource group within the user's subscription. The
         name is case insensitive. Required.
        :type resource_group_name: str
        :param asc_location: The location where ASC stores the data of the subscription. can be
         retrieved from Get locations. Required.
        :type asc_location: str
        :param task_name: Name of the task object, will be a GUID. Required.
        :type task_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: SecurityTask or the result of cls(response)
        :rtype: ~azure.mgmt.security.v2015_06_01_preview.models.SecurityTask
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

        api_version: Literal["2015-06-01-preview"] = kwargs.pop(
            "api_version", _params.pop("api-version", "2015-06-01-preview")
        )
        cls: ClsType[_models.SecurityTask] = kwargs.pop("cls", None)

        request = build_get_resource_group_level_task_request(
            resource_group_name=resource_group_name,
            asc_location=asc_location,
            task_name=task_name,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            template_url=self.get_resource_group_level_task.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        _stream = False
        pipeline_response: PipelineResponse = self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize("SecurityTask", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_resource_group_level_task.metadata = {
        "url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Security/locations/{ascLocation}/tasks/{taskName}"
    }

    @distributed_trace
    def update_resource_group_level_task_state(  # pylint: disable=inconsistent-return-statements
        self,
        resource_group_name: str,
        asc_location: str,
        task_name: str,
        task_update_action_type: Union[str, _models.TaskUpdateActionType],
        **kwargs: Any
    ) -> None:
        """Recommended tasks that will help improve the security of the subscription proactively.

        :param resource_group_name: The name of the resource group within the user's subscription. The
         name is case insensitive. Required.
        :type resource_group_name: str
        :param asc_location: The location where ASC stores the data of the subscription. can be
         retrieved from Get locations. Required.
        :type asc_location: str
        :param task_name: Name of the task object, will be a GUID. Required.
        :type task_name: str
        :param task_update_action_type: Type of the action to do on the task. Known values are:
         "Activate", "Dismiss", "Start", "Resolve", and "Close". Required.
        :type task_update_action_type: str or
         ~azure.mgmt.security.v2015_06_01_preview.models.TaskUpdateActionType
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

        api_version: Literal["2015-06-01-preview"] = kwargs.pop(
            "api_version", _params.pop("api-version", "2015-06-01-preview")
        )
        cls: ClsType[None] = kwargs.pop("cls", None)

        request = build_update_resource_group_level_task_state_request(
            resource_group_name=resource_group_name,
            asc_location=asc_location,
            task_name=task_name,
            task_update_action_type=task_update_action_type,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            template_url=self.update_resource_group_level_task_state.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        _stream = False
        pipeline_response: PipelineResponse = self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    update_resource_group_level_task_state.metadata = {
        "url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Security/locations/{ascLocation}/tasks/{taskName}/{taskUpdateActionType}"
    }
