# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import sys
from typing import Any, AsyncIterable, Callable, Dict, IO, Optional, TypeVar, Union, cast, overload
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
from azure.core.polling import AsyncLROPoller, AsyncNoPolling, AsyncPollingMethod
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator import distributed_trace
from azure.core.tracing.decorator_async import distributed_trace_async
from azure.core.utils import case_insensitive_dict
from azure.mgmt.core.exceptions import ARMErrorFormat
from azure.mgmt.core.polling.async_arm_polling import AsyncARMPolling

from ... import models as _models
from ..._vendor import _convert_request
from ...operations._virtual_machines_operations import (
    build_get_request,
    build_list_request,
    build_restrict_movement_request,
)

if sys.version_info >= (3, 8):
    from typing import Literal  # pylint: disable=no-name-in-module, ungrouped-imports
else:
    from typing_extensions import Literal  # type: ignore  # pylint: disable=ungrouped-imports
T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]


class VirtualMachinesOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~azure.mgmt.avs.aio.AVSClient`'s
        :attr:`virtual_machines` attribute.
    """

    models = _models

    def __init__(self, *args, **kwargs) -> None:
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    @distributed_trace
    def list(
        self, resource_group_name: str, private_cloud_name: str, cluster_name: str, **kwargs: Any
    ) -> AsyncIterable["_models.VirtualMachine"]:
        """List of virtual machines in a private cloud cluster.

        List of virtual machines in a private cloud cluster.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param private_cloud_name: Name of the private cloud. Required.
        :type private_cloud_name: str
        :param cluster_name: Name of the cluster in the private cloud. Required.
        :type cluster_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either VirtualMachine or the result of cls(response)
        :rtype: ~azure.core.async_paging.AsyncItemPaged[~azure.mgmt.avs.models.VirtualMachine]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: Literal["2022-05-01"] = kwargs.pop(
            "api_version", _params.pop("api-version", self._config.api_version)
        )
        cls: ClsType[_models.VirtualMachinesList] = kwargs.pop("cls", None)

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
                    resource_group_name=resource_group_name,
                    private_cloud_name=private_cloud_name,
                    cluster_name=cluster_name,
                    subscription_id=self._config.subscription_id,
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
            deserialized = self._deserialize("VirtualMachinesList", pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)  # type: ignore
            return deserialized.next_link or None, AsyncList(list_of_elem)

        async def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
                request, stream=False, **kwargs
            )
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response, error_format=ARMErrorFormat)

            return pipeline_response

        return AsyncItemPaged(get_next, extract_data)

    list.metadata = {
        "url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AVS/privateClouds/{privateCloudName}/clusters/{clusterName}/virtualMachines"
    }

    @distributed_trace_async
    async def get(
        self,
        resource_group_name: str,
        private_cloud_name: str,
        cluster_name: str,
        virtual_machine_id: str,
        **kwargs: Any
    ) -> _models.VirtualMachine:
        """Get a virtual machine by id in a private cloud cluster.

        Get a virtual machine by id in a private cloud cluster.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param private_cloud_name: Name of the private cloud. Required.
        :type private_cloud_name: str
        :param cluster_name: Name of the cluster in the private cloud. Required.
        :type cluster_name: str
        :param virtual_machine_id: Virtual Machine identifier. Required.
        :type virtual_machine_id: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: VirtualMachine or the result of cls(response)
        :rtype: ~azure.mgmt.avs.models.VirtualMachine
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

        api_version: Literal["2022-05-01"] = kwargs.pop(
            "api_version", _params.pop("api-version", self._config.api_version)
        )
        cls: ClsType[_models.VirtualMachine] = kwargs.pop("cls", None)

        request = build_get_request(
            resource_group_name=resource_group_name,
            private_cloud_name=private_cloud_name,
            cluster_name=cluster_name,
            virtual_machine_id=virtual_machine_id,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            template_url=self.get.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize("VirtualMachine", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get.metadata = {
        "url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AVS/privateClouds/{privateCloudName}/clusters/{clusterName}/virtualMachines/{virtualMachineId}"
    }

    async def _restrict_movement_initial(  # pylint: disable=inconsistent-return-statements
        self,
        resource_group_name: str,
        private_cloud_name: str,
        cluster_name: str,
        virtual_machine_id: str,
        restrict_movement: Union[_models.VirtualMachineRestrictMovement, IO],
        **kwargs: Any
    ) -> None:
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: Literal["2022-05-01"] = kwargs.pop(
            "api_version", _params.pop("api-version", self._config.api_version)
        )
        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[None] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(restrict_movement, (IO, bytes)):
            _content = restrict_movement
        else:
            _json = self._serialize.body(restrict_movement, "VirtualMachineRestrictMovement")

        request = build_restrict_movement_request(
            resource_group_name=resource_group_name,
            private_cloud_name=private_cloud_name,
            cluster_name=cluster_name,
            virtual_machine_id=virtual_machine_id,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            content_type=content_type,
            json=_json,
            content=_content,
            template_url=self._restrict_movement_initial.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [202]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    _restrict_movement_initial.metadata = {
        "url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AVS/privateClouds/{privateCloudName}/clusters/{clusterName}/virtualMachines/{virtualMachineId}/restrictMovement"
    }

    @overload
    async def begin_restrict_movement(
        self,
        resource_group_name: str,
        private_cloud_name: str,
        cluster_name: str,
        virtual_machine_id: str,
        restrict_movement: _models.VirtualMachineRestrictMovement,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> AsyncLROPoller[None]:
        """Enable or disable DRS-driven VM movement restriction.

        Enable or disable DRS-driven VM movement restriction.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param private_cloud_name: Name of the private cloud. Required.
        :type private_cloud_name: str
        :param cluster_name: Name of the cluster in the private cloud. Required.
        :type cluster_name: str
        :param virtual_machine_id: Virtual Machine identifier. Required.
        :type virtual_machine_id: str
        :param restrict_movement: Whether VM DRS-driven movement is restricted (Enabled) or not
         (Disabled). Required.
        :type restrict_movement: ~azure.mgmt.avs.models.VirtualMachineRestrictMovement
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :keyword str continuation_token: A continuation token to restart a poller from a saved state.
        :keyword polling: By default, your polling method will be AsyncARMPolling. Pass in False for
         this operation to not poll, or pass in your own initialized polling object for a personal
         polling strategy.
        :paramtype polling: bool or ~azure.core.polling.AsyncPollingMethod
        :keyword int polling_interval: Default waiting time between two polls for LRO operations if no
         Retry-After header is present.
        :return: An instance of AsyncLROPoller that returns either None or the result of cls(response)
        :rtype: ~azure.core.polling.AsyncLROPoller[None]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def begin_restrict_movement(
        self,
        resource_group_name: str,
        private_cloud_name: str,
        cluster_name: str,
        virtual_machine_id: str,
        restrict_movement: IO,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> AsyncLROPoller[None]:
        """Enable or disable DRS-driven VM movement restriction.

        Enable or disable DRS-driven VM movement restriction.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param private_cloud_name: Name of the private cloud. Required.
        :type private_cloud_name: str
        :param cluster_name: Name of the cluster in the private cloud. Required.
        :type cluster_name: str
        :param virtual_machine_id: Virtual Machine identifier. Required.
        :type virtual_machine_id: str
        :param restrict_movement: Whether VM DRS-driven movement is restricted (Enabled) or not
         (Disabled). Required.
        :type restrict_movement: IO
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :keyword str continuation_token: A continuation token to restart a poller from a saved state.
        :keyword polling: By default, your polling method will be AsyncARMPolling. Pass in False for
         this operation to not poll, or pass in your own initialized polling object for a personal
         polling strategy.
        :paramtype polling: bool or ~azure.core.polling.AsyncPollingMethod
        :keyword int polling_interval: Default waiting time between two polls for LRO operations if no
         Retry-After header is present.
        :return: An instance of AsyncLROPoller that returns either None or the result of cls(response)
        :rtype: ~azure.core.polling.AsyncLROPoller[None]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace_async
    async def begin_restrict_movement(
        self,
        resource_group_name: str,
        private_cloud_name: str,
        cluster_name: str,
        virtual_machine_id: str,
        restrict_movement: Union[_models.VirtualMachineRestrictMovement, IO],
        **kwargs: Any
    ) -> AsyncLROPoller[None]:
        """Enable or disable DRS-driven VM movement restriction.

        Enable or disable DRS-driven VM movement restriction.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param private_cloud_name: Name of the private cloud. Required.
        :type private_cloud_name: str
        :param cluster_name: Name of the cluster in the private cloud. Required.
        :type cluster_name: str
        :param virtual_machine_id: Virtual Machine identifier. Required.
        :type virtual_machine_id: str
        :param restrict_movement: Whether VM DRS-driven movement is restricted (Enabled) or not
         (Disabled). Is either a model type or a IO type. Required.
        :type restrict_movement: ~azure.mgmt.avs.models.VirtualMachineRestrictMovement or IO
        :keyword content_type: Body Parameter content-type. Known values are: 'application/json'.
         Default value is None.
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :keyword str continuation_token: A continuation token to restart a poller from a saved state.
        :keyword polling: By default, your polling method will be AsyncARMPolling. Pass in False for
         this operation to not poll, or pass in your own initialized polling object for a personal
         polling strategy.
        :paramtype polling: bool or ~azure.core.polling.AsyncPollingMethod
        :keyword int polling_interval: Default waiting time between two polls for LRO operations if no
         Retry-After header is present.
        :return: An instance of AsyncLROPoller that returns either None or the result of cls(response)
        :rtype: ~azure.core.polling.AsyncLROPoller[None]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: Literal["2022-05-01"] = kwargs.pop(
            "api_version", _params.pop("api-version", self._config.api_version)
        )
        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[None] = kwargs.pop("cls", None)
        polling: Union[bool, AsyncPollingMethod] = kwargs.pop("polling", True)
        lro_delay = kwargs.pop("polling_interval", self._config.polling_interval)
        cont_token: Optional[str] = kwargs.pop("continuation_token", None)
        if cont_token is None:
            raw_result = await self._restrict_movement_initial(  # type: ignore
                resource_group_name=resource_group_name,
                private_cloud_name=private_cloud_name,
                cluster_name=cluster_name,
                virtual_machine_id=virtual_machine_id,
                restrict_movement=restrict_movement,
                api_version=api_version,
                content_type=content_type,
                cls=lambda x, y, z: x,
                headers=_headers,
                params=_params,
                **kwargs
            )
        kwargs.pop("error_map", None)

        def get_long_running_output(pipeline_response):  # pylint: disable=inconsistent-return-statements
            if cls:
                return cls(pipeline_response, None, {})

        if polling is True:
            polling_method: AsyncPollingMethod = cast(AsyncPollingMethod, AsyncARMPolling(lro_delay, **kwargs))
        elif polling is False:
            polling_method = cast(AsyncPollingMethod, AsyncNoPolling())
        else:
            polling_method = polling
        if cont_token:
            return AsyncLROPoller.from_continuation_token(
                polling_method=polling_method,
                continuation_token=cont_token,
                client=self._client,
                deserialization_callback=get_long_running_output,
            )
        return AsyncLROPoller(self._client, raw_result, get_long_running_output, polling_method)  # type: ignore

    begin_restrict_movement.metadata = {
        "url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AVS/privateClouds/{privateCloudName}/clusters/{clusterName}/virtualMachines/{virtualMachineId}/restrictMovement"
    }
