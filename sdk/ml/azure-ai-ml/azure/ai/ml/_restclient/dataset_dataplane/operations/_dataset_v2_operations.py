# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import functools
from typing import TYPE_CHECKING
import warnings

from azure.core.exceptions import ClientAuthenticationError, HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.paging import ItemPaged
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpResponse
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator import distributed_trace
from azure.mgmt.core.exceptions import ARMErrorFormat
from msrest import Serializer

from .. import models as _models
from .._vendor import _convert_request, _format_url_section

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Callable, Dict, Generic, Iterable, List, Optional, TypeVar
    T = TypeVar('T')
    ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

_SERIALIZER = Serializer()
_SERIALIZER.client_side_validation = False
# fmt: off

def build_create_request(
    subscription_id,  # type: str
    resource_group_name,  # type: str
    workspace_name,  # type: str
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    content_type = kwargs.pop('content_type', None)  # type: Optional[str]
    if_exists_update = kwargs.pop('if_exists_update', False)  # type: Optional[bool]

    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", '/dataset/v2.0/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearningServices/workspaces/{workspaceName}/datasets')
    path_format_arguments = {
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, 'str'),
        "resourceGroupName": _SERIALIZER.url("resource_group_name", resource_group_name, 'str'),
        "workspaceName": _SERIALIZER.url("workspace_name", workspace_name, 'str'),
    }

    url = _format_url_section(url, **path_format_arguments)

    # Construct parameters
    query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    if if_exists_update is not None:
        query_parameters['ifExistsUpdate'] = _SERIALIZER.query("if_exists_update", if_exists_update, 'bool')

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    if content_type is not None:
        header_parameters['Content-Type'] = _SERIALIZER.header("content_type", content_type, 'str')
    header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="POST",
        url=url,
        params=query_parameters,
        headers=header_parameters,
        **kwargs
    )


def build_delete_all_datasets_request(
    subscription_id,  # type: str
    resource_group_name,  # type: str
    workspace_name,  # type: str
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", '/dataset/v2.0/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearningServices/workspaces/{workspaceName}/datasets')
    path_format_arguments = {
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, 'str'),
        "resourceGroupName": _SERIALIZER.url("resource_group_name", resource_group_name, 'str'),
        "workspaceName": _SERIALIZER.url("workspace_name", workspace_name, 'str'),
    }

    url = _format_url_section(url, **path_format_arguments)

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="DELETE",
        url=url,
        headers=header_parameters,
        **kwargs
    )


def build_list_request(
    subscription_id,  # type: str
    resource_group_name,  # type: str
    workspace_name,  # type: str
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    names = kwargs.pop('names', None)  # type: Optional[List[str]]
    search_text = kwargs.pop('search_text', None)  # type: Optional[str]
    continuation_token_parameter = kwargs.pop('continuation_token_parameter', None)  # type: Optional[str]
    page_size = kwargs.pop('page_size', None)  # type: Optional[int]

    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", '/dataset/v2.0/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearningServices/workspaces/{workspaceName}/datasets')
    path_format_arguments = {
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, 'str'),
        "resourceGroupName": _SERIALIZER.url("resource_group_name", resource_group_name, 'str'),
        "workspaceName": _SERIALIZER.url("workspace_name", workspace_name, 'str'),
    }

    url = _format_url_section(url, **path_format_arguments)

    # Construct parameters
    query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    if names is not None:
        query_parameters['names'] = _SERIALIZER.query("names", names, '[str]')
    if search_text is not None:
        query_parameters['searchText'] = _SERIALIZER.query("search_text", search_text, 'str')
    if continuation_token_parameter is not None:
        query_parameters['continuationToken'] = _SERIALIZER.query("continuation_token_parameter", continuation_token_parameter, 'str')
    if page_size is not None:
        query_parameters['pageSize'] = _SERIALIZER.query("page_size", page_size, 'int')

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=url,
        params=query_parameters,
        headers=header_parameters,
        **kwargs
    )


def build_delete_dataset_by_name_request(
    subscription_id,  # type: str
    resource_group_name,  # type: str
    workspace_name,  # type: str
    name,  # type: str
    version_id,  # type: str
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", '/dataset/v2.0/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearningServices/workspaces/{workspaceName}/datasets/{name}/versions/{versionId}')
    path_format_arguments = {
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, 'str'),
        "resourceGroupName": _SERIALIZER.url("resource_group_name", resource_group_name, 'str'),
        "workspaceName": _SERIALIZER.url("workspace_name", workspace_name, 'str'),
        "name": _SERIALIZER.url("name", name, 'str'),
        "versionId": _SERIALIZER.url("version_id", version_id, 'str'),
    }

    url = _format_url_section(url, **path_format_arguments)

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="DELETE",
        url=url,
        headers=header_parameters,
        **kwargs
    )


def build_update_dataset_by_name_and_version_request(
    subscription_id,  # type: str
    resource_group_name,  # type: str
    workspace_name,  # type: str
    name,  # type: str
    version_id,  # type: str
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    content_type = kwargs.pop('content_type', None)  # type: Optional[str]

    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", '/dataset/v2.0/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearningServices/workspaces/{workspaceName}/datasets/{name}/versions/{versionId}')
    path_format_arguments = {
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, 'str'),
        "resourceGroupName": _SERIALIZER.url("resource_group_name", resource_group_name, 'str'),
        "workspaceName": _SERIALIZER.url("workspace_name", workspace_name, 'str'),
        "name": _SERIALIZER.url("name", name, 'str'),
        "versionId": _SERIALIZER.url("version_id", version_id, 'str'),
    }

    url = _format_url_section(url, **path_format_arguments)

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    if content_type is not None:
        header_parameters['Content-Type'] = _SERIALIZER.header("content_type", content_type, 'str')
    header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="PUT",
        url=url,
        headers=header_parameters,
        **kwargs
    )


def build_get_dataset_by_id_request(
    subscription_id,  # type: str
    resource_group_name,  # type: str
    workspace_name,  # type: str
    dataset_id,  # type: str
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", '/dataset/v2.0/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearningServices/workspaces/{workspaceName}/datasets/{datasetId}')
    path_format_arguments = {
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, 'str'),
        "resourceGroupName": _SERIALIZER.url("resource_group_name", resource_group_name, 'str'),
        "workspaceName": _SERIALIZER.url("workspace_name", workspace_name, 'str'),
        "datasetId": _SERIALIZER.url("dataset_id", dataset_id, 'str'),
    }

    url = _format_url_section(url, **path_format_arguments)

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=url,
        headers=header_parameters,
        **kwargs
    )


def build_update_dataset_request(
    subscription_id,  # type: str
    resource_group_name,  # type: str
    workspace_name,  # type: str
    dataset_id,  # type: str
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    content_type = kwargs.pop('content_type', None)  # type: Optional[str]

    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", '/dataset/v2.0/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearningServices/workspaces/{workspaceName}/datasets/{datasetId}')
    path_format_arguments = {
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, 'str'),
        "resourceGroupName": _SERIALIZER.url("resource_group_name", resource_group_name, 'str'),
        "workspaceName": _SERIALIZER.url("workspace_name", workspace_name, 'str'),
        "datasetId": _SERIALIZER.url("dataset_id", dataset_id, 'str'),
    }

    url = _format_url_section(url, **path_format_arguments)

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    if content_type is not None:
        header_parameters['Content-Type'] = _SERIALIZER.header("content_type", content_type, 'str')
    header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="PUT",
        url=url,
        headers=header_parameters,
        **kwargs
    )


def build_get_dataset_by_name_request(
    subscription_id,  # type: str
    resource_group_name,  # type: str
    workspace_name,  # type: str
    dataset_name,  # type: str
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    version_id = kwargs.pop('version_id', None)  # type: Optional[str]

    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", '/dataset/v2.0/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearningServices/workspaces/{workspaceName}/datasets/query/name={datasetName}')
    path_format_arguments = {
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, 'str'),
        "resourceGroupName": _SERIALIZER.url("resource_group_name", resource_group_name, 'str'),
        "workspaceName": _SERIALIZER.url("workspace_name", workspace_name, 'str'),
        "datasetName": _SERIALIZER.url("dataset_name", dataset_name, 'str'),
    }

    url = _format_url_section(url, **path_format_arguments)

    # Construct parameters
    query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    if version_id is not None:
        query_parameters['versionId'] = _SERIALIZER.query("version_id", version_id, 'str')

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=url,
        params=query_parameters,
        headers=header_parameters,
        **kwargs
    )

# fmt: on
class DatasetV2Operations(object):
    """DatasetV2Operations operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~azure.mgmt.machinelearningservices.models
    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = _models

    def __init__(self, client, config, serializer, deserializer):
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    @distributed_trace
    def create(
        self,
        subscription_id,  # type: str
        resource_group_name,  # type: str
        workspace_name,  # type: str
        if_exists_update=False,  # type: Optional[bool]
        body=None,  # type: Optional["_models.DatasetV2"]
        **kwargs  # type: Any
    ):
        # type: (...) -> "_models.DatasetV2"
        """Create new dataset.

        :param subscription_id: The Azure Subscription ID.
        :type subscription_id: str
        :param resource_group_name: The Name of the resource group in which the workspace is located.
        :type resource_group_name: str
        :param workspace_name: The name of the workspace.
        :type workspace_name: str
        :param if_exists_update:
        :type if_exists_update: bool
        :param body:
        :type body: ~azure.mgmt.machinelearningservices.models.DatasetV2
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: DatasetV2, or the result of cls(response)
        :rtype: ~azure.mgmt.machinelearningservices.models.DatasetV2
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.DatasetV2"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        content_type = kwargs.pop('content_type', "application/json")  # type: Optional[str]

        if body is not None:
            _json = self._serialize.body(body, 'DatasetV2')
        else:
            _json = None

        request = build_create_request(
            subscription_id=subscription_id,
            resource_group_name=resource_group_name,
            workspace_name=workspace_name,
            content_type=content_type,
            json=_json,
            if_exists_update=if_exists_update,
            template_url=self.create.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('DatasetV2', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    create.metadata = {'url': '/dataset/v2.0/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearningServices/workspaces/{workspaceName}/datasets'}  # type: ignore


    @distributed_trace
    def delete_all_datasets(
        self,
        subscription_id,  # type: str
        resource_group_name,  # type: str
        workspace_name,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """Delete all datasets in the workspace.

        :param subscription_id: The Azure Subscription ID.
        :type subscription_id: str
        :param resource_group_name: The Name of the resource group in which the workspace is located.
        :type resource_group_name: str
        :param workspace_name: The name of the workspace.
        :type workspace_name: str
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

        
        request = build_delete_all_datasets_request(
            subscription_id=subscription_id,
            resource_group_name=resource_group_name,
            workspace_name=workspace_name,
            template_url=self.delete_all_datasets.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in []:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    delete_all_datasets.metadata = {'url': '/dataset/v2.0/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearningServices/workspaces/{workspaceName}/datasets'}  # type: ignore


    @distributed_trace
    def list(
        self,
        subscription_id,  # type: str
        resource_group_name,  # type: str
        workspace_name,  # type: str
        names=None,  # type: Optional[List[str]]
        search_text=None,  # type: Optional[str]
        continuation_token_parameter=None,  # type: Optional[str]
        page_size=None,  # type: Optional[int]
        **kwargs  # type: Any
    ):
        # type: (...) -> Iterable["_models.PaginatedDatasetV2List"]
        """Get a list of datasets.

        :param subscription_id: The Azure Subscription ID.
        :type subscription_id: str
        :param resource_group_name: The Name of the resource group in which the workspace is located.
        :type resource_group_name: str
        :param workspace_name: The name of the workspace.
        :type workspace_name: str
        :param names:
        :type names: list[str]
        :param search_text:
        :type search_text: str
        :param continuation_token_parameter:
        :type continuation_token_parameter: str
        :param page_size:
        :type page_size: int
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either PaginatedDatasetV2List or the result of
         cls(response)
        :rtype:
         ~azure.core.paging.ItemPaged[~azure.mgmt.machinelearningservices.models.PaginatedDatasetV2List]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.PaginatedDatasetV2List"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        def prepare_request(next_link=None):
            if not next_link:
                
                request = build_list_request(
                    subscription_id=subscription_id,
                    resource_group_name=resource_group_name,
                    workspace_name=workspace_name,
                    names=names,
                    search_text=search_text,
                    continuation_token_parameter=continuation_token_parameter,
                    page_size=page_size,
                    template_url=self.list.metadata['url'],
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)

            else:
                
                request = build_list_request(
                    subscription_id=subscription_id,
                    resource_group_name=resource_group_name,
                    workspace_name=workspace_name,
                    names=names,
                    search_text=search_text,
                    continuation_token_parameter=continuation_token_parameter,
                    page_size=page_size,
                    template_url=next_link,
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)
                request.method = "GET"
            return request

        def extract_data(pipeline_response):
            deserialized = self._deserialize("PaginatedDatasetV2List", pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.next_link or None, iter(list_of_elem)

        def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
                raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

            return pipeline_response


        return ItemPaged(
            get_next, extract_data
        )
    list.metadata = {'url': '/dataset/v2.0/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearningServices/workspaces/{workspaceName}/datasets'}  # type: ignore

    @distributed_trace
    def delete_dataset_by_name(
        self,
        subscription_id,  # type: str
        resource_group_name,  # type: str
        workspace_name,  # type: str
        name,  # type: str
        version_id,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """Delete a dataset.

        :param subscription_id: The Azure Subscription ID.
        :type subscription_id: str
        :param resource_group_name: The Name of the resource group in which the workspace is located.
        :type resource_group_name: str
        :param workspace_name: The name of the workspace.
        :type workspace_name: str
        :param name:
        :type name: str
        :param version_id:
        :type version_id: str
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

        
        request = build_delete_dataset_by_name_request(
            subscription_id=subscription_id,
            resource_group_name=resource_group_name,
            workspace_name=workspace_name,
            name=name,
            version_id=version_id,
            template_url=self.delete_dataset_by_name.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in []:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    delete_dataset_by_name.metadata = {'url': '/dataset/v2.0/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearningServices/workspaces/{workspaceName}/datasets/{name}/versions/{versionId}'}  # type: ignore


    @distributed_trace
    def update_dataset_by_name_and_version(
        self,
        subscription_id,  # type: str
        resource_group_name,  # type: str
        workspace_name,  # type: str
        name,  # type: str
        version_id,  # type: str
        body=None,  # type: Optional["_models.DatasetV2"]
        **kwargs  # type: Any
    ):
        # type: (...) -> "_models.DatasetV2"
        """Update a dataset by its name and version.

        :param subscription_id: The Azure Subscription ID.
        :type subscription_id: str
        :param resource_group_name: The Name of the resource group in which the workspace is located.
        :type resource_group_name: str
        :param workspace_name: The name of the workspace.
        :type workspace_name: str
        :param name:
        :type name: str
        :param version_id:
        :type version_id: str
        :param body:
        :type body: ~azure.mgmt.machinelearningservices.models.DatasetV2
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: DatasetV2, or the result of cls(response)
        :rtype: ~azure.mgmt.machinelearningservices.models.DatasetV2
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.DatasetV2"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        content_type = kwargs.pop('content_type', "application/json")  # type: Optional[str]

        if body is not None:
            _json = self._serialize.body(body, 'DatasetV2')
        else:
            _json = None

        request = build_update_dataset_by_name_and_version_request(
            subscription_id=subscription_id,
            resource_group_name=resource_group_name,
            workspace_name=workspace_name,
            name=name,
            version_id=version_id,
            content_type=content_type,
            json=_json,
            template_url=self.update_dataset_by_name_and_version.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('DatasetV2', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    update_dataset_by_name_and_version.metadata = {'url': '/dataset/v2.0/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearningServices/workspaces/{workspaceName}/datasets/{name}/versions/{versionId}'}  # type: ignore


    @distributed_trace
    def get_dataset_by_id(
        self,
        subscription_id,  # type: str
        resource_group_name,  # type: str
        workspace_name,  # type: str
        dataset_id,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> "_models.DatasetV2"
        """Get a dataset for a given dataset id.

        :param subscription_id: The Azure Subscription ID.
        :type subscription_id: str
        :param resource_group_name: The Name of the resource group in which the workspace is located.
        :type resource_group_name: str
        :param workspace_name: The name of the workspace.
        :type workspace_name: str
        :param dataset_id:
        :type dataset_id: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: DatasetV2, or the result of cls(response)
        :rtype: ~azure.mgmt.machinelearningservices.models.DatasetV2
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.DatasetV2"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        
        request = build_get_dataset_by_id_request(
            subscription_id=subscription_id,
            resource_group_name=resource_group_name,
            workspace_name=workspace_name,
            dataset_id=dataset_id,
            template_url=self.get_dataset_by_id.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('DatasetV2', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_dataset_by_id.metadata = {'url': '/dataset/v2.0/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearningServices/workspaces/{workspaceName}/datasets/{datasetId}'}  # type: ignore


    @distributed_trace
    def update_dataset(
        self,
        subscription_id,  # type: str
        resource_group_name,  # type: str
        workspace_name,  # type: str
        dataset_id,  # type: str
        body=None,  # type: Optional["_models.DatasetV2"]
        **kwargs  # type: Any
    ):
        # type: (...) -> "_models.DatasetV2"
        """Update a dataset.

        :param subscription_id: The Azure Subscription ID.
        :type subscription_id: str
        :param resource_group_name: The Name of the resource group in which the workspace is located.
        :type resource_group_name: str
        :param workspace_name: The name of the workspace.
        :type workspace_name: str
        :param dataset_id:
        :type dataset_id: str
        :param body:
        :type body: ~azure.mgmt.machinelearningservices.models.DatasetV2
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: DatasetV2, or the result of cls(response)
        :rtype: ~azure.mgmt.machinelearningservices.models.DatasetV2
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.DatasetV2"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        content_type = kwargs.pop('content_type', "application/json")  # type: Optional[str]

        if body is not None:
            _json = self._serialize.body(body, 'DatasetV2')
        else:
            _json = None

        request = build_update_dataset_request(
            subscription_id=subscription_id,
            resource_group_name=resource_group_name,
            workspace_name=workspace_name,
            dataset_id=dataset_id,
            content_type=content_type,
            json=_json,
            template_url=self.update_dataset.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('DatasetV2', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    update_dataset.metadata = {'url': '/dataset/v2.0/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearningServices/workspaces/{workspaceName}/datasets/{datasetId}'}  # type: ignore


    @distributed_trace
    def get_dataset_by_name(
        self,
        subscription_id,  # type: str
        resource_group_name,  # type: str
        workspace_name,  # type: str
        dataset_name,  # type: str
        version_id=None,  # type: Optional[str]
        **kwargs  # type: Any
    ):
        # type: (...) -> "_models.DatasetV2"
        """Get a dataset for a given dataset name.

        :param subscription_id: The Azure Subscription ID.
        :type subscription_id: str
        :param resource_group_name: The Name of the resource group in which the workspace is located.
        :type resource_group_name: str
        :param workspace_name: The name of the workspace.
        :type workspace_name: str
        :param dataset_name:
        :type dataset_name: str
        :param version_id:
        :type version_id: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: DatasetV2, or the result of cls(response)
        :rtype: ~azure.mgmt.machinelearningservices.models.DatasetV2
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.DatasetV2"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        
        request = build_get_dataset_by_name_request(
            subscription_id=subscription_id,
            resource_group_name=resource_group_name,
            workspace_name=workspace_name,
            dataset_name=dataset_name,
            version_id=version_id,
            template_url=self.get_dataset_by_name.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('DatasetV2', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_dataset_by_name.metadata = {'url': '/dataset/v2.0/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearningServices/workspaces/{workspaceName}/datasets/query/name={datasetName}'}  # type: ignore

