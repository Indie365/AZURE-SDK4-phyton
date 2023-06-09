# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .linked_service_py3 import LinkedService


class HDInsightOnDemandLinkedService(LinkedService):
    """HDInsight ondemand linked service.

    All required parameters must be populated in order to send to Azure.

    :param additional_properties: Unmatched properties from the message are
     deserialized this collection
    :type additional_properties: dict[str, object]
    :param connect_via: The integration runtime reference.
    :type connect_via:
     ~azure.mgmt.datafactory.models.IntegrationRuntimeReference
    :param description: Linked service description.
    :type description: str
    :param parameters: Parameters for linked service.
    :type parameters: dict[str,
     ~azure.mgmt.datafactory.models.ParameterSpecification]
    :param annotations: List of tags that can be used for describing the
     linked service.
    :type annotations: list[object]
    :param type: Required. Constant filled by server.
    :type type: str
    :param cluster_size: Required. Number of worker/data nodes in the cluster.
     Suggestion value: 4. Type: string (or Expression with resultType string).
    :type cluster_size: object
    :param time_to_live: Required. The allowed idle time for the on-demand
     HDInsight cluster. Specifies how long the on-demand HDInsight cluster
     stays alive after completion of an activity run if there are no other
     active jobs in the cluster. The minimum value is 5 mins. Type: string (or
     Expression with resultType string).
    :type time_to_live: object
    :param version: Required. Version of the HDInsight cluster.  Type: string
     (or Expression with resultType string).
    :type version: object
    :param linked_service_name: Required. Azure Storage linked service to be
     used by the on-demand cluster for storing and processing data.
    :type linked_service_name:
     ~azure.mgmt.datafactory.models.LinkedServiceReference
    :param host_subscription_id: Required. The customer’s subscription to host
     the cluster. Type: string (or Expression with resultType string).
    :type host_subscription_id: object
    :param service_principal_id: The service principal id for the
     hostSubscriptionId. Type: string (or Expression with resultType string).
    :type service_principal_id: object
    :param service_principal_key: The key for the service principal id.
    :type service_principal_key: ~azure.mgmt.datafactory.models.SecretBase
    :param tenant: Required. The Tenant id/name to which the service principal
     belongs. Type: string (or Expression with resultType string).
    :type tenant: object
    :param cluster_resource_group: Required. The resource group where the
     cluster belongs. Type: string (or Expression with resultType string).
    :type cluster_resource_group: object
    :param cluster_name_prefix: The prefix of cluster name, postfix will be
     distinct with timestamp. Type: string (or Expression with resultType
     string).
    :type cluster_name_prefix: object
    :param cluster_user_name: The username to access the cluster. Type: string
     (or Expression with resultType string).
    :type cluster_user_name: object
    :param cluster_password: The password to access the cluster.
    :type cluster_password: ~azure.mgmt.datafactory.models.SecretBase
    :param cluster_ssh_user_name: The username to SSH remotely connect to
     cluster’s node (for Linux). Type: string (or Expression with resultType
     string).
    :type cluster_ssh_user_name: object
    :param cluster_ssh_password: The password to SSH remotely connect
     cluster’s node (for Linux).
    :type cluster_ssh_password: ~azure.mgmt.datafactory.models.SecretBase
    :param additional_linked_service_names: Specifies additional storage
     accounts for the HDInsight linked service so that the Data Factory service
     can register them on your behalf.
    :type additional_linked_service_names:
     list[~azure.mgmt.datafactory.models.LinkedServiceReference]
    :param hcatalog_linked_service_name: The name of Azure SQL linked service
     that point to the HCatalog database. The on-demand HDInsight cluster is
     created by using the Azure SQL database as the metastore.
    :type hcatalog_linked_service_name:
     ~azure.mgmt.datafactory.models.LinkedServiceReference
    :param cluster_type: The cluster type. Type: string (or Expression with
     resultType string).
    :type cluster_type: object
    :param spark_version: The version of spark if the cluster type is 'spark'.
     Type: string (or Expression with resultType string).
    :type spark_version: object
    :param core_configuration: Specifies the core configuration parameters (as
     in core-site.xml) for the HDInsight cluster to be created.
    :type core_configuration: object
    :param h_base_configuration: Specifies the HBase configuration parameters
     (hbase-site.xml) for the HDInsight cluster.
    :type h_base_configuration: object
    :param hdfs_configuration: Specifies the HDFS configuration parameters
     (hdfs-site.xml) for the HDInsight cluster.
    :type hdfs_configuration: object
    :param hive_configuration: Specifies the hive configuration parameters
     (hive-site.xml) for the HDInsight cluster.
    :type hive_configuration: object
    :param map_reduce_configuration: Specifies the MapReduce configuration
     parameters (mapred-site.xml) for the HDInsight cluster.
    :type map_reduce_configuration: object
    :param oozie_configuration: Specifies the Oozie configuration parameters
     (oozie-site.xml) for the HDInsight cluster.
    :type oozie_configuration: object
    :param storm_configuration: Specifies the Storm configuration parameters
     (storm-site.xml) for the HDInsight cluster.
    :type storm_configuration: object
    :param yarn_configuration: Specifies the Yarn configuration parameters
     (yarn-site.xml) for the HDInsight cluster.
    :type yarn_configuration: object
    :param encrypted_credential: The encrypted credential used for
     authentication. Credentials are encrypted using the integration runtime
     credential manager. Type: string (or Expression with resultType string).
    :type encrypted_credential: object
    :param head_node_size: Specifies the size of the head node for the
     HDInsight cluster.
    :type head_node_size: object
    :param data_node_size: Specifies the size of the data node for the
     HDInsight cluster.
    :type data_node_size: object
    :param zookeeper_node_size: Specifies the size of the Zoo Keeper node for
     the HDInsight cluster.
    :type zookeeper_node_size: object
    :param script_actions: Custom script actions to run on HDI ondemand
     cluster once it's up. Please refer to
     https://docs.microsoft.com/en-us/azure/hdinsight/hdinsight-hadoop-customize-cluster-linux?toc=%2Fen-us%2Fazure%2Fhdinsight%2Fr-server%2FTOC.json&bc=%2Fen-us%2Fazure%2Fbread%2Ftoc.json#understanding-script-actions.
    :type script_actions: list[~azure.mgmt.datafactory.models.ScriptAction]
    :param virtual_network_id: The ARM resource ID for the vNet to which the
     cluster should be joined after creation. Type: string (or Expression with
     resultType string).
    :type virtual_network_id: object
    :param subnet_name: The ARM resource ID for the subnet in the vNet. If
     virtualNetworkId was specified, then this property is required. Type:
     string (or Expression with resultType string).
    :type subnet_name: object
    """

    _validation = {
        'type': {'required': True},
        'cluster_size': {'required': True},
        'time_to_live': {'required': True},
        'version': {'required': True},
        'linked_service_name': {'required': True},
        'host_subscription_id': {'required': True},
        'tenant': {'required': True},
        'cluster_resource_group': {'required': True},
    }

    _attribute_map = {
        'additional_properties': {'key': '', 'type': '{object}'},
        'connect_via': {'key': 'connectVia', 'type': 'IntegrationRuntimeReference'},
        'description': {'key': 'description', 'type': 'str'},
        'parameters': {'key': 'parameters', 'type': '{ParameterSpecification}'},
        'annotations': {'key': 'annotations', 'type': '[object]'},
        'type': {'key': 'type', 'type': 'str'},
        'cluster_size': {'key': 'typeProperties.clusterSize', 'type': 'object'},
        'time_to_live': {'key': 'typeProperties.timeToLive', 'type': 'object'},
        'version': {'key': 'typeProperties.version', 'type': 'object'},
        'linked_service_name': {'key': 'typeProperties.linkedServiceName', 'type': 'LinkedServiceReference'},
        'host_subscription_id': {'key': 'typeProperties.hostSubscriptionId', 'type': 'object'},
        'service_principal_id': {'key': 'typeProperties.servicePrincipalId', 'type': 'object'},
        'service_principal_key': {'key': 'typeProperties.servicePrincipalKey', 'type': 'SecretBase'},
        'tenant': {'key': 'typeProperties.tenant', 'type': 'object'},
        'cluster_resource_group': {'key': 'typeProperties.clusterResourceGroup', 'type': 'object'},
        'cluster_name_prefix': {'key': 'typeProperties.clusterNamePrefix', 'type': 'object'},
        'cluster_user_name': {'key': 'typeProperties.clusterUserName', 'type': 'object'},
        'cluster_password': {'key': 'typeProperties.clusterPassword', 'type': 'SecretBase'},
        'cluster_ssh_user_name': {'key': 'typeProperties.clusterSshUserName', 'type': 'object'},
        'cluster_ssh_password': {'key': 'typeProperties.clusterSshPassword', 'type': 'SecretBase'},
        'additional_linked_service_names': {'key': 'typeProperties.additionalLinkedServiceNames', 'type': '[LinkedServiceReference]'},
        'hcatalog_linked_service_name': {'key': 'typeProperties.hcatalogLinkedServiceName', 'type': 'LinkedServiceReference'},
        'cluster_type': {'key': 'typeProperties.clusterType', 'type': 'object'},
        'spark_version': {'key': 'typeProperties.sparkVersion', 'type': 'object'},
        'core_configuration': {'key': 'typeProperties.coreConfiguration', 'type': 'object'},
        'h_base_configuration': {'key': 'typeProperties.hBaseConfiguration', 'type': 'object'},
        'hdfs_configuration': {'key': 'typeProperties.hdfsConfiguration', 'type': 'object'},
        'hive_configuration': {'key': 'typeProperties.hiveConfiguration', 'type': 'object'},
        'map_reduce_configuration': {'key': 'typeProperties.mapReduceConfiguration', 'type': 'object'},
        'oozie_configuration': {'key': 'typeProperties.oozieConfiguration', 'type': 'object'},
        'storm_configuration': {'key': 'typeProperties.stormConfiguration', 'type': 'object'},
        'yarn_configuration': {'key': 'typeProperties.yarnConfiguration', 'type': 'object'},
        'encrypted_credential': {'key': 'typeProperties.encryptedCredential', 'type': 'object'},
        'head_node_size': {'key': 'typeProperties.headNodeSize', 'type': 'object'},
        'data_node_size': {'key': 'typeProperties.dataNodeSize', 'type': 'object'},
        'zookeeper_node_size': {'key': 'typeProperties.zookeeperNodeSize', 'type': 'object'},
        'script_actions': {'key': 'typeProperties.scriptActions', 'type': '[ScriptAction]'},
        'virtual_network_id': {'key': 'typeProperties.virtualNetworkId', 'type': 'object'},
        'subnet_name': {'key': 'typeProperties.subnetName', 'type': 'object'},
    }

    def __init__(self, *, cluster_size, time_to_live, version, linked_service_name, host_subscription_id, tenant, cluster_resource_group, additional_properties=None, connect_via=None, description: str=None, parameters=None, annotations=None, service_principal_id=None, service_principal_key=None, cluster_name_prefix=None, cluster_user_name=None, cluster_password=None, cluster_ssh_user_name=None, cluster_ssh_password=None, additional_linked_service_names=None, hcatalog_linked_service_name=None, cluster_type=None, spark_version=None, core_configuration=None, h_base_configuration=None, hdfs_configuration=None, hive_configuration=None, map_reduce_configuration=None, oozie_configuration=None, storm_configuration=None, yarn_configuration=None, encrypted_credential=None, head_node_size=None, data_node_size=None, zookeeper_node_size=None, script_actions=None, virtual_network_id=None, subnet_name=None, **kwargs) -> None:
        super(HDInsightOnDemandLinkedService, self).__init__(additional_properties=additional_properties, connect_via=connect_via, description=description, parameters=parameters, annotations=annotations, **kwargs)
        self.cluster_size = cluster_size
        self.time_to_live = time_to_live
        self.version = version
        self.linked_service_name = linked_service_name
        self.host_subscription_id = host_subscription_id
        self.service_principal_id = service_principal_id
        self.service_principal_key = service_principal_key
        self.tenant = tenant
        self.cluster_resource_group = cluster_resource_group
        self.cluster_name_prefix = cluster_name_prefix
        self.cluster_user_name = cluster_user_name
        self.cluster_password = cluster_password
        self.cluster_ssh_user_name = cluster_ssh_user_name
        self.cluster_ssh_password = cluster_ssh_password
        self.additional_linked_service_names = additional_linked_service_names
        self.hcatalog_linked_service_name = hcatalog_linked_service_name
        self.cluster_type = cluster_type
        self.spark_version = spark_version
        self.core_configuration = core_configuration
        self.h_base_configuration = h_base_configuration
        self.hdfs_configuration = hdfs_configuration
        self.hive_configuration = hive_configuration
        self.map_reduce_configuration = map_reduce_configuration
        self.oozie_configuration = oozie_configuration
        self.storm_configuration = storm_configuration
        self.yarn_configuration = yarn_configuration
        self.encrypted_credential = encrypted_credential
        self.head_node_size = head_node_size
        self.data_node_size = data_node_size
        self.zookeeper_node_size = zookeeper_node_size
        self.script_actions = script_actions
        self.virtual_network_id = virtual_network_id
        self.subnet_name = subnet_name
        self.type = 'HDInsightOnDemand'
