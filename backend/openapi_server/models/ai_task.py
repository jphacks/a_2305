# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.schedule import Schedule
from openapi_server import util

from openapi_server.models.schedule import Schedule  # noqa: E501

class AITask(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, task=None, start=None, end=None):  # noqa: E501
        """AITask - a model defined in OpenAPI

        :param task: The task of this AITask.  # noqa: E501
        :type task: Schedule
        :param start: The start of this AITask.  # noqa: E501
        :type start: datetime
        :param end: The end of this AITask.  # noqa: E501
        :type end: datetime
        """
        self.openapi_types = {
            'task': Schedule,
            'start': datetime,
            'end': datetime
        }

        self.attribute_map = {
            'task': 'Task',
            'start': 'start',
            'end': 'end'
        }

        self._task = task
        self._start = start
        self._end = end

    @classmethod
    def from_dict(cls, dikt) -> 'AITask':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The AITask of this AITask.  # noqa: E501
        :rtype: AITask
        """
        return util.deserialize_model(dikt, cls)

    @property
    def task(self):
        """Gets the task of this AITask.


        :return: The task of this AITask.
        :rtype: Schedule
        """
        return self._task

    @task.setter
    def task(self, task):
        """Sets the task of this AITask.


        :param task: The task of this AITask.
        :type task: Schedule
        """

        self._task = task

    @property
    def start(self):
        """Gets the start of this AITask.


        :return: The start of this AITask.
        :rtype: datetime
        """
        return self._start

    @start.setter
    def start(self, start):
        """Sets the start of this AITask.


        :param start: The start of this AITask.
        :type start: datetime
        """

        self._start = start

    @property
    def end(self):
        """Gets the end of this AITask.


        :return: The end of this AITask.
        :rtype: datetime
        """
        return self._end

    @end.setter
    def end(self, end):
        """Sets the end of this AITask.


        :param end: The end of this AITask.
        :type end: datetime
        """

        self._end = end
