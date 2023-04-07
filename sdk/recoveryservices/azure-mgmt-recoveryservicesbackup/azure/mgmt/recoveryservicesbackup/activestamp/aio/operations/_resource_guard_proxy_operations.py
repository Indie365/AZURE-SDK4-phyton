# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import sys
from typing import Any, Callable, Dict, IO, Optional, TypeVar, Union, overload

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
from azure.core.tracing.decorator_async import distributed_trace_async
from azure.core.utils import case_insensitive_dict
from azure.mgmt.core.exceptions import ARMErrorFormat

from ... import models as _models
from ..._vendor import _convert_request
from ...operations._resource_guard_proxy_operations import (
    build_delete_request,
    build_get_request,
    build_put_request,
    build_unlock_delete_request,
)
from .._vendor import RecoveryServicesBackupClientMixinABC

if sys.version_info >= (3, 8):
    from typing import Literal  # pylint: disable=no-name-in-module, ungrouped-imports
else:
    from typing_extensions import Literal  # type: ignore  # pylint: disable=ungrouped-imports
T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]


class ResourceGuardProxyOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~azure.mgmt.recoveryservicesbackup.activestamp.aio.RecoveryServicesBackupClient`'s
        :attr:`resource_guard_proxy` attribute.
    """

    models = _models

    def __init__(self, *args, **kwargs) -> None:
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    @distributed_trace_async
    async def get(
        self, vault_name: str, resource_group_name: str, resource_guard_proxy_name: str, **kwargs: Any
    ) -> _models.ResourceGuardProxyBaseResource:
        """Returns ResourceGuardProxy under vault and with the name referenced in request.

        :param vault_name: The name of the recovery services vault. Required.
        :type vault_name: str
        :param resource_group_name: The name of the resource group where the recovery services vault is
         present. Required.
        :type resource_group_name: str
        :param resource_guard_proxy_name: Required.
        :type resource_guard_proxy_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ResourceGuardProxyBaseResource or the result of cls(response)
        :rtype: ~azure.mgmt.recoveryservicesbackup.activestamp.models.ResourceGuardProxyBaseResource
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

        api_version: Literal["2023-02-01"] = kwargs.pop(
            "api_version", _params.pop("api-version", self._config.api_version)
        )
        cls: ClsType[_models.ResourceGuardProxyBaseResource] = kwargs.pop("cls", None)

        request = build_get_request(
            vault_name=vault_name,
            resource_group_name=resource_group_name,
            resource_guard_proxy_name=resource_guard_proxy_name,
            subscription_id=self._config.subscription_id,
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

        deserialized = self._deserialize("ResourceGuardProxyBaseResource", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get.metadata = {
        "url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{vaultName}/backupResourceGuardProxies/{resourceGuardProxyName}"
    }

    @overload
    async def put(
        self,
        vault_name: str,
        resource_group_name: str,
        resource_guard_proxy_name: str,
        parameters: _models.ResourceGuardProxyBaseResource,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.ResourceGuardProxyBaseResource:
        """Add or Update ResourceGuardProxy under vault
        Secures vault critical operations.

        :param vault_name: The name of the recovery services vault. Required.
        :type vault_name: str
        :param resource_group_name: The name of the resource group where the recovery services vault is
         present. Required.
        :type resource_group_name: str
        :param resource_guard_proxy_name: Required.
        :type resource_guard_proxy_name: str
        :param parameters: Request body for operation. Required.
        :type parameters:
         ~azure.mgmt.recoveryservicesbackup.activestamp.models.ResourceGuardProxyBaseResource
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ResourceGuardProxyBaseResource or the result of cls(response)
        :rtype: ~azure.mgmt.recoveryservicesbackup.activestamp.models.ResourceGuardProxyBaseResource
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def put(
        self,
        vault_name: str,
        resource_group_name: str,
        resource_guard_proxy_name: str,
        parameters: IO,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.ResourceGuardProxyBaseResource:
        """Add or Update ResourceGuardProxy under vault
        Secures vault critical operations.

        :param vault_name: The name of the recovery services vault. Required.
        :type vault_name: str
        :param resource_group_name: The name of the resource group where the recovery services vault is
         present. Required.
        :type resource_group_name: str
        :param resource_guard_proxy_name: Required.
        :type resource_guard_proxy_name: str
        :param parameters: Request body for operation. Required.
        :type parameters: IO
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ResourceGuardProxyBaseResource or the result of cls(response)
        :rtype: ~azure.mgmt.recoveryservicesbackup.activestamp.models.ResourceGuardProxyBaseResource
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace_async
    async def put(
        self,
        vault_name: str,
        resource_group_name: str,
        resource_guard_proxy_name: str,
        parameters: Union[_models.ResourceGuardProxyBaseResource, IO],
        **kwargs: Any
    ) -> _models.ResourceGuardProxyBaseResource:
        """Add or Update ResourceGuardProxy under vault
        Secures vault critical operations.

        :param vault_name: The name of the recovery services vault. Required.
        :type vault_name: str
        :param resource_group_name: The name of the resource group where the recovery services vault is
         present. Required.
        :type resource_group_name: str
        :param resource_guard_proxy_name: Required.
        :type resource_guard_proxy_name: str
        :param parameters: Request body for operation. Is either a ResourceGuardProxyBaseResource type
         or a IO type. Required.
        :type parameters:
         ~azure.mgmt.recoveryservicesbackup.activestamp.models.ResourceGuardProxyBaseResource or IO
        :keyword content_type: Body Parameter content-type. Known values are: 'application/json'.
         Default value is None.
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ResourceGuardProxyBaseResource or the result of cls(response)
        :rtype: ~azure.mgmt.recoveryservicesbackup.activestamp.models.ResourceGuardProxyBaseResource
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

        api_version: Literal["2023-02-01"] = kwargs.pop(
            "api_version", _params.pop("api-version", self._config.api_version)
        )
        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[_models.ResourceGuardProxyBaseResource] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(parameters, (IO, bytes)):
            _content = parameters
        else:
            _json = self._serialize.body(parameters, "ResourceGuardProxyBaseResource")

        request = build_put_request(
            vault_name=vault_name,
            resource_group_name=resource_group_name,
            resource_guard_proxy_name=resource_guard_proxy_name,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            content_type=content_type,
            json=_json,
            content=_content,
            template_url=self.put.metadata["url"],
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

        deserialized = self._deserialize("ResourceGuardProxyBaseResource", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    put.metadata = {
        "url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{vaultName}/backupResourceGuardProxies/{resourceGuardProxyName}"
    }

    @distributed_trace_async
    async def delete(  # pylint: disable=inconsistent-return-statements
        self, vault_name: str, resource_group_name: str, resource_guard_proxy_name: str, **kwargs: Any
    ) -> None:
        """Delete ResourceGuardProxy under vault.

        :param vault_name: The name of the recovery services vault. Required.
        :type vault_name: str
        :param resource_group_name: The name of the resource group where the recovery services vault is
         present. Required.
        :type resource_group_name: str
        :param resource_guard_proxy_name: Required.
        :type resource_guard_proxy_name: str
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

        api_version: Literal["2023-02-01"] = kwargs.pop(
            "api_version", _params.pop("api-version", self._config.api_version)
        )
        cls: ClsType[None] = kwargs.pop("cls", None)

        request = build_delete_request(
            vault_name=vault_name,
            resource_group_name=resource_group_name,
            resource_guard_proxy_name=resource_guard_proxy_name,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            template_url=self.delete.metadata["url"],
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

        if response.status_code not in [200, 204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    delete.metadata = {
        "url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{vaultName}/backupResourceGuardProxies/{resourceGuardProxyName}"
    }

    @overload
    async def unlock_delete(
        self,
        vault_name: str,
        resource_group_name: str,
        resource_guard_proxy_name: str,
        parameters: _models.UnlockDeleteRequest,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.UnlockDeleteResponse:
        """Secures delete ResourceGuardProxy operations.

        :param vault_name: The name of the recovery services vault. Required.
        :type vault_name: str
        :param resource_group_name: The name of the resource group where the recovery services vault is
         present. Required.
        :type resource_group_name: str
        :param resource_guard_proxy_name: Required.
        :type resource_guard_proxy_name: str
        :param parameters: Request body for operation. Required.
        :type parameters: ~azure.mgmt.recoveryservicesbackup.activestamp.models.UnlockDeleteRequest
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: UnlockDeleteResponse or the result of cls(response)
        :rtype: ~azure.mgmt.recoveryservicesbackup.activestamp.models.UnlockDeleteResponse
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def unlock_delete(
        self,
        vault_name: str,
        resource_group_name: str,
        resource_guard_proxy_name: str,
        parameters: IO,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.UnlockDeleteResponse:
        """Secures delete ResourceGuardProxy operations.

        :param vault_name: The name of the recovery services vault. Required.
        :type vault_name: str
        :param resource_group_name: The name of the resource group where the recovery services vault is
         present. Required.
        :type resource_group_name: str
        :param resource_guard_proxy_name: Required.
        :type resource_guard_proxy_name: str
        :param parameters: Request body for operation. Required.
        :type parameters: IO
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: UnlockDeleteResponse or the result of cls(response)
        :rtype: ~azure.mgmt.recoveryservicesbackup.activestamp.models.UnlockDeleteResponse
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace_async
    async def unlock_delete(
        self,
        vault_name: str,
        resource_group_name: str,
        resource_guard_proxy_name: str,
        parameters: Union[_models.UnlockDeleteRequest, IO],
        **kwargs: Any
    ) -> _models.UnlockDeleteResponse:
        """Secures delete ResourceGuardProxy operations.

        :param vault_name: The name of the recovery services vault. Required.
        :type vault_name: str
        :param resource_group_name: The name of the resource group where the recovery services vault is
         present. Required.
        :type resource_group_name: str
        :param resource_guard_proxy_name: Required.
        :type resource_guard_proxy_name: str
        :param parameters: Request body for operation. Is either a UnlockDeleteRequest type or a IO
         type. Required.
        :type parameters: ~azure.mgmt.recoveryservicesbackup.activestamp.models.UnlockDeleteRequest or
         IO
        :keyword content_type: Body Parameter content-type. Known values are: 'application/json'.
         Default value is None.
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: UnlockDeleteResponse or the result of cls(response)
        :rtype: ~azure.mgmt.recoveryservicesbackup.activestamp.models.UnlockDeleteResponse
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

        api_version: Literal["2023-02-01"] = kwargs.pop(
            "api_version", _params.pop("api-version", self._config.api_version)
        )
        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[_models.UnlockDeleteResponse] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(parameters, (IO, bytes)):
            _content = parameters
        else:
            _json = self._serialize.body(parameters, "UnlockDeleteRequest")

        request = build_unlock_delete_request(
            vault_name=vault_name,
            resource_group_name=resource_group_name,
            resource_guard_proxy_name=resource_guard_proxy_name,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            content_type=content_type,
            json=_json,
            content=_content,
            template_url=self.unlock_delete.metadata["url"],
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

        deserialized = self._deserialize("UnlockDeleteResponse", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    unlock_delete.metadata = {
        "url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{vaultName}/backupResourceGuardProxies/{resourceGuardProxyName}/unlockDelete"
    }
