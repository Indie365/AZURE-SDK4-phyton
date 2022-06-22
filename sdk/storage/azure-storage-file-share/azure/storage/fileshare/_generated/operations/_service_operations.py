# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import TYPE_CHECKING

from msrest import Serializer

from azure.core.exceptions import ClientAuthenticationError, HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpResponse
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator import distributed_trace

from .. import models as _models
from .._vendor import _convert_request, _format_url_section

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Callable, Dict, List, Optional, TypeVar, Union
    T = TypeVar('T')
    ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

_SERIALIZER = Serializer()
_SERIALIZER.client_side_validation = False
# fmt: off

def build_set_properties_request(
    url,  # type: str
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    restype = kwargs.pop('restype', "service")  # type: str
    comp = kwargs.pop('comp', "properties")  # type: str
    version = kwargs.pop('version', "2021-06-08")  # type: str
    content_type = kwargs.pop('content_type', None)  # type: Optional[str]
    timeout = kwargs.pop('timeout', None)  # type: Optional[int]

    accept = "application/xml"
    # Construct URL
    _url = kwargs.pop("template_url", "{url}")
    path_format_arguments = {
        "url": _SERIALIZER.url("url", url, 'str', skip_quote=True),
    }

    _url = _format_url_section(_url, **path_format_arguments)

    # Construct parameters
    _query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    _query_parameters['restype'] = _SERIALIZER.query("restype", restype, 'str')
    _query_parameters['comp'] = _SERIALIZER.query("comp", comp, 'str')
    if timeout is not None:
        _query_parameters['timeout'] = _SERIALIZER.query("timeout", timeout, 'int', minimum=0)

    # Construct headers
    _header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    _header_parameters['x-ms-version'] = _SERIALIZER.header("version", version, 'str')
    if content_type is not None:
        _header_parameters['Content-Type'] = _SERIALIZER.header("content_type", content_type, 'str')
    _header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="PUT",
        url=_url,
        params=_query_parameters,
        headers=_header_parameters,
        **kwargs
    )


def build_get_properties_request(
    url,  # type: str
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    restype = kwargs.pop('restype', "service")  # type: str
    comp = kwargs.pop('comp', "properties")  # type: str
    version = kwargs.pop('version', "2021-06-08")  # type: str
    timeout = kwargs.pop('timeout', None)  # type: Optional[int]

    accept = "application/xml"
    # Construct URL
    _url = kwargs.pop("template_url", "{url}")
    path_format_arguments = {
        "url": _SERIALIZER.url("url", url, 'str', skip_quote=True),
    }

    _url = _format_url_section(_url, **path_format_arguments)

    # Construct parameters
    _query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    _query_parameters['restype'] = _SERIALIZER.query("restype", restype, 'str')
    _query_parameters['comp'] = _SERIALIZER.query("comp", comp, 'str')
    if timeout is not None:
        _query_parameters['timeout'] = _SERIALIZER.query("timeout", timeout, 'int', minimum=0)

    # Construct headers
    _header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    _header_parameters['x-ms-version'] = _SERIALIZER.header("version", version, 'str')
    _header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=_url,
        params=_query_parameters,
        headers=_header_parameters,
        **kwargs
    )


def build_list_shares_segment_request(
    url,  # type: str
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    comp = kwargs.pop('comp', "list")  # type: str
    version = kwargs.pop('version', "2021-06-08")  # type: str
    prefix = kwargs.pop('prefix', None)  # type: Optional[str]
    marker = kwargs.pop('marker', None)  # type: Optional[str]
    maxresults = kwargs.pop('maxresults', None)  # type: Optional[int]
    include = kwargs.pop('include', None)  # type: Optional[List[Union[str, "_models.ListSharesIncludeType"]]]
    timeout = kwargs.pop('timeout', None)  # type: Optional[int]

    accept = "application/xml"
    # Construct URL
    _url = kwargs.pop("template_url", "{url}")
    path_format_arguments = {
        "url": _SERIALIZER.url("url", url, 'str', skip_quote=True),
    }

    _url = _format_url_section(_url, **path_format_arguments)

    # Construct parameters
    _query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    _query_parameters['comp'] = _SERIALIZER.query("comp", comp, 'str')
    if prefix is not None:
        _query_parameters['prefix'] = _SERIALIZER.query("prefix", prefix, 'str')
    if marker is not None:
        _query_parameters['marker'] = _SERIALIZER.query("marker", marker, 'str')
    if maxresults is not None:
        _query_parameters['maxresults'] = _SERIALIZER.query("maxresults", maxresults, 'int', minimum=1)
    if include is not None:
        _query_parameters['include'] = _SERIALIZER.query("include", include, '[str]', div=',')
    if timeout is not None:
        _query_parameters['timeout'] = _SERIALIZER.query("timeout", timeout, 'int', minimum=0)

    # Construct headers
    _header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    _header_parameters['x-ms-version'] = _SERIALIZER.header("version", version, 'str')
    _header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=_url,
        params=_query_parameters,
        headers=_header_parameters,
        **kwargs
    )

# fmt: on
class ServiceOperations(object):
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~azure.storage.fileshare.AzureFileStorage`'s
        :attr:`service` attribute.
    """

    models = _models

    def __init__(self, *args, **kwargs):
        args = list(args)
        self._client = args.pop(0) if args else kwargs.pop("client")
        self._config = args.pop(0) if args else kwargs.pop("config")
        self._serialize = args.pop(0) if args else kwargs.pop("serializer")
        self._deserialize = args.pop(0) if args else kwargs.pop("deserializer")


    @distributed_trace
    def set_properties(  # pylint: disable=inconsistent-return-statements
        self,
        storage_service_properties,  # type: "_models.StorageServiceProperties"
        timeout=None,  # type: Optional[int]
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """Sets properties for a storage account's File service endpoint, including properties for Storage
        Analytics metrics and CORS (Cross-Origin Resource Sharing) rules.

        :param storage_service_properties: The StorageService properties.
        :type storage_service_properties: ~azure.storage.fileshare.models.StorageServiceProperties
        :param timeout: The timeout parameter is expressed in seconds. For more information, see
         :code:`<a
         href="https://docs.microsoft.com/en-us/rest/api/storageservices/Setting-Timeouts-for-File-Service-Operations?redirectedfrom=MSDN">Setting
         Timeouts for File Service Operations.</a>`. Default value is None.
        :type timeout: int
        :keyword restype: restype. Default value is "service". Note that overriding this default value
         may result in unsupported behavior.
        :paramtype restype: str
        :keyword comp: comp. Default value is "properties". Note that overriding this default value may
         result in unsupported behavior.
        :paramtype comp: str
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

        restype = kwargs.pop('restype', "service")  # type: str
        comp = kwargs.pop('comp', "properties")  # type: str
        content_type = kwargs.pop('content_type', "application/xml")  # type: Optional[str]

        _content = self._serialize.body(storage_service_properties, 'StorageServiceProperties', is_xml=True)

        request = build_set_properties_request(
            url=self._config.url,
            restype=restype,
            comp=comp,
            version=self._config.version,
            content_type=content_type,
            content=_content,
            timeout=timeout,
            template_url=self.set_properties.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = self._client._pipeline.run(  # pylint: disable=protected-access
            request,
            stream=False,
            **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [202]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.StorageError, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        response_headers = {}
        response_headers['x-ms-request-id']=self._deserialize('str', response.headers.get('x-ms-request-id'))
        response_headers['x-ms-version']=self._deserialize('str', response.headers.get('x-ms-version'))


        if cls:
            return cls(pipeline_response, None, response_headers)

    set_properties.metadata = {'url': "{url}"}  # type: ignore


    @distributed_trace
    def get_properties(
        self,
        timeout=None,  # type: Optional[int]
        **kwargs  # type: Any
    ):
        # type: (...) -> "_models.StorageServiceProperties"
        """Gets the properties of a storage account's File service, including properties for Storage
        Analytics metrics and CORS (Cross-Origin Resource Sharing) rules.

        :param timeout: The timeout parameter is expressed in seconds. For more information, see
         :code:`<a
         href="https://docs.microsoft.com/en-us/rest/api/storageservices/Setting-Timeouts-for-File-Service-Operations?redirectedfrom=MSDN">Setting
         Timeouts for File Service Operations.</a>`. Default value is None.
        :type timeout: int
        :keyword restype: restype. Default value is "service". Note that overriding this default value
         may result in unsupported behavior.
        :paramtype restype: str
        :keyword comp: comp. Default value is "properties". Note that overriding this default value may
         result in unsupported behavior.
        :paramtype comp: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: StorageServiceProperties, or the result of cls(response)
        :rtype: ~azure.storage.fileshare.models.StorageServiceProperties
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.StorageServiceProperties"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        restype = kwargs.pop('restype', "service")  # type: str
        comp = kwargs.pop('comp', "properties")  # type: str

        
        request = build_get_properties_request(
            url=self._config.url,
            restype=restype,
            comp=comp,
            version=self._config.version,
            timeout=timeout,
            template_url=self.get_properties.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = self._client._pipeline.run(  # pylint: disable=protected-access
            request,
            stream=False,
            **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.StorageError, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        response_headers = {}
        response_headers['x-ms-request-id']=self._deserialize('str', response.headers.get('x-ms-request-id'))
        response_headers['x-ms-version']=self._deserialize('str', response.headers.get('x-ms-version'))

        deserialized = self._deserialize('StorageServiceProperties', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, response_headers)

        return deserialized

    get_properties.metadata = {'url': "{url}"}  # type: ignore


    @distributed_trace
    def list_shares_segment(
        self,
        prefix=None,  # type: Optional[str]
        marker=None,  # type: Optional[str]
        maxresults=None,  # type: Optional[int]
        include=None,  # type: Optional[List[Union[str, "_models.ListSharesIncludeType"]]]
        timeout=None,  # type: Optional[int]
        **kwargs  # type: Any
    ):
        # type: (...) -> "_models.ListSharesResponse"
        """The List Shares Segment operation returns a list of the shares and share snapshots under the
        specified account.

        :param prefix: Filters the results to return only entries whose name begins with the specified
         prefix. Default value is None.
        :type prefix: str
        :param marker: A string value that identifies the portion of the list to be returned with the
         next list operation. The operation returns a marker value within the response body if the list
         returned was not complete. The marker value may then be used in a subsequent call to request
         the next set of list items. The marker value is opaque to the client. Default value is None.
        :type marker: str
        :param maxresults: Specifies the maximum number of entries to return. If the request does not
         specify maxresults, or specifies a value greater than 5,000, the server will return up to 5,000
         items. Default value is None.
        :type maxresults: int
        :param include: Include this parameter to specify one or more datasets to include in the
         response. Default value is None.
        :type include: list[str or ~azure.storage.fileshare.models.ListSharesIncludeType]
        :param timeout: The timeout parameter is expressed in seconds. For more information, see
         :code:`<a
         href="https://docs.microsoft.com/en-us/rest/api/storageservices/Setting-Timeouts-for-File-Service-Operations?redirectedfrom=MSDN">Setting
         Timeouts for File Service Operations.</a>`. Default value is None.
        :type timeout: int
        :keyword comp: comp. Default value is "list". Note that overriding this default value may
         result in unsupported behavior.
        :paramtype comp: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ListSharesResponse, or the result of cls(response)
        :rtype: ~azure.storage.fileshare.models.ListSharesResponse
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.ListSharesResponse"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        comp = kwargs.pop('comp', "list")  # type: str

        
        request = build_list_shares_segment_request(
            url=self._config.url,
            comp=comp,
            version=self._config.version,
            prefix=prefix,
            marker=marker,
            maxresults=maxresults,
            include=include,
            timeout=timeout,
            template_url=self.list_shares_segment.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = self._client._pipeline.run(  # pylint: disable=protected-access
            request,
            stream=False,
            **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.StorageError, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        response_headers = {}
        response_headers['x-ms-request-id']=self._deserialize('str', response.headers.get('x-ms-request-id'))
        response_headers['x-ms-version']=self._deserialize('str', response.headers.get('x-ms-version'))

        deserialized = self._deserialize('ListSharesResponse', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, response_headers)

        return deserialized

    list_shares_segment.metadata = {'url': "{url}"}  # type: ignore

