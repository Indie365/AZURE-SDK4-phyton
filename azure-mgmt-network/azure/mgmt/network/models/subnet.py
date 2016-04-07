# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft and contributors.  All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .sub_resource import SubResource


class Subnet(SubResource):
    """
    Subnet in a VirtualNework resource

    :param id: Resource Id
    :type id: str
    :param address_prefix: Gets or sets Address prefix for the subnet.
    :type address_prefix: str
    :param network_security_group: Gets or sets the reference of the
     NetworkSecurityGroup resource
    :type network_security_group: :class:`NetworkSecurityGroup
     <azure.mgmt.network.models.NetworkSecurityGroup>`
    :param route_table: Gets or sets the reference of the RouteTable resource
    :type route_table: :class:`RouteTable
     <azure.mgmt.network.models.RouteTable>`
    :param ip_configurations: Gets array of references to the network
     interface IP configurations using subnet
    :type ip_configurations: list of :class:`IPConfiguration
     <azure.mgmt.network.models.IPConfiguration>`
    :param provisioning_state: Gets or sets Provisioning state of the
     PublicIP resource Updating/Deleting/Failed
    :type provisioning_state: str
    :param name: Gets name of the resource that is unique within a resource
     group. This name can be used to access the resource
    :type name: str
    :param etag: A unique read-only string that changes whenever the resource
     is updated
    :type etag: str
    """ 

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'address_prefix': {'key': 'properties.addressPrefix', 'type': 'str'},
        'network_security_group': {'key': 'properties.networkSecurityGroup', 'type': 'NetworkSecurityGroup'},
        'route_table': {'key': 'properties.routeTable', 'type': 'RouteTable'},
        'ip_configurations': {'key': 'properties.ipConfigurations', 'type': '[IPConfiguration]'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'etag': {'key': 'etag', 'type': 'str'},
    }

    def __init__(self, id=None, address_prefix=None, network_security_group=None, route_table=None, ip_configurations=None, provisioning_state=None, name=None, etag=None):
        super(Subnet, self).__init__(id=id)
        self.address_prefix = address_prefix
        self.network_security_group = network_security_group
        self.route_table = route_table
        self.ip_configurations = ip_configurations
        self.provisioning_state = provisioning_state
        self.name = name
        self.etag = etag
