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

from msrest.serialization import Model


class RegenerateTestKeyRequestPayload(Model):
    """Regenerate test key request payload.

    All required parameters must be populated in order to send to Azure.

    :param key_type: Required. Type of the test key. Possible values include:
     'Primary', 'Secondary'
    :type key_type: str or ~azure.mgmt.appplatform.models.TestKeyType
    """

    _validation = {
        'key_type': {'required': True},
    }

    _attribute_map = {
        'key_type': {'key': 'keyType', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(RegenerateTestKeyRequestPayload, self).__init__(**kwargs)
        self.key_type = kwargs.get('key_type', None)
