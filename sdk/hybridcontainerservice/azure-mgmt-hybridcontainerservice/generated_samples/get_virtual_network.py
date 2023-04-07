# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.identity import DefaultAzureCredential
from azure.mgmt.hybridcontainerservice import HybridContainerServiceMgmtClient

"""
# PREREQUISITES
    pip install azure-identity
    pip install azure-mgmt-hybridcontainerservice
# USAGE
    python get_virtual_network.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = HybridContainerServiceMgmtClient(
        credential=DefaultAzureCredential(),
        subscription_id="a3e42606-29b1-4d7d-b1d9-9ff6b9d3c71b",
    )

    response = client.virtual_networks.retrieve(
        resource_group_name="test-arcappliance-resgrp",
        virtual_networks_name="test-vnet-static",
    )
    print(response)


# x-ms-original-file: specification/hybridaks/resource-manager/Microsoft.HybridContainerService/preview/2022-09-01-preview/examples/GetVirtualNetwork.json
if __name__ == "__main__":
    main()
