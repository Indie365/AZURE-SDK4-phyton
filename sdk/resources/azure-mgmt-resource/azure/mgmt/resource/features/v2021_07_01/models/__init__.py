# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from ._models_py3 import AuthorizationProfile
from ._models_py3 import ErrorDefinition
from ._models_py3 import ErrorResponse
from ._models_py3 import FeatureOperationsListResult
from ._models_py3 import FeatureProperties
from ._models_py3 import FeatureResult
from ._models_py3 import Operation
from ._models_py3 import OperationDisplay
from ._models_py3 import OperationListResult
from ._models_py3 import ProxyResource
from ._models_py3 import SubscriptionFeatureRegistration
from ._models_py3 import SubscriptionFeatureRegistrationList
from ._models_py3 import SubscriptionFeatureRegistrationProperties

from ._feature_client_enums import SubscriptionFeatureRegistrationApprovalType
from ._feature_client_enums import SubscriptionFeatureRegistrationState
from ._patch import __all__ as _patch_all
from ._patch import *  # pylint: disable=unused-wildcard-import
from ._patch import patch_sdk as _patch_sdk

__all__ = [
    "AuthorizationProfile",
    "ErrorDefinition",
    "ErrorResponse",
    "FeatureOperationsListResult",
    "FeatureProperties",
    "FeatureResult",
    "Operation",
    "OperationDisplay",
    "OperationListResult",
    "ProxyResource",
    "SubscriptionFeatureRegistration",
    "SubscriptionFeatureRegistrationList",
    "SubscriptionFeatureRegistrationProperties",
    "SubscriptionFeatureRegistrationApprovalType",
    "SubscriptionFeatureRegistrationState",
]
__all__.extend([p for p in _patch_all if p not in __all__])
_patch_sdk()
