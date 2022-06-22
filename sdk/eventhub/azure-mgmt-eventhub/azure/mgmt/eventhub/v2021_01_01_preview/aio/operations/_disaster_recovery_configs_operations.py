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
from ...operations._disaster_recovery_configs_operations import build_break_pairing_request, build_check_name_availability_request, build_create_or_update_request, build_delete_request, build_fail_over_request, build_get_authorization_rule_request, build_get_request, build_list_authorization_rules_request, build_list_keys_request, build_list_request
T = TypeVar('T')
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]

class DisasterRecoveryConfigsOperations:
    """DisasterRecoveryConfigsOperations async operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~azure.mgmt.eventhub.v2021_01_01_preview.models
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
    async def check_name_availability(
        self,
        resource_group_name: str,
        namespace_name: str,
        parameters: "_models.CheckNameAvailabilityParameter",
        **kwargs: Any
    ) -> "_models.CheckNameAvailabilityResult":
        """Check the give Namespace name availability.

        :param resource_group_name: Name of the resource group within the azure subscription.
        :type resource_group_name: str
        :param namespace_name: The Namespace name.
        :type namespace_name: str
        :param parameters: Parameters to check availability of the given Alias name.
        :type parameters:
         ~azure.mgmt.eventhub.v2021_01_01_preview.models.CheckNameAvailabilityParameter
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: CheckNameAvailabilityResult, or the result of cls(response)
        :rtype: ~azure.mgmt.eventhub.v2021_01_01_preview.models.CheckNameAvailabilityResult
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.CheckNameAvailabilityResult"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        api_version = kwargs.pop('api_version', "2021-01-01-preview")  # type: str
        content_type = kwargs.pop('content_type', "application/json")  # type: Optional[str]

        _json = self._serialize.body(parameters, 'CheckNameAvailabilityParameter')

        request = build_check_name_availability_request(
            subscription_id=self._config.subscription_id,
            resource_group_name=resource_group_name,
            namespace_name=namespace_name,
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
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('CheckNameAvailabilityResult', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    check_name_availability.metadata = {'url': "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.EventHub/namespaces/{namespaceName}/disasterRecoveryConfigs/checkNameAvailability"}  # type: ignore


    @distributed_trace
    def list(
        self,
        resource_group_name: str,
        namespace_name: str,
        **kwargs: Any
    ) -> AsyncIterable["_models.ArmDisasterRecoveryListResult"]:
        """Gets all Alias(Disaster Recovery configurations).

        :param resource_group_name: Name of the resource group within the azure subscription.
        :type resource_group_name: str
        :param namespace_name: The Namespace name.
        :type namespace_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either ArmDisasterRecoveryListResult or the result of
         cls(response)
        :rtype:
         ~azure.core.async_paging.AsyncItemPaged[~azure.mgmt.eventhub.v2021_01_01_preview.models.ArmDisasterRecoveryListResult]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        api_version = kwargs.pop('api_version', "2021-01-01-preview")  # type: str

        cls = kwargs.pop('cls', None)  # type: ClsType["_models.ArmDisasterRecoveryListResult"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        def prepare_request(next_link=None):
            if not next_link:
                
                request = build_list_request(
                    resource_group_name=resource_group_name,
                    namespace_name=namespace_name,
                    subscription_id=self._config.subscription_id,
                    api_version=api_version,
                    template_url=self.list.metadata['url'],
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)

            else:
                
                request = build_list_request(
                    resource_group_name=resource_group_name,
                    namespace_name=namespace_name,
                    subscription_id=self._config.subscription_id,
                    api_version=api_version,
                    template_url=next_link,
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)
                request.method = "GET"
            return request

        async def extract_data(pipeline_response):
            deserialized = self._deserialize("ArmDisasterRecoveryListResult", pipeline_response)
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
                error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
                raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

            return pipeline_response


        return AsyncItemPaged(
            get_next, extract_data
        )
    list.metadata = {'url': "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.EventHub/namespaces/{namespaceName}/disasterRecoveryConfigs"}  # type: ignore

    @distributed_trace_async
    async def create_or_update(
        self,
        resource_group_name: str,
        namespace_name: str,
        alias: str,
        parameters: "_models.ArmDisasterRecovery",
        **kwargs: Any
    ) -> Optional["_models.ArmDisasterRecovery"]:
        """Creates or updates a new Alias(Disaster Recovery configuration).

        :param resource_group_name: Name of the resource group within the azure subscription.
        :type resource_group_name: str
        :param namespace_name: The Namespace name.
        :type namespace_name: str
        :param alias: The Disaster Recovery configuration name.
        :type alias: str
        :param parameters: Parameters required to create an Alias(Disaster Recovery configuration).
        :type parameters: ~azure.mgmt.eventhub.v2021_01_01_preview.models.ArmDisasterRecovery
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ArmDisasterRecovery, or the result of cls(response)
        :rtype: ~azure.mgmt.eventhub.v2021_01_01_preview.models.ArmDisasterRecovery or None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[Optional["_models.ArmDisasterRecovery"]]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        api_version = kwargs.pop('api_version', "2021-01-01-preview")  # type: str
        content_type = kwargs.pop('content_type', "application/json")  # type: Optional[str]

        _json = self._serialize.body(parameters, 'ArmDisasterRecovery')

        request = build_create_or_update_request(
            resource_group_name=resource_group_name,
            namespace_name=namespace_name,
            alias=alias,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            content_type=content_type,
            json=_json,
            template_url=self.create_or_update.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(  # pylint: disable=protected-access
            request,
            stream=False,
            **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200, 201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('ArmDisasterRecovery', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    create_or_update.metadata = {'url': "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.EventHub/namespaces/{namespaceName}/disasterRecoveryConfigs/{alias}"}  # type: ignore


    @distributed_trace_async
    async def delete(  # pylint: disable=inconsistent-return-statements
        self,
        resource_group_name: str,
        namespace_name: str,
        alias: str,
        **kwargs: Any
    ) -> None:
        """Deletes an Alias(Disaster Recovery configuration).

        :param resource_group_name: Name of the resource group within the azure subscription.
        :type resource_group_name: str
        :param namespace_name: The Namespace name.
        :type namespace_name: str
        :param alias: The Disaster Recovery configuration name.
        :type alias: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        api_version = kwargs.pop('api_version', "2021-01-01-preview")  # type: str

        
        request = build_delete_request(
            resource_group_name=resource_group_name,
            namespace_name=namespace_name,
            alias=alias,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            template_url=self.delete.metadata['url'],
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
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    delete.metadata = {'url': "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.EventHub/namespaces/{namespaceName}/disasterRecoveryConfigs/{alias}"}  # type: ignore


    @distributed_trace_async
    async def get(
        self,
        resource_group_name: str,
        namespace_name: str,
        alias: str,
        **kwargs: Any
    ) -> "_models.ArmDisasterRecovery":
        """Retrieves Alias(Disaster Recovery configuration) for primary or secondary namespace.

        :param resource_group_name: Name of the resource group within the azure subscription.
        :type resource_group_name: str
        :param namespace_name: The Namespace name.
        :type namespace_name: str
        :param alias: The Disaster Recovery configuration name.
        :type alias: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ArmDisasterRecovery, or the result of cls(response)
        :rtype: ~azure.mgmt.eventhub.v2021_01_01_preview.models.ArmDisasterRecovery
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.ArmDisasterRecovery"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        api_version = kwargs.pop('api_version', "2021-01-01-preview")  # type: str

        
        request = build_get_request(
            resource_group_name=resource_group_name,
            namespace_name=namespace_name,
            alias=alias,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            template_url=self.get.metadata['url'],
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
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('ArmDisasterRecovery', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get.metadata = {'url': "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.EventHub/namespaces/{namespaceName}/disasterRecoveryConfigs/{alias}"}  # type: ignore


    @distributed_trace_async
    async def break_pairing(  # pylint: disable=inconsistent-return-statements
        self,
        resource_group_name: str,
        namespace_name: str,
        alias: str,
        **kwargs: Any
    ) -> None:
        """This operation disables the Disaster Recovery and stops replicating changes from primary to
        secondary namespaces.

        :param resource_group_name: Name of the resource group within the azure subscription.
        :type resource_group_name: str
        :param namespace_name: The Namespace name.
        :type namespace_name: str
        :param alias: The Disaster Recovery configuration name.
        :type alias: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        api_version = kwargs.pop('api_version', "2021-01-01-preview")  # type: str

        
        request = build_break_pairing_request(
            resource_group_name=resource_group_name,
            namespace_name=namespace_name,
            alias=alias,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            template_url=self.break_pairing.metadata['url'],
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
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    break_pairing.metadata = {'url': "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.EventHub/namespaces/{namespaceName}/disasterRecoveryConfigs/{alias}/breakPairing"}  # type: ignore


    @distributed_trace_async
    async def fail_over(  # pylint: disable=inconsistent-return-statements
        self,
        resource_group_name: str,
        namespace_name: str,
        alias: str,
        **kwargs: Any
    ) -> None:
        """Invokes GEO DR failover and reconfigure the alias to point to the secondary namespace.

        :param resource_group_name: Name of the resource group within the azure subscription.
        :type resource_group_name: str
        :param namespace_name: The Namespace name.
        :type namespace_name: str
        :param alias: The Disaster Recovery configuration name.
        :type alias: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        api_version = kwargs.pop('api_version', "2021-01-01-preview")  # type: str

        
        request = build_fail_over_request(
            resource_group_name=resource_group_name,
            namespace_name=namespace_name,
            alias=alias,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            template_url=self.fail_over.metadata['url'],
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
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    fail_over.metadata = {'url': "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.EventHub/namespaces/{namespaceName}/disasterRecoveryConfigs/{alias}/failover"}  # type: ignore


    @distributed_trace
    def list_authorization_rules(
        self,
        resource_group_name: str,
        namespace_name: str,
        alias: str,
        **kwargs: Any
    ) -> AsyncIterable["_models.AuthorizationRuleListResult"]:
        """Gets a list of authorization rules for a Namespace.

        :param resource_group_name: Name of the resource group within the azure subscription.
        :type resource_group_name: str
        :param namespace_name: The Namespace name.
        :type namespace_name: str
        :param alias: The Disaster Recovery configuration name.
        :type alias: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either AuthorizationRuleListResult or the result of
         cls(response)
        :rtype:
         ~azure.core.async_paging.AsyncItemPaged[~azure.mgmt.eventhub.v2021_01_01_preview.models.AuthorizationRuleListResult]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        api_version = kwargs.pop('api_version', "2021-01-01-preview")  # type: str

        cls = kwargs.pop('cls', None)  # type: ClsType["_models.AuthorizationRuleListResult"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        def prepare_request(next_link=None):
            if not next_link:
                
                request = build_list_authorization_rules_request(
                    resource_group_name=resource_group_name,
                    namespace_name=namespace_name,
                    alias=alias,
                    subscription_id=self._config.subscription_id,
                    api_version=api_version,
                    template_url=self.list_authorization_rules.metadata['url'],
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)

            else:
                
                request = build_list_authorization_rules_request(
                    resource_group_name=resource_group_name,
                    namespace_name=namespace_name,
                    alias=alias,
                    subscription_id=self._config.subscription_id,
                    api_version=api_version,
                    template_url=next_link,
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)
                request.method = "GET"
            return request

        async def extract_data(pipeline_response):
            deserialized = self._deserialize("AuthorizationRuleListResult", pipeline_response)
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
                error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
                raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

            return pipeline_response


        return AsyncItemPaged(
            get_next, extract_data
        )
    list_authorization_rules.metadata = {'url': "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.EventHub/namespaces/{namespaceName}/disasterRecoveryConfigs/{alias}/authorizationRules"}  # type: ignore

    @distributed_trace_async
    async def get_authorization_rule(
        self,
        resource_group_name: str,
        namespace_name: str,
        alias: str,
        authorization_rule_name: str,
        **kwargs: Any
    ) -> "_models.AuthorizationRule":
        """Gets an AuthorizationRule for a Namespace by rule name.

        :param resource_group_name: Name of the resource group within the azure subscription.
        :type resource_group_name: str
        :param namespace_name: The Namespace name.
        :type namespace_name: str
        :param alias: The Disaster Recovery configuration name.
        :type alias: str
        :param authorization_rule_name: The authorization rule name.
        :type authorization_rule_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: AuthorizationRule, or the result of cls(response)
        :rtype: ~azure.mgmt.eventhub.v2021_01_01_preview.models.AuthorizationRule
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.AuthorizationRule"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        api_version = kwargs.pop('api_version', "2021-01-01-preview")  # type: str

        
        request = build_get_authorization_rule_request(
            resource_group_name=resource_group_name,
            namespace_name=namespace_name,
            alias=alias,
            authorization_rule_name=authorization_rule_name,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            template_url=self.get_authorization_rule.metadata['url'],
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
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('AuthorizationRule', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_authorization_rule.metadata = {'url': "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.EventHub/namespaces/{namespaceName}/disasterRecoveryConfigs/{alias}/authorizationRules/{authorizationRuleName}"}  # type: ignore


    @distributed_trace_async
    async def list_keys(
        self,
        resource_group_name: str,
        namespace_name: str,
        alias: str,
        authorization_rule_name: str,
        **kwargs: Any
    ) -> "_models.AccessKeys":
        """Gets the primary and secondary connection strings for the Namespace.

        :param resource_group_name: Name of the resource group within the azure subscription.
        :type resource_group_name: str
        :param namespace_name: The Namespace name.
        :type namespace_name: str
        :param alias: The Disaster Recovery configuration name.
        :type alias: str
        :param authorization_rule_name: The authorization rule name.
        :type authorization_rule_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: AccessKeys, or the result of cls(response)
        :rtype: ~azure.mgmt.eventhub.v2021_01_01_preview.models.AccessKeys
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.AccessKeys"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        api_version = kwargs.pop('api_version', "2021-01-01-preview")  # type: str

        
        request = build_list_keys_request(
            resource_group_name=resource_group_name,
            namespace_name=namespace_name,
            alias=alias,
            authorization_rule_name=authorization_rule_name,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            template_url=self.list_keys.metadata['url'],
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
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('AccessKeys', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    list_keys.metadata = {'url': "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.EventHub/namespaces/{namespaceName}/disasterRecoveryConfigs/{alias}/authorizationRules/{authorizationRuleName}/listKeys"}  # type: ignore

