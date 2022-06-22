# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, AsyncIterable, Callable, Dict, Optional, TypeVar

from azure.core.async_paging import AsyncItemPaged, AsyncList
from azure.core.exceptions import ClientAuthenticationError, HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator import distributed_trace
from azure.core.tracing.decorator_async import distributed_trace_async
from azure.mgmt.core.exceptions import ARMErrorFormat

from ... import models as _models
from ..._vendor import _convert_request
from ...operations._location_operations import build_check_name_availability_request, build_get_quotas_request, build_list_supported_cloud_service_skus_request, build_list_supported_virtual_machine_skus_request
T = TypeVar('T')
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]

class LocationOperations:
    """LocationOperations async operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~azure.mgmt.batch.models
    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = _models

    def __init__(self, client, config, serializer, deserializer) -> None:
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    @distributed_trace_async
    async def get_quotas(
        self,
        location_name: str,
        **kwargs: Any
    ) -> "_models.BatchLocationQuota":
        """Gets the Batch service quotas for the specified subscription at the given location.

        :param location_name: The region for which to retrieve Batch service quotas.
        :type location_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: BatchLocationQuota, or the result of cls(response)
        :rtype: ~azure.mgmt.batch.models.BatchLocationQuota
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.BatchLocationQuota"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        api_version = kwargs.pop('api_version', "2022-06-01")  # type: str

        
        request = build_get_quotas_request(
            location_name=location_name,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            template_url=self.get_quotas.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(  # pylint: disable=protected-access
            request,
            stream=False,
            **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize('BatchLocationQuota', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_quotas.metadata = {'url': "/subscriptions/{subscriptionId}/providers/Microsoft.Batch/locations/{locationName}/quotas"}  # type: ignore


    @distributed_trace
    def list_supported_virtual_machine_skus(
        self,
        location_name: str,
        maxresults: Optional[int] = None,
        filter: Optional[str] = None,
        **kwargs: Any
    ) -> AsyncIterable["_models.SupportedSkusResult"]:
        """Gets the list of Batch supported Virtual Machine VM sizes available at the given location.

        :param location_name: The region for which to retrieve Batch service supported SKUs.
        :type location_name: str
        :param maxresults: The maximum number of items to return in the response. Default value is
         None.
        :type maxresults: int
        :param filter: OData filter expression. Valid properties for filtering are "familyName".
         Default value is None.
        :type filter: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either SupportedSkusResult or the result of cls(response)
        :rtype: ~azure.core.async_paging.AsyncItemPaged[~azure.mgmt.batch.models.SupportedSkusResult]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        api_version = kwargs.pop('api_version', "2022-06-01")  # type: str

        cls = kwargs.pop('cls', None)  # type: ClsType["_models.SupportedSkusResult"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        def prepare_request(next_link=None):
            if not next_link:
                
                request = build_list_supported_virtual_machine_skus_request(
                    location_name=location_name,
                    subscription_id=self._config.subscription_id,
                    api_version=api_version,
                    maxresults=maxresults,
                    filter=filter,
                    template_url=self.list_supported_virtual_machine_skus.metadata['url'],
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)

            else:
                
                request = build_list_supported_virtual_machine_skus_request(
                    location_name=location_name,
                    subscription_id=self._config.subscription_id,
                    api_version=api_version,
                    maxresults=maxresults,
                    filter=filter,
                    template_url=next_link,
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)
                request.method = "GET"
            return request

        async def extract_data(pipeline_response):
            deserialized = self._deserialize("SupportedSkusResult", pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.next_link or None, AsyncList(list_of_elem)

        async def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = await self._client._pipeline.run(  # pylint: disable=protected-access
                request,
                stream=False,
                **kwargs
            )
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response, error_format=ARMErrorFormat)

            return pipeline_response


        return AsyncItemPaged(
            get_next, extract_data
        )
    list_supported_virtual_machine_skus.metadata = {'url': "/subscriptions/{subscriptionId}/providers/Microsoft.Batch/locations/{locationName}/virtualMachineSkus"}  # type: ignore

    @distributed_trace
    def list_supported_cloud_service_skus(
        self,
        location_name: str,
        maxresults: Optional[int] = None,
        filter: Optional[str] = None,
        **kwargs: Any
    ) -> AsyncIterable["_models.SupportedSkusResult"]:
        """Gets the list of Batch supported Cloud Service VM sizes available at the given location.

        :param location_name: The region for which to retrieve Batch service supported SKUs.
        :type location_name: str
        :param maxresults: The maximum number of items to return in the response. Default value is
         None.
        :type maxresults: int
        :param filter: OData filter expression. Valid properties for filtering are "familyName".
         Default value is None.
        :type filter: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either SupportedSkusResult or the result of cls(response)
        :rtype: ~azure.core.async_paging.AsyncItemPaged[~azure.mgmt.batch.models.SupportedSkusResult]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        api_version = kwargs.pop('api_version', "2022-06-01")  # type: str

        cls = kwargs.pop('cls', None)  # type: ClsType["_models.SupportedSkusResult"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        def prepare_request(next_link=None):
            if not next_link:
                
                request = build_list_supported_cloud_service_skus_request(
                    location_name=location_name,
                    subscription_id=self._config.subscription_id,
                    api_version=api_version,
                    maxresults=maxresults,
                    filter=filter,
                    template_url=self.list_supported_cloud_service_skus.metadata['url'],
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)

            else:
                
                request = build_list_supported_cloud_service_skus_request(
                    location_name=location_name,
                    subscription_id=self._config.subscription_id,
                    api_version=api_version,
                    maxresults=maxresults,
                    filter=filter,
                    template_url=next_link,
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)
                request.method = "GET"
            return request

        async def extract_data(pipeline_response):
            deserialized = self._deserialize("SupportedSkusResult", pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.next_link or None, AsyncList(list_of_elem)

        async def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = await self._client._pipeline.run(  # pylint: disable=protected-access
                request,
                stream=False,
                **kwargs
            )
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response, error_format=ARMErrorFormat)

            return pipeline_response


        return AsyncItemPaged(
            get_next, extract_data
        )
    list_supported_cloud_service_skus.metadata = {'url': "/subscriptions/{subscriptionId}/providers/Microsoft.Batch/locations/{locationName}/cloudServiceSkus"}  # type: ignore

    @distributed_trace_async
    async def check_name_availability(
        self,
        location_name: str,
        parameters: "_models.CheckNameAvailabilityParameters",
        **kwargs: Any
    ) -> "_models.CheckNameAvailabilityResult":
        """Checks whether the Batch account name is available in the specified region.

        :param location_name: The desired region for the name check.
        :type location_name: str
        :param parameters: Properties needed to check the availability of a name.
        :type parameters: ~azure.mgmt.batch.models.CheckNameAvailabilityParameters
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: CheckNameAvailabilityResult, or the result of cls(response)
        :rtype: ~azure.mgmt.batch.models.CheckNameAvailabilityResult
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.CheckNameAvailabilityResult"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        api_version = kwargs.pop('api_version', "2022-06-01")  # type: str
        content_type = kwargs.pop('content_type', "application/json")  # type: Optional[str]

        _json = self._serialize.body(parameters, 'CheckNameAvailabilityParameters')

        request = build_check_name_availability_request(
            location_name=location_name,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            content_type=content_type,
            json=_json,
            template_url=self.check_name_availability.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(  # pylint: disable=protected-access
            request,
            stream=False,
            **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize('CheckNameAvailabilityResult', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    check_name_availability.metadata = {'url': "/subscriptions/{subscriptionId}/providers/Microsoft.Batch/locations/{locationName}/checkNameAvailability"}  # type: ignore

