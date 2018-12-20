# coding: utf-8

"""
    Qc API

    QC API  # noqa: E501

    OpenAPI spec version: 2.0.3
    Contact: cloudsupport@telestream.net
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class SynchronizationEvent(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'timestamp': 'str',
        'skew': 'int',
        'result': 'str'
    }

    attribute_map = {
        'timestamp': 'timestamp',
        'skew': 'skew',
        'result': 'result'
    }

    def __init__(self, timestamp=None, skew=None, result=None):  # noqa: E501
        """SynchronizationEvent - a model defined in Swagger"""  # noqa: E501

        self._timestamp = None
        self._skew = None
        self._result = None
        self.discriminator = None

        if timestamp is not None:
            self.timestamp = timestamp
        if skew is not None:
            self.skew = skew
        if result is not None:
            self.result = result

    @property
    def timestamp(self):
        """Gets the timestamp of this SynchronizationEvent.  # noqa: E501


        :return: The timestamp of this SynchronizationEvent.  # noqa: E501
        :rtype: str
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this SynchronizationEvent.


        :param timestamp: The timestamp of this SynchronizationEvent.  # noqa: E501
        :type: str
        """

        self._timestamp = timestamp

    @property
    def skew(self):
        """Gets the skew of this SynchronizationEvent.  # noqa: E501


        :return: The skew of this SynchronizationEvent.  # noqa: E501
        :rtype: int
        """
        return self._skew

    @skew.setter
    def skew(self, skew):
        """Sets the skew of this SynchronizationEvent.


        :param skew: The skew of this SynchronizationEvent.  # noqa: E501
        :type: int
        """

        self._skew = skew

    @property
    def result(self):
        """Gets the result of this SynchronizationEvent.  # noqa: E501


        :return: The result of this SynchronizationEvent.  # noqa: E501
        :rtype: str
        """
        return self._result

    @result.setter
    def result(self, result):
        """Sets the result of this SynchronizationEvent.


        :param result: The result of this SynchronizationEvent.  # noqa: E501
        :type: str
        """

        self._result = result

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, SynchronizationEvent):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other