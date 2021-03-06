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


class BlackLevelTest(object):
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
        'level_default_or_custom': 'DefaultOrCustomType',
        'level': 'int',
        'level_max_outside_range': 'float',
        'reject_on_error': 'bool',
        'do_correction': 'bool',
        'checked': 'bool'
    }

    attribute_map = {
        'level_default_or_custom': 'level_default_or_custom',
        'level': 'level',
        'level_max_outside_range': 'level_max_outside_range',
        'reject_on_error': 'reject_on_error',
        'do_correction': 'do_correction',
        'checked': 'checked'
    }

    def __init__(self, level_default_or_custom=None, level=None, level_max_outside_range=None, reject_on_error=None, do_correction=None, checked=None, local_vars_configuration=None):  # noqa: E501
        """BlackLevelTest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._level_default_or_custom = None
        self._level = None
        self._level_max_outside_range = None
        self._reject_on_error = None
        self._do_correction = None
        self._checked = None
        self.discriminator = None

        if level_default_or_custom is not None:
            self.level_default_or_custom = level_default_or_custom
        if level is not None:
            self.level = level
        if level_max_outside_range is not None:
            self.level_max_outside_range = level_max_outside_range
        if reject_on_error is not None:
            self.reject_on_error = reject_on_error
        if do_correction is not None:
            self.do_correction = do_correction
        if checked is not None:
            self.checked = checked

    @property
    def level_default_or_custom(self):
        """Gets the level_default_or_custom of this BlackLevelTest.  # noqa: E501


        :return: The level_default_or_custom of this BlackLevelTest.  # noqa: E501
        :rtype: DefaultOrCustomType
        """
        return self._level_default_or_custom

    @level_default_or_custom.setter
    def level_default_or_custom(self, level_default_or_custom):
        """Sets the level_default_or_custom of this BlackLevelTest.


        :param level_default_or_custom: The level_default_or_custom of this BlackLevelTest.  # noqa: E501
        :type: DefaultOrCustomType
        """

        self._level_default_or_custom = level_default_or_custom

    @property
    def level(self):
        """Gets the level of this BlackLevelTest.  # noqa: E501


        :return: The level of this BlackLevelTest.  # noqa: E501
        :rtype: int
        """
        return self._level

    @level.setter
    def level(self, level):
        """Sets the level of this BlackLevelTest.


        :param level: The level of this BlackLevelTest.  # noqa: E501
        :type: int
        """

        self._level = level

    @property
    def level_max_outside_range(self):
        """Gets the level_max_outside_range of this BlackLevelTest.  # noqa: E501


        :return: The level_max_outside_range of this BlackLevelTest.  # noqa: E501
        :rtype: float
        """
        return self._level_max_outside_range

    @level_max_outside_range.setter
    def level_max_outside_range(self, level_max_outside_range):
        """Sets the level_max_outside_range of this BlackLevelTest.


        :param level_max_outside_range: The level_max_outside_range of this BlackLevelTest.  # noqa: E501
        :type: float
        """

        self._level_max_outside_range = level_max_outside_range

    @property
    def reject_on_error(self):
        """Gets the reject_on_error of this BlackLevelTest.  # noqa: E501


        :return: The reject_on_error of this BlackLevelTest.  # noqa: E501
        :rtype: bool
        """
        return self._reject_on_error

    @reject_on_error.setter
    def reject_on_error(self, reject_on_error):
        """Sets the reject_on_error of this BlackLevelTest.


        :param reject_on_error: The reject_on_error of this BlackLevelTest.  # noqa: E501
        :type: bool
        """

        self._reject_on_error = reject_on_error

    @property
    def do_correction(self):
        """Gets the do_correction of this BlackLevelTest.  # noqa: E501


        :return: The do_correction of this BlackLevelTest.  # noqa: E501
        :rtype: bool
        """
        return self._do_correction

    @do_correction.setter
    def do_correction(self, do_correction):
        """Sets the do_correction of this BlackLevelTest.


        :param do_correction: The do_correction of this BlackLevelTest.  # noqa: E501
        :type: bool
        """

        self._do_correction = do_correction

    @property
    def checked(self):
        """Gets the checked of this BlackLevelTest.  # noqa: E501


        :return: The checked of this BlackLevelTest.  # noqa: E501
        :rtype: bool
        """
        return self._checked

    @checked.setter
    def checked(self, checked):
        """Sets the checked of this BlackLevelTest.


        :param checked: The checked of this BlackLevelTest.  # noqa: E501
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
        if not isinstance(other, BlackLevelTest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, BlackLevelTest):
            return True

        return self.to_dict() != other.to_dict()
