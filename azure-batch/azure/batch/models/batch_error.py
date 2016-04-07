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

from msrest.serialization import Model
from msrest.exceptions import HttpOperationError


class BatchError(Model):
    """
    An error response received from the Azure Batch service.

    :param code: Gets or sets an identifier for the error. Codes are
     invariant and are intended to be consumed programmatically.
    :type code: str
    :param message: Gets or sets a message describing the error, intended to
     be suitable for display in a user interface.
    :type message: :class:`ErrorMessage <azure.batch.models.ErrorMessage>`
    :param values: Gets or sets a collection of key-value pairs containing
     additional details about the error.
    :type values: list of :class:`BatchErrorDetail
     <azure.batch.models.BatchErrorDetail>`
    """ 

    _attribute_map = {
        'code': {'key': 'code', 'type': 'str'},
        'message': {'key': 'message', 'type': 'ErrorMessage'},
        'values': {'key': 'values', 'type': '[BatchErrorDetail]'},
    }

    def __init__(self, code=None, message=None, values=None):
        self.code = code
        self.message = message
        self.values = values


class BatchErrorException(HttpOperationError):
    """Server responsed with exception of type: 'BatchError'.

    :param deserialize: A deserializer
    :param response: Server response to be deserialized.
    """

    def __init__(self, deserialize, response, *args):

        super(BatchErrorException, self).__init__(deserialize, response, 'BatchError', *args)
