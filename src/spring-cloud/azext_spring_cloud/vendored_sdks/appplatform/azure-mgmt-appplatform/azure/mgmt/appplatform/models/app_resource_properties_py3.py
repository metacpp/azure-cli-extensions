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


class AppResourceProperties(Model):
    """App resource properties payload.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :param public: Indicates whether the App exposes public endpoint
    :type public: bool
    :ivar url: URL of the App
    :vartype url: str
    :ivar provisioning_state: Provisioning state of the App. Possible values
     include: 'Succeeded', 'Failed', 'Creating', 'Updating'
    :vartype provisioning_state: str or
     ~azure.mgmt.appplatform.models.AppResourceProvisioningState
    :param active_deployment_name: Name of the active deployment of the App
    :type active_deployment_name: str
    :ivar created_time: Date time when the resource is created
    :vartype created_time: datetime
    :param temporary_disk: Temporary disk settings
    :type temporary_disk: ~azure.mgmt.appplatform.models.TemporaryDisk
    :param persistent_disk: Persistent disk settings
    :type persistent_disk: ~azure.mgmt.appplatform.models.PersistentDisk
    """

    _validation = {
        'url': {'readonly': True},
        'provisioning_state': {'readonly': True},
        'created_time': {'readonly': True},
    }

    _attribute_map = {
        'public': {'key': 'public', 'type': 'bool'},
        'url': {'key': 'url', 'type': 'str'},
        'provisioning_state': {'key': 'provisioningState', 'type': 'str'},
        'active_deployment_name': {'key': 'activeDeploymentName', 'type': 'str'},
        'created_time': {'key': 'createdTime', 'type': 'iso-8601'},
        'temporary_disk': {'key': 'temporaryDisk', 'type': 'TemporaryDisk'},
        'persistent_disk': {'key': 'persistentDisk', 'type': 'PersistentDisk'},
    }

    def __init__(self, *, public: bool=None, active_deployment_name: str=None, temporary_disk=None, persistent_disk=None, **kwargs) -> None:
        super(AppResourceProperties, self).__init__(**kwargs)
        self.public = public
        self.url = None
        self.provisioning_state = None
        self.active_deployment_name = active_deployment_name
        self.created_time = None
        self.temporary_disk = temporary_disk
        self.persistent_disk = persistent_disk
