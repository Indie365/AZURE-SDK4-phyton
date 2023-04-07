# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.identity import DefaultAzureCredential
from azure.mgmt.mobilenetwork import MobileNetworkManagementClient

"""
# PREREQUISITES
    pip install azure-identity
    pip install azure-mgmt-mobilenetwork
# USAGE
    python sim_bulk_upload_encrypted.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = MobileNetworkManagementClient(
        credential=DefaultAzureCredential(),
        subscription_id="subid",
    )

    response = client.sims.begin_bulk_upload_encrypted(
        resource_group_name="rg1",
        sim_group_name="testSimGroup",
        parameters={
            "azureKeyIdentifier": 1,
            "encryptedTransportKey": "ABC123",
            "signedTransportKey": "ABC123",
            "sims": [
                {
                    "name": "testSim",
                    "properties": {
                        "deviceType": "Video camera",
                        "encryptedCredentials": "ABC123",
                        "integratedCircuitCardIdentifier": "8900000000000000000",
                        "internationalMobileSubscriberIdentity": "00000",
                        "simPolicy": {
                            "id": "/subscriptions/subid/resourceGroups/rg1/providers/Microsoft.MobileNetwork/mobileNetworks/testMobileNetwork/simPolicies/MySimPolicy"
                        },
                        "staticIpConfiguration": [
                            {
                                "attachedDataNetwork": {
                                    "id": "/subscriptions/subid/resourceGroups/rg1/providers/Microsoft.MobileNetwork/packetCoreControlPlanes/TestPacketCoreCP/packetCoreDataPlanes/TestPacketCoreDP/attachedDataNetworks/TestAttachedDataNetwork"
                                },
                                "slice": {
                                    "id": "/subscriptions/subid/resourceGroups/rg1/providers/Microsoft.MobileNetwork/mobileNetworks/testMobileNetwork/slices/testSlice"
                                },
                                "staticIp": {"ipv4Address": "2.4.0.1"},
                            }
                        ],
                    },
                },
                {
                    "name": "testSim2",
                    "properties": {
                        "deviceType": "Video camera",
                        "encryptedCredentials": "ABC123",
                        "integratedCircuitCardIdentifier": "8900000000000000001",
                        "internationalMobileSubscriberIdentity": "00000",
                        "simPolicy": {
                            "id": "/subscriptions/subid/resourceGroups/rg1/providers/Microsoft.MobileNetwork/mobileNetworks/testMobileNetwork/simPolicies/MySimPolicy"
                        },
                        "staticIpConfiguration": [
                            {
                                "attachedDataNetwork": {
                                    "id": "/subscriptions/subid/resourceGroups/rg1/providers/Microsoft.MobileNetwork/packetCoreControlPlanes/TestPacketCoreCP/packetCoreDataPlanes/TestPacketCoreDP/attachedDataNetworks/TestAttachedDataNetwork"
                                },
                                "slice": {
                                    "id": "/subscriptions/subid/resourceGroups/rg1/providers/Microsoft.MobileNetwork/mobileNetworks/testMobileNetwork/slices/testSlice"
                                },
                                "staticIp": {"ipv4Address": "2.4.0.2"},
                            }
                        ],
                    },
                },
            ],
            "vendorKeyFingerprint": "ABC123",
            "version": 1,
        },
    ).result()
    print(response)


# x-ms-original-file: specification/mobilenetwork/resource-manager/Microsoft.MobileNetwork/stable/2022-11-01/examples/SimBulkUploadEncrypted.json
if __name__ == "__main__":
    main()
