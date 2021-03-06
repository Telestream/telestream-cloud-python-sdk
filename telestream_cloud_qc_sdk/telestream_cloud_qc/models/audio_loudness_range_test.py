# coding: utf-8

"""
    Qc API

    Qc API  # noqa: E501

    The version of the OpenAPI document: 3.0.0
    Contact: cloudsupport@telestream.net
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from telestream_cloud_qc.configuration import Configuration


class AudioLoudnessRangeTest(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'do_min': 'bool',
        'range_min': 'float',
        'do_max': 'bool',
        'range_max': 'float',
        'channels': 'Channels',
        'reject_on_error': 'bool',
        'checked': 'bool'
    }

    attribute_map = {
        'do_min': 'do_min',
        'range_min': 'range_min',
        'do_max': 'do_max',
        'range_max': 'range_max',
        'channels': 'channels',
        'reject_on_error': 'reject_on_error',
        'checked': 'checked'
    }

    def __init__(self, do_min=None, range_min=None, do_max=None, range_max=None, channels=None, reject_on_error=None, checked=None, local_vars_configuration=None):  # noqa: E501
        """AudioLoudnessRangeTest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._do_min = None
        self._range_min = None
        self._do_max = None
        self._range_max = None
        self._channels = None
        self._reject_on_error = None
        self._checked = None
        self.discriminator = None

        if do_min is not None:
            self.do_min = do_min
        if range_min is not None:
            self.range_min = range_min
        if do_max is not None:
            self.do_max = do_max
        if range_max is not None:
            self.range_max = range_max
        if channels is not None:
            self.channels = channels
        if reject_on_error is not None:
            self.reject_on_error = reject_on_error
        if checked is not None:
            self.checked = checked

    @property
    def do_min(self):
        """Gets the do_min of this AudioLoudnessRangeTest.  # noqa: E501


        :return: The do_min of this AudioLoudnessRangeTest.  # noqa: E501
        :rtype: bool
        """
        return self._do_min

    @do_min.setter
    def do_min(self, do_min):
        """Sets the do_min of this AudioLoudnessRangeTest.


        :param do_min: The do_min of this AudioLoudnessRangeTest.  # noqa: E501
        :type: bool
        """

        self._do_min = do_min

    @property
    def range_min(self):
        """Gets the range_min of this AudioLoudnessRangeTest.  # noqa: E501


        :return: The range_min of this AudioLoudnessRangeTest.  # noqa: E501
        :rtype: float
        """
        return self._range_min

    @range_min.setter
    def range_min(self, range_min):
        """Sets the range_min of this AudioLoudnessRangeTest.


        :param range_min: The range_min of this AudioLoudnessRangeTest.  # noqa: E501
        :type: float
        """

        self._range_min = range_min

    @property
    def do_max(self):
        """Gets the do_max of this AudioLoudnessRangeTest.  # noqa: E501


        :return: The do_max of this AudioLoudnessRangeTest.  # noqa: E501
        :rtype: bool
        """
        return self._do_max

    @do_max.setter
    def do_max(self, do_max):
        """Sets the do_max of this AudioLoudnessRangeTest.


        :param do_max: The do_max of this AudioLoudnessRangeTest.  # noqa: E501
        :type: bool
        """

        self._do_max = do_max

    @property
    def range_max(self):
        """Gets the range_max of this AudioLoudnessRangeTest.  # noqa: E501


        :return: The range_max of this AudioLoudnessRangeTest.  # noqa: E501
        :rtype: float
        """
        return self._range_max

    @range_max.setter
    def range_max(self, range_max):
        """Sets the range_max of this AudioLoudnessRangeTest.


        :param range_max: The range_max of this AudioLoudnessRangeTest.  # noqa: E501
        :type: float
        """

        self._range_max = range_max

    @property
    def channels(self):
        """Gets the channels of this AudioLoudnessRangeTest.  # noqa: E501


        :return: The channels of this AudioLoudnessRangeTest.  # noqa: E501
        :rtype: Channels
        """
        return self._channels

    @channels.setter
    def channels(self, channels):
        """Sets the channels of this AudioLoudnessRangeTest.


        :param channels: The channels of this AudioLoudnessRangeTest.  # noqa: E501
        :type: Channels
        """

        self._channels = channels

    @property
    def reject_on_error(self):
        """Gets the reject_on_error of this AudioLoudnessRangeTest.  # noqa: E501


        :return: The reject_on_error of this AudioLoudnessRangeTest.  # noqa: E501
        :rtype: bool
        """
        return self._reject_on_error

    @reject_on_error.setter
    def reject_on_error(self, reject_on_error):
        """Sets the reject_on_error of this AudioLoudnessRangeTest.


        :param reject_on_error: The reject_on_error of this AudioLoudnessRangeTest.  # noqa: E501
        :type: bool
        """

        self._reject_on_error = reject_on_error

    @property
    def checked(self):
        """Gets the checked of this AudioLoudnessRangeTest.  # noqa: E501


        :return: The checked of this AudioLoudnessRangeTest.  # noqa: E501
        :rtype: bool
        """
        return self._checked

    @checked.setter
    def checked(self, checked):
        """Sets the checked of this AudioLoudnessRangeTest.


        :param checked: The checked of this AudioLoudnessRangeTest.  # noqa: E501
        :type: bool
        """

        self._checked = checked

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        if not isinstance(other, AudioLoudnessRangeTest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AudioLoudnessRangeTest):
            return True

        return self.to_dict() != other.to_dict()
