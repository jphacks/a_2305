# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class AuthUserRequest(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, id=None, password=None):  # noqa: E501
        """AuthUserRequest - a model defined in OpenAPI

        :param id: The id of this AuthUserRequest.  # noqa: E501
        :type id: str
        :param password: The password of this AuthUserRequest.  # noqa: E501
        :type password: str
        """
        self.openapi_types = {
            'id': str,
            'password': str
        }

        self.attribute_map = {
            'id': 'id',
            'password': 'password'
        }

        self._id = id
        self._password = password

    @classmethod
    def from_dict(cls, dikt) -> 'AuthUserRequest':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The authUser_request of this AuthUserRequest.  # noqa: E501
        :rtype: AuthUserRequest
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self):
        """Gets the id of this AuthUserRequest.


        :return: The id of this AuthUserRequest.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AuthUserRequest.


        :param id: The id of this AuthUserRequest.
        :type id: str
        """

        self._id = id

    @property
    def password(self):
        """Gets the password of this AuthUserRequest.


        :return: The password of this AuthUserRequest.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this AuthUserRequest.


        :param password: The password of this AuthUserRequest.
        :type password: str
        """

        self._password = password