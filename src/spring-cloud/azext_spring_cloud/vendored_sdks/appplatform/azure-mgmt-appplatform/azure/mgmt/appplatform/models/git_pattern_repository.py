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


class GitPatternRepository(Model):
    """Git repository property payload.

    All required parameters must be populated in order to send to Azure.

    :param name: Required. Name of the repository
    :type name: str
    :param pattern: Collection of pattern of the repository
    :type pattern: list[str]
    :param uri: Required. URI of the repository
    :type uri: str
    :param label: Label of the repository
    :type label: str
    :param search_paths: Searching path of the repository
    :type search_paths: list[str]
    :param username: Username of git repository basic auth.
    :type username: str
    :param password: Password of git repository basic auth.
    :type password: str
    :param host_key: Public sshKey of git repository.
    :type host_key: str
    :param host_key_algorithm: SshKey algorithm of git repository.
    :type host_key_algorithm: str
    :param private_key: Private sshKey algorithm of git repository.
    :type private_key: str
    :param strict_host_key_checking: Strict host key checking or not.
    :type strict_host_key_checking: bool
    """

    _validation = {
        'name': {'required': True},
        'uri': {'required': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'pattern': {'key': 'pattern', 'type': '[str]'},
        'uri': {'key': 'uri', 'type': 'str'},
        'label': {'key': 'label', 'type': 'str'},
        'search_paths': {'key': 'searchPaths', 'type': '[str]'},
        'username': {'key': 'username', 'type': 'str'},
        'password': {'key': 'password', 'type': 'str'},
        'host_key': {'key': 'hostKey', 'type': 'str'},
        'host_key_algorithm': {'key': 'hostKeyAlgorithm', 'type': 'str'},
        'private_key': {'key': 'privateKey', 'type': 'str'},
        'strict_host_key_checking': {'key': 'strictHostKeyChecking', 'type': 'bool'},
    }

    def __init__(self, **kwargs):
        super(GitPatternRepository, self).__init__(**kwargs)
        self.name = kwargs.get('name', None)
        self.pattern = kwargs.get('pattern', None)
        self.uri = kwargs.get('uri', None)
        self.label = kwargs.get('label', None)
        self.search_paths = kwargs.get('search_paths', None)
        self.username = kwargs.get('username', None)
        self.password = kwargs.get('password', None)
        self.host_key = kwargs.get('host_key', None)
        self.host_key_algorithm = kwargs.get('host_key_algorithm', None)
        self.private_key = kwargs.get('private_key', None)
        self.strict_host_key_checking = kwargs.get('strict_host_key_checking', None)
