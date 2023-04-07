# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from ._models_py3 import AadConnectivityState
from ._models_py3 import AadExternalSecuritySolution
from ._models_py3 import AadSolutionProperties
from ._models_py3 import AdaptiveApplicationControlGroup
from ._models_py3 import AdaptiveApplicationControlGroups
from ._models_py3 import AdaptiveApplicationControlIssueSummary
from ._models_py3 import AdaptiveNetworkHardening
from ._models_py3 import AdaptiveNetworkHardeningEnforceRequest
from ._models_py3 import AdaptiveNetworkHardeningsList
from ._models_py3 import AllowedConnectionsList
from ._models_py3 import AllowedConnectionsResource
from ._models_py3 import AssessmentLinks
from ._models_py3 import AssessmentStatus
from ._models_py3 import AtaExternalSecuritySolution
from ._models_py3 import AtaSolutionProperties
from ._models_py3 import AzureResourceDetails
from ._models_py3 import AzureResourceLink
from ._models_py3 import CefExternalSecuritySolution
from ._models_py3 import CefSolutionProperties
from ._models_py3 import CloudErrorBody
from ._models_py3 import ConnectableResource
from ._models_py3 import ConnectedResource
from ._models_py3 import ConnectedWorkspace
from ._models_py3 import DiscoveredSecuritySolution
from ._models_py3 import DiscoveredSecuritySolutionList
from ._models_py3 import EffectiveNetworkSecurityGroups
from ._models_py3 import ErrorAdditionalInfo
from ._models_py3 import ExternalSecuritySolution
from ._models_py3 import ExternalSecuritySolutionKind
from ._models_py3 import ExternalSecuritySolutionList
from ._models_py3 import ExternalSecuritySolutionProperties
from ._models_py3 import JitNetworkAccessPoliciesList
from ._models_py3 import JitNetworkAccessPolicy
from ._models_py3 import JitNetworkAccessPolicyInitiatePort
from ._models_py3 import JitNetworkAccessPolicyInitiateRequest
from ._models_py3 import JitNetworkAccessPolicyInitiateVirtualMachine
from ._models_py3 import JitNetworkAccessPolicyVirtualMachine
from ._models_py3 import JitNetworkAccessPortRule
from ._models_py3 import JitNetworkAccessRequest
from ._models_py3 import JitNetworkAccessRequestPort
from ._models_py3 import JitNetworkAccessRequestVirtualMachine
from ._models_py3 import Kind
from ._models_py3 import Location
from ._models_py3 import OnPremiseResourceDetails
from ._models_py3 import OnPremiseSqlResourceDetails
from ._models_py3 import PathRecommendation
from ._models_py3 import ProtectionMode
from ._models_py3 import PublisherInfo
from ._models_py3 import Resource
from ._models_py3 import ResourceDetails
from ._models_py3 import Rule
from ._models_py3 import SecureScoreControlDefinitionItem
from ._models_py3 import SecureScoreControlDefinitionList
from ._models_py3 import SecureScoreControlDefinitionSource
from ._models_py3 import SecureScoreControlDetails
from ._models_py3 import SecureScoreControlList
from ._models_py3 import SecureScoreControlScore
from ._models_py3 import SecureScoreItem
from ._models_py3 import SecureScoresList
from ._models_py3 import SecurityAssessment
from ._models_py3 import SecurityAssessmentList
from ._models_py3 import SecurityAssessmentMetadata
from ._models_py3 import SecurityAssessmentMetadataList
from ._models_py3 import SecurityAssessmentMetadataPartnerData
from ._models_py3 import SecurityAssessmentMetadataProperties
from ._models_py3 import SecurityAssessmentPartnerData
from ._models_py3 import SecuritySolution
from ._models_py3 import SecuritySolutionList
from ._models_py3 import SecuritySolutionsReferenceData
from ._models_py3 import SecuritySolutionsReferenceDataList
from ._models_py3 import ServerVulnerabilityAssessment
from ._models_py3 import ServerVulnerabilityAssessmentsList
from ._models_py3 import TopologyList
from ._models_py3 import TopologyResource
from ._models_py3 import TopologySingleResource
from ._models_py3 import TopologySingleResourceChild
from ._models_py3 import TopologySingleResourceParent
from ._models_py3 import UserRecommendation
from ._models_py3 import VmRecommendation

from ._security_center_enums import AadConnectivityStateEnum
from ._security_center_enums import AdaptiveApplicationControlIssue
from ._security_center_enums import AssessmentStatusCode
from ._security_center_enums import AssessmentType
from ._security_center_enums import Categories
from ._security_center_enums import ConfigurationStatus
from ._security_center_enums import ConnectionType
from ._security_center_enums import ControlType
from ._security_center_enums import Direction
from ._security_center_enums import EnforcementMode
from ._security_center_enums import EnforcementSupport
from ._security_center_enums import ExpandControlsEnum
from ._security_center_enums import ExpandEnum
from ._security_center_enums import ExternalSecuritySolutionKindEnum
from ._security_center_enums import FileType
from ._security_center_enums import ImplementationEffort
from ._security_center_enums import ProtocolEnum
from ._security_center_enums import ProvisioningState
from ._security_center_enums import RecommendationAction
from ._security_center_enums import RecommendationStatus
from ._security_center_enums import RecommendationType
from ._security_center_enums import SecurityFamily
from ._security_center_enums import ServerVulnerabilityAssessmentPropertiesProvisioningState
from ._security_center_enums import Severity
from ._security_center_enums import Source
from ._security_center_enums import SourceSystem
from ._security_center_enums import Status
from ._security_center_enums import StatusReason
from ._security_center_enums import Threats
from ._security_center_enums import TransportProtocol
from ._security_center_enums import UserImpact
from ._patch import __all__ as _patch_all
from ._patch import *  # pylint: disable=unused-wildcard-import
from ._patch import patch_sdk as _patch_sdk

__all__ = [
    "AadConnectivityState",
    "AadExternalSecuritySolution",
    "AadSolutionProperties",
    "AdaptiveApplicationControlGroup",
    "AdaptiveApplicationControlGroups",
    "AdaptiveApplicationControlIssueSummary",
    "AdaptiveNetworkHardening",
    "AdaptiveNetworkHardeningEnforceRequest",
    "AdaptiveNetworkHardeningsList",
    "AllowedConnectionsList",
    "AllowedConnectionsResource",
    "AssessmentLinks",
    "AssessmentStatus",
    "AtaExternalSecuritySolution",
    "AtaSolutionProperties",
    "AzureResourceDetails",
    "AzureResourceLink",
    "CefExternalSecuritySolution",
    "CefSolutionProperties",
    "CloudErrorBody",
    "ConnectableResource",
    "ConnectedResource",
    "ConnectedWorkspace",
    "DiscoveredSecuritySolution",
    "DiscoveredSecuritySolutionList",
    "EffectiveNetworkSecurityGroups",
    "ErrorAdditionalInfo",
    "ExternalSecuritySolution",
    "ExternalSecuritySolutionKind",
    "ExternalSecuritySolutionList",
    "ExternalSecuritySolutionProperties",
    "JitNetworkAccessPoliciesList",
    "JitNetworkAccessPolicy",
    "JitNetworkAccessPolicyInitiatePort",
    "JitNetworkAccessPolicyInitiateRequest",
    "JitNetworkAccessPolicyInitiateVirtualMachine",
    "JitNetworkAccessPolicyVirtualMachine",
    "JitNetworkAccessPortRule",
    "JitNetworkAccessRequest",
    "JitNetworkAccessRequestPort",
    "JitNetworkAccessRequestVirtualMachine",
    "Kind",
    "Location",
    "OnPremiseResourceDetails",
    "OnPremiseSqlResourceDetails",
    "PathRecommendation",
    "ProtectionMode",
    "PublisherInfo",
    "Resource",
    "ResourceDetails",
    "Rule",
    "SecureScoreControlDefinitionItem",
    "SecureScoreControlDefinitionList",
    "SecureScoreControlDefinitionSource",
    "SecureScoreControlDetails",
    "SecureScoreControlList",
    "SecureScoreControlScore",
    "SecureScoreItem",
    "SecureScoresList",
    "SecurityAssessment",
    "SecurityAssessmentList",
    "SecurityAssessmentMetadata",
    "SecurityAssessmentMetadataList",
    "SecurityAssessmentMetadataPartnerData",
    "SecurityAssessmentMetadataProperties",
    "SecurityAssessmentPartnerData",
    "SecuritySolution",
    "SecuritySolutionList",
    "SecuritySolutionsReferenceData",
    "SecuritySolutionsReferenceDataList",
    "ServerVulnerabilityAssessment",
    "ServerVulnerabilityAssessmentsList",
    "TopologyList",
    "TopologyResource",
    "TopologySingleResource",
    "TopologySingleResourceChild",
    "TopologySingleResourceParent",
    "UserRecommendation",
    "VmRecommendation",
    "AadConnectivityStateEnum",
    "AdaptiveApplicationControlIssue",
    "AssessmentStatusCode",
    "AssessmentType",
    "Categories",
    "ConfigurationStatus",
    "ConnectionType",
    "ControlType",
    "Direction",
    "EnforcementMode",
    "EnforcementSupport",
    "ExpandControlsEnum",
    "ExpandEnum",
    "ExternalSecuritySolutionKindEnum",
    "FileType",
    "ImplementationEffort",
    "ProtocolEnum",
    "ProvisioningState",
    "RecommendationAction",
    "RecommendationStatus",
    "RecommendationType",
    "SecurityFamily",
    "ServerVulnerabilityAssessmentPropertiesProvisioningState",
    "Severity",
    "Source",
    "SourceSystem",
    "Status",
    "StatusReason",
    "Threats",
    "TransportProtocol",
    "UserImpact",
]
__all__.extend([p for p in _patch_all if p not in __all__])
_patch_sdk()
