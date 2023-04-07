# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import sys
from typing import Any, Callable, Dict, Optional, TypeVar, Union

from azure.core.exceptions import (
    ClientAuthenticationError,
    HttpResponseError,
    ResourceExistsError,
    ResourceNotFoundError,
    ResourceNotModifiedError,
    map_error,
)
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpResponse
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator import distributed_trace
from azure.core.utils import case_insensitive_dict
from azure.mgmt.core.exceptions import ARMErrorFormat

from .. import models as _models
from .._serialization import Serializer
from .._vendor import _convert_request, _format_url_section

if sys.version_info >= (3, 8):
    from typing import Literal  # pylint: disable=no-name-in-module, ungrouped-imports
else:
    from typing_extensions import Literal  # type: ignore  # pylint: disable=ungrouped-imports
T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

_SERIALIZER = Serializer()
_SERIALIZER.client_side_validation = False


def build_get_request(
    resource_scope: str,
    *,
    scope: Union[str, _models.Scope],
    region: str,
    term: Union[str, _models.Term],
    look_back_period: Union[str, _models.LookBackPeriod],
    product: str,
    **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version: Literal["2021-10-01"] = kwargs.pop("api_version", _params.pop("api-version", "2021-10-01"))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop(
        "template_url", "/{resourceScope}/providers/Microsoft.Consumption/reservationRecommendationDetails"
    )
    path_format_arguments = {
        "resourceScope": _SERIALIZER.url("resource_scope", resource_scope, "str", skip_quote=True),
    }

    _url: str = _format_url_section(_url, **path_format_arguments)  # type: ignore

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")
    _params["scope"] = _SERIALIZER.query("scope", scope, "str")
    _params["region"] = _SERIALIZER.query("region", region, "str")
    _params["term"] = _SERIALIZER.query("term", term, "str")
    _params["lookBackPeriod"] = _SERIALIZER.query("look_back_period", look_back_period, "str")
    _params["product"] = _SERIALIZER.query("product", product, "str")

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=_url, params=_params, headers=_headers, **kwargs)


class ReservationRecommendationDetailsOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~azure.mgmt.consumption.ConsumptionManagementClient`'s
        :attr:`reservation_recommendation_details` attribute.
    """

    models = _models

    def __init__(self, *args, **kwargs):
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    @distributed_trace
    def get(
        self,
        resource_scope: str,
        scope: Union[str, _models.Scope],
        region: str,
        term: Union[str, _models.Term],
        look_back_period: Union[str, _models.LookBackPeriod],
        product: str,
        **kwargs: Any
    ) -> Optional[_models.ReservationRecommendationDetailsModel]:
        """Details of a reservation recommendation for what-if analysis of reserved instances.

        :param resource_scope: The scope associated with reservation recommendation details operations.
         This includes '/subscriptions/{subscriptionId}/' for subscription scope,
         '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}' for resource group scope,
         /providers/Microsoft.Billing/billingAccounts/{billingAccountId}' for BillingAccount scope, and
         '/providers/Microsoft.Billing/billingAccounts/{billingAccountId}/billingProfiles/{billingProfileId}'
         for billingProfile scope. Required.
        :type resource_scope: str
        :param scope: Scope of the reservation. Known values are: "Single" and "Shared". Required.
        :type scope: str or ~azure.mgmt.consumption.models.Scope
        :param region: Used to select the region the recommendation should be generated for. Required.
        :type region: str
        :param term: Specify length of reservation recommendation term. Known values are: "P1Y" and
         "P3Y". Required.
        :type term: str or ~azure.mgmt.consumption.models.Term
        :param look_back_period: Filter the time period on which reservation recommendation results are
         based. Known values are: "Last7Days", "Last30Days", and "Last60Days". Required.
        :type look_back_period: str or ~azure.mgmt.consumption.models.LookBackPeriod
        :param product: Filter the products for which reservation recommendation results are generated.
         Examples: Standard_DS1_v2 (for VM), Premium_SSD_Managed_Disks_P30 (for Managed Disks).
         Required.
        :type product: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ReservationRecommendationDetailsModel or None or the result of cls(response)
        :rtype: ~azure.mgmt.consumption.models.ReservationRecommendationDetailsModel or None
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

        api_version: Literal["2021-10-01"] = kwargs.pop(
            "api_version", _params.pop("api-version", self._config.api_version)
        )
        cls: ClsType[Optional[_models.ReservationRecommendationDetailsModel]] = kwargs.pop("cls", None)

        request = build_get_request(
            resource_scope=resource_scope,
            scope=scope,
            region=region,
            term=term,
            look_back_period=look_back_period,
            product=product,
            api_version=api_version,
            template_url=self.get.metadata["url"],
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
            error = self._deserialize.failsafe_deserialize(_models.HighCasedErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize("ReservationRecommendationDetailsModel", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get.metadata = {"url": "/{resourceScope}/providers/Microsoft.Consumption/reservationRecommendationDetails"}
