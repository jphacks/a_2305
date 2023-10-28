# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class NewUserRequest(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, nickname=None, id=None, password=None):  # noqa: E501
        """NewUserRequest - a model defined in OpenAPI

        :param nickname: The nickname of this NewUserRequest.  # noqa: E501
        :type nickname: str
        :param id: The id of this NewUserRequest.  # noqa: E501
        :type id: str
        :param password: The password of this NewUserRequest.  # noqa: E501
        :type password: str
        """
        self.openapi_types = {
            'nickname': str,
            'id': str,
            'password': str
        }

        self.attribute_map = {
            'nickname': 'nickname',
            'id': 'id',
            'password': 'password'
        }

        self._nickname = nickname
        self._id = id
        self._password = password

    @classmethod
    def from_dict(cls, dikt) -> 'NewUserRequest':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The newUser_request of this NewUserRequest.  # noqa: E501
        :rtype: NewUserRequest
        """
        return util.deserialize_model(dikt, cls)

    @property
    def nickname(self):
        """Gets the nickname of this NewUserRequest.


        :return: The nickname of this NewUserRequest.
        :rtype: str
        """
        return self._nickname

    @nickname.setter
    def nickname(self, nickname):
        """Sets the nickname of this NewUserRequest.


        :param nickname: The nickname of this NewUserRequest.
        :type nickname: str
        """

        self._nickname = nickname

    @property
    def id(self):
        """Gets the id of this NewUserRequest.


        :return: The id of this NewUserRequest.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this NewUserRequest.


        :param id: The id of this NewUserRequest.
        :type id: str
        """

        self._id = id

    @property
    def password(self):
        """Gets the password of this NewUserRequest.


        :return: The password of this NewUserRequest.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this NewUserRequest.


        :param password: The password of this NewUserRequest.
        :type password: str
        """

        self._password = password
