# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from enum import Enum
from azure.core import CaseInsensitiveEnumMeta


class AccessControlEntryAction(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Action object."""

    PERMIT = "Permit"
    DENY = "Deny"


class AppServicePlanRestrictions(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """App Service plans this offer is restricted to."""

    NONE = "None"
    FREE = "Free"
    SHARED = "Shared"
    BASIC = "Basic"
    STANDARD = "Standard"
    PREMIUM = "Premium"


class AutoHealActionType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Predefined action to be taken."""

    RECYCLE = "Recycle"
    LOG_EVENT = "LogEvent"
    CUSTOM_ACTION = "CustomAction"


class AzureResourceType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Type of the Azure resource the hostname is assigned to."""

    WEBSITE = "Website"
    TRAFFIC_MANAGER = "TrafficManager"


class AzureStorageState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """State of the storage account."""

    OK = "Ok"
    INVALID_CREDENTIALS = "InvalidCredentials"
    INVALID_SHARE = "InvalidShare"


class AzureStorageType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Type of storage."""

    AZURE_FILES = "AzureFiles"
    AZURE_BLOB = "AzureBlob"


class BackupItemStatus(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Backup status."""

    IN_PROGRESS = "InProgress"
    FAILED = "Failed"
    SUCCEEDED = "Succeeded"
    TIMED_OUT = "TimedOut"
    CREATED = "Created"
    SKIPPED = "Skipped"
    PARTIALLY_SUCCEEDED = "PartiallySucceeded"
    DELETE_IN_PROGRESS = "DeleteInProgress"
    DELETE_FAILED = "DeleteFailed"
    DELETED = "Deleted"


class BackupRestoreOperationType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Operation type."""

    DEFAULT = "Default"
    CLONE = "Clone"
    RELOCATION = "Relocation"
    SNAPSHOT = "Snapshot"
    CLOUD_FS = "CloudFS"


class BuiltInAuthenticationProvider(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The default authentication provider to use when multiple providers are configured.
    This setting is only needed if multiple providers are configured and the unauthenticated client
    action is set to "RedirectToLoginPage".
    """

    AZURE_ACTIVE_DIRECTORY = "AzureActiveDirectory"
    FACEBOOK = "Facebook"
    GOOGLE = "Google"
    MICROSOFT_ACCOUNT = "MicrosoftAccount"
    TWITTER = "Twitter"


class CertificateOrderActionType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Action type."""

    CERTIFICATE_ISSUED = "CertificateIssued"
    CERTIFICATE_ORDER_CANCELED = "CertificateOrderCanceled"
    CERTIFICATE_ORDER_CREATED = "CertificateOrderCreated"
    CERTIFICATE_REVOKED = "CertificateRevoked"
    DOMAIN_VALIDATION_COMPLETE = "DomainValidationComplete"
    FRAUD_DETECTED = "FraudDetected"
    ORG_NAME_CHANGE = "OrgNameChange"
    ORG_VALIDATION_COMPLETE = "OrgValidationComplete"
    SAN_DROP = "SanDrop"
    FRAUD_CLEARED = "FraudCleared"
    CERTIFICATE_EXPIRED = "CertificateExpired"
    CERTIFICATE_EXPIRATION_WARNING = "CertificateExpirationWarning"
    FRAUD_DOCUMENTATION_REQUIRED = "FraudDocumentationRequired"
    UNKNOWN = "Unknown"


class CertificateOrderStatus(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Current order status."""

    PENDINGISSUANCE = "Pendingissuance"
    ISSUED = "Issued"
    REVOKED = "Revoked"
    CANCELED = "Canceled"
    DENIED = "Denied"
    PENDINGREVOCATION = "Pendingrevocation"
    PENDING_REKEY = "PendingRekey"
    UNUSED = "Unused"
    EXPIRED = "Expired"
    NOT_SUBMITTED = "NotSubmitted"


class CertificateProductType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Certificate product type."""

    STANDARD_DOMAIN_VALIDATED_SSL = "StandardDomainValidatedSsl"
    STANDARD_DOMAIN_VALIDATED_WILD_CARD_SSL = "StandardDomainValidatedWildCardSsl"


class Channels(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """List of channels that this recommendation can apply."""

    NOTIFICATION = "Notification"
    API = "Api"
    EMAIL = "Email"
    WEBHOOK = "Webhook"
    ALL = "All"


class CheckNameResourceTypes(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Resource type used for verification."""

    SITE = "Site"
    SLOT = "Slot"
    HOSTING_ENVIRONMENT = "HostingEnvironment"
    PUBLISHING_USER = "PublishingUser"
    MICROSOFT_WEB_SITES = "Microsoft.Web/sites"
    MICROSOFT_WEB_SITES_SLOTS = "Microsoft.Web/sites/slots"
    MICROSOFT_WEB_HOSTING_ENVIRONMENTS = "Microsoft.Web/hostingEnvironments"
    MICROSOFT_WEB_PUBLISHING_USERS = "Microsoft.Web/publishingUsers"


class CloneAbilityResult(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Name of app."""

    CLONEABLE = "Cloneable"
    PARTIALLY_CLONEABLE = "PartiallyCloneable"
    NOT_CLONEABLE = "NotCloneable"


class ComputeModeOptions(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Shared/dedicated workers."""

    SHARED = "Shared"
    DEDICATED = "Dedicated"
    DYNAMIC = "Dynamic"


class ConnectionStringType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Type of database."""

    MY_SQL = "MySql"
    SQL_SERVER = "SQLServer"
    SQL_AZURE = "SQLAzure"
    CUSTOM = "Custom"
    NOTIFICATION_HUB = "NotificationHub"
    SERVICE_BUS = "ServiceBus"
    EVENT_HUB = "EventHub"
    API_HUB = "ApiHub"
    DOC_DB = "DocDb"
    REDIS_CACHE = "RedisCache"
    POSTGRE_SQL = "PostgreSQL"


class ContinuousWebJobStatus(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Job status."""

    INITIALIZING = "Initializing"
    STARTING = "Starting"
    RUNNING = "Running"
    PENDING_RESTART = "PendingRestart"
    STOPPED = "Stopped"


class CustomHostNameDnsRecordType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Type of the DNS record."""

    C_NAME = "CName"
    A = "A"


class DatabaseType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Database type (e.g. SqlAzure / MySql)."""

    SQL_AZURE = "SqlAzure"
    MY_SQL = "MySql"
    LOCAL_MY_SQL = "LocalMySql"
    POSTGRE_SQL = "PostgreSql"


class DnsType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Current DNS type."""

    AZURE_DNS = "AzureDns"
    DEFAULT_DOMAIN_REGISTRAR_DNS = "DefaultDomainRegistrarDns"


class DnsVerificationTestResult(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """DNS verification test result."""

    PASSED = "Passed"
    FAILED = "Failed"
    SKIPPED = "Skipped"


class DomainPatchResourcePropertiesDomainNotRenewableReasonsItem(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """DomainPatchResourcePropertiesDomainNotRenewableReasonsItem."""

    REGISTRATION_STATUS_NOT_SUPPORTED_FOR_RENEWAL = "RegistrationStatusNotSupportedForRenewal"
    EXPIRATION_NOT_IN_RENEWAL_TIME_RANGE = "ExpirationNotInRenewalTimeRange"
    SUBSCRIPTION_NOT_ACTIVE = "SubscriptionNotActive"


class DomainPropertiesDomainNotRenewableReasonsItem(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """DomainPropertiesDomainNotRenewableReasonsItem."""

    REGISTRATION_STATUS_NOT_SUPPORTED_FOR_RENEWAL = "RegistrationStatusNotSupportedForRenewal"
    EXPIRATION_NOT_IN_RENEWAL_TIME_RANGE = "ExpirationNotInRenewalTimeRange"
    SUBSCRIPTION_NOT_ACTIVE = "SubscriptionNotActive"


class DomainStatus(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Domain registration status."""

    ACTIVE = "Active"
    AWAITING = "Awaiting"
    CANCELLED = "Cancelled"
    CONFISCATED = "Confiscated"
    DISABLED = "Disabled"
    EXCLUDED = "Excluded"
    EXPIRED = "Expired"
    FAILED = "Failed"
    HELD = "Held"
    LOCKED = "Locked"
    PARKED = "Parked"
    PENDING = "Pending"
    RESERVED = "Reserved"
    REVERTED = "Reverted"
    SUSPENDED = "Suspended"
    TRANSFERRED = "Transferred"
    UNKNOWN = "Unknown"
    UNLOCKED = "Unlocked"
    UNPARKED = "Unparked"
    UPDATED = "Updated"
    JSON_CONVERTER_FAILED = "JsonConverterFailed"


class DomainType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Valid values are Regular domain: Azure will charge the full price of domain registration,
    SoftDeleted: Purchasing this domain will simply restore it and this operation will not cost
    anything.
    """

    REGULAR = "Regular"
    SOFT_DELETED = "SoftDeleted"


class Enum3(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Enum3."""

    WINDOWS = "Windows"
    LINUX = "Linux"
    WINDOWS_FUNCTIONS = "WindowsFunctions"
    LINUX_FUNCTIONS = "LinuxFunctions"


class Enum4(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Enum4."""

    WINDOWS = "Windows"
    LINUX = "Linux"
    WINDOWS_FUNCTIONS = "WindowsFunctions"
    LINUX_FUNCTIONS = "LinuxFunctions"


class FrequencyUnit(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The unit of time for how often the backup should be executed (e.g. for weekly backup, this
    should be set to Day and FrequencyInterval should be set to 7).
    """

    DAY = "Day"
    HOUR = "Hour"


class FtpsState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """State of FTP / FTPS service."""

    ALL_ALLOWED = "AllAllowed"
    FTPS_ONLY = "FtpsOnly"
    DISABLED = "Disabled"


class HostingEnvironmentStatus(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Current status of the App Service Environment."""

    PREPARING = "Preparing"
    READY = "Ready"
    SCALING = "Scaling"
    DELETING = "Deleting"


class HostNameType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Type of the hostname."""

    VERIFIED = "Verified"
    MANAGED = "Managed"


class HostType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Indicates whether the hostname is a standard or repository hostname."""

    STANDARD = "Standard"
    REPOSITORY = "Repository"


class InAvailabilityReasonType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """:code:`<code>Invalid</code>` indicates the name provided does not match Azure App Service
    naming requirements. :code:`<code>AlreadyExists</code>` indicates that the name is already in
    use and is therefore unavailable.
    """

    INVALID = "Invalid"
    ALREADY_EXISTS = "AlreadyExists"


class InternalLoadBalancingMode(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Specifies which endpoints to serve internally in the Virtual Network for the App Service
    Environment.
    """

    NONE = "None"
    WEB = "Web"
    PUBLISHING = "Publishing"


class IpFilterTag(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Defines what this IP filter will be used for. This is to support IP filtering on proxies."""

    DEFAULT = "Default"
    XFF_PROXY = "XffProxy"


class IssueType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Represents the type of the Detector."""

    SERVICE_INCIDENT = "ServiceIncident"
    APP_DEPLOYMENT = "AppDeployment"
    APP_CRASH = "AppCrash"
    RUNTIME_ISSUE_DETECTED = "RuntimeIssueDetected"
    ASE_DEPLOYMENT = "AseDeployment"
    USER_ISSUE = "UserIssue"
    PLATFORM_ISSUE = "PlatformIssue"
    OTHER = "Other"


class KeyVaultSecretStatus(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Status of the Key Vault secret."""

    INITIALIZED = "Initialized"
    WAITING_ON_CERTIFICATE_ORDER = "WaitingOnCertificateOrder"
    SUCCEEDED = "Succeeded"
    CERTIFICATE_ORDER_FAILED = "CertificateOrderFailed"
    OPERATION_NOT_PERMITTED_ON_KEY_VAULT = "OperationNotPermittedOnKeyVault"
    AZURE_SERVICE_UNAUTHORIZED_TO_ACCESS_KEY_VAULT = "AzureServiceUnauthorizedToAccessKeyVault"
    KEY_VAULT_DOES_NOT_EXIST = "KeyVaultDoesNotExist"
    KEY_VAULT_SECRET_DOES_NOT_EXIST = "KeyVaultSecretDoesNotExist"
    UNKNOWN_ERROR = "UnknownError"
    EXTERNAL_PRIVATE_KEY = "ExternalPrivateKey"
    UNKNOWN = "Unknown"


class LogLevel(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Log level."""

    OFF = "Off"
    VERBOSE = "Verbose"
    INFORMATION = "Information"
    WARNING = "Warning"
    ERROR = "Error"


class ManagedPipelineMode(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Managed pipeline mode."""

    INTEGRATED = "Integrated"
    CLASSIC = "Classic"


class ManagedServiceIdentityType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Type of managed service identity."""

    SYSTEM_ASSIGNED = "SystemAssigned"
    USER_ASSIGNED = "UserAssigned"
    SYSTEM_ASSIGNED_USER_ASSIGNED = "SystemAssigned, UserAssigned"
    NONE = "None"


class MSDeployLogEntryType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Log entry type."""

    MESSAGE = "Message"
    WARNING = "Warning"
    ERROR = "Error"


class MSDeployProvisioningState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Provisioning state."""

    ACCEPTED = "accepted"
    RUNNING = "running"
    SUCCEEDED = "succeeded"
    FAILED = "failed"
    CANCELED = "canceled"


class MySqlMigrationType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The type of migration operation to be done."""

    LOCAL_TO_REMOTE = "LocalToRemote"
    REMOTE_TO_LOCAL = "RemoteToLocal"


class NotificationLevel(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Level indicating how critical this recommendation can impact."""

    CRITICAL = "Critical"
    WARNING = "Warning"
    INFORMATION = "Information"
    NON_URGENT_SUGGESTION = "NonUrgentSuggestion"


class OperationStatus(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The current status of the operation."""

    IN_PROGRESS = "InProgress"
    FAILED = "Failed"
    SUCCEEDED = "Succeeded"
    TIMED_OUT = "TimedOut"
    CREATED = "Created"


class ProvisioningState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Status of certificate order."""

    SUCCEEDED = "Succeeded"
    FAILED = "Failed"
    CANCELED = "Canceled"
    IN_PROGRESS = "InProgress"
    DELETING = "Deleting"


class PublicCertificateLocation(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Public Certificate Location."""

    CURRENT_USER_MY = "CurrentUserMy"
    LOCAL_MACHINE_MY = "LocalMachineMy"
    UNKNOWN = "Unknown"


class PublishingProfileFormat(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Name of the format. Valid values are:
    FileZilla3
    WebDeploy -- default
    Ftp.
    """

    FILE_ZILLA3 = "FileZilla3"
    WEB_DEPLOY = "WebDeploy"
    FTP = "Ftp"


class RedundancyMode(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Site redundancy mode."""

    NONE = "None"
    MANUAL = "Manual"
    FAILOVER = "Failover"
    ACTIVE_ACTIVE = "ActiveActive"
    GEO_REDUNDANT = "GeoRedundant"


class RenderingType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Rendering Type."""

    NO_GRAPH = "NoGraph"
    TABLE = "Table"
    TIME_SERIES = "TimeSeries"
    TIME_SERIES_PER_INSTANCE = "TimeSeriesPerInstance"


class ResourceNotRenewableReason(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """ResourceNotRenewableReason."""

    REGISTRATION_STATUS_NOT_SUPPORTED_FOR_RENEWAL = "RegistrationStatusNotSupportedForRenewal"
    EXPIRATION_NOT_IN_RENEWAL_TIME_RANGE = "ExpirationNotInRenewalTimeRange"
    SUBSCRIPTION_NOT_ACTIVE = "SubscriptionNotActive"


class ResourceScopeType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Name of a resource type this recommendation applies, e.g. Subscription, ServerFarm, Site."""

    SERVER_FARM = "ServerFarm"
    SUBSCRIPTION = "Subscription"
    WEB_SITE = "WebSite"


class RouteType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The type of route this is:
    DEFAULT - By default, every app has routes to the local address ranges specified by RFC1918
    INHERITED - Routes inherited from the real Virtual Network routes
    STATIC - Static route set on the app only

    These values will be used for syncing an app's routes with those from a Virtual Network.
    """

    DEFAULT = "DEFAULT"
    INHERITED = "INHERITED"
    STATIC = "STATIC"


class ScmType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """SCM type."""

    NONE = "None"
    DROPBOX = "Dropbox"
    TFS = "Tfs"
    LOCAL_GIT = "LocalGit"
    GIT_HUB = "GitHub"
    CODE_PLEX_GIT = "CodePlexGit"
    CODE_PLEX_HG = "CodePlexHg"
    BITBUCKET_GIT = "BitbucketGit"
    BITBUCKET_HG = "BitbucketHg"
    EXTERNAL_GIT = "ExternalGit"
    EXTERNAL_HG = "ExternalHg"
    ONE_DRIVE = "OneDrive"
    VSO = "VSO"


class SiteAvailabilityState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Management information availability state for the app."""

    NORMAL = "Normal"
    LIMITED = "Limited"
    DISASTER_RECOVERY_MODE = "DisasterRecoveryMode"


class SiteExtensionType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Site extension type."""

    GALLERY = "Gallery"
    WEB_ROOT = "WebRoot"


class SiteLoadBalancing(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Site load balancing."""

    WEIGHTED_ROUND_ROBIN = "WeightedRoundRobin"
    LEAST_REQUESTS = "LeastRequests"
    LEAST_RESPONSE_TIME = "LeastResponseTime"
    WEIGHTED_TOTAL_TRAFFIC = "WeightedTotalTraffic"
    REQUEST_HASH = "RequestHash"


class SkuName(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """SkuName."""

    FREE = "Free"
    SHARED = "Shared"
    BASIC = "Basic"
    STANDARD = "Standard"
    PREMIUM = "Premium"
    DYNAMIC = "Dynamic"
    ISOLATED = "Isolated"
    PREMIUM_V2 = "PremiumV2"
    ELASTIC_PREMIUM = "ElasticPremium"
    ELASTIC_ISOLATED = "ElasticIsolated"


class SolutionType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Type of Solution."""

    QUICK_SOLUTION = "QuickSolution"
    DEEP_INVESTIGATION = "DeepInvestigation"
    BEST_PRACTICES = "BestPractices"


class SslState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """SSL type."""

    DISABLED = "Disabled"
    SNI_ENABLED = "SniEnabled"
    IP_BASED_ENABLED = "IpBasedEnabled"


class StatusOptions(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """App Service plan status."""

    READY = "Ready"
    PENDING = "Pending"
    CREATING = "Creating"


class SupportedTlsVersions(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """MinTlsVersion: configures the minimum version of TLS required for SSL requests."""

    ONE0 = "1.0"
    ONE1 = "1.1"
    ONE2 = "1.2"


class TriggeredWebJobStatus(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Job status."""

    SUCCESS = "Success"
    FAILED = "Failed"
    ERROR = "Error"


class UnauthenticatedClientAction(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The action to take when an unauthenticated client attempts to access the app."""

    REDIRECT_TO_LOGIN_PAGE = "RedirectToLoginPage"
    ALLOW_ANONYMOUS = "AllowAnonymous"


class UsageState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """State indicating whether the app has exceeded its quota usage. Read-only."""

    NORMAL = "Normal"
    EXCEEDED = "Exceeded"


class ValidateResourceTypes(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Resource type used for verification."""

    SERVER_FARM = "ServerFarm"
    SITE = "Site"


class WebJobType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Job type."""

    CONTINUOUS = "Continuous"
    TRIGGERED = "Triggered"


class WorkerSizeOptions(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Size of the machines."""

    SMALL = "Small"
    MEDIUM = "Medium"
    LARGE = "Large"
    D1 = "D1"
    D2 = "D2"
    D3 = "D3"
    DEFAULT = "Default"
