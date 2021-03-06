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


class ChromaLevelTest(object):
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
        'y_level_default_or_custom': 'DefaultOrCustomType',
        'y_level_lower': 'int',
        'y_level_upper': 'int',
        'y_level_max_outside_range': 'float',
        'y_level_tolerance_low': 'float',
        'y_level_tolerance_high': 'float',
        'u_vlevel_default_or_custom': 'DefaultOrCustomType',
        'u_vlevel_lower': 'int',
        'u_vlevel_upper': 'int',
        'u_vlevel_max_outside_range': 'float',
        'low_pass_filter': 'LowPassFilterType',
        'reject_on_error': 'bool',
        'do_correction': 'bool',
        'checked': 'bool'
    }

    attribute_map = {
        'y_level_default_or_custom': 'y_level_default_or_custom',
        'y_level_lower': 'y_level_lower',
        'y_level_upper': 'y_level_upper',
        'y_level_max_outside_range': 'y_level_max_outside_range',
        'y_level_tolerance_low': 'y_level_tolerance_low',
        'y_level_tolerance_high': 'y_level_tolerance_high',
        'u_vlevel_default_or_custom': 'u_vlevel_default_or_custom',
        'u_vlevel_lower': 'u_vlevel_lower',
        'u_vlevel_upper': 'u_vlevel_upper',
        'u_vlevel_max_outside_range': 'u_vlevel_max_outside_range',
        'low_pass_filter': 'low_pass_filter',
        'reject_on_error': 'reject_on_error',
        'do_correction': 'do_correction',
        'checked': 'checked'
    }

    def __init__(self, y_level_default_or_custom=None, y_level_lower=None, y_level_upper=None, y_level_max_outside_range=None, y_level_tolerance_low=None, y_level_tolerance_high=None, u_vlevel_default_or_custom=None, u_vlevel_lower=None, u_vlevel_upper=None, u_vlevel_max_outside_range=None, low_pass_filter=None, reject_on_error=None, do_correction=None, checked=None, local_vars_configuration=None):  # noqa: E501
        """ChromaLevelTest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._y_level_default_or_custom = None
        self._y_level_lower = None
        self._y_level_upper = None
        self._y_level_max_outside_range = None
        self._y_level_tolerance_low = None
        self._y_level_tolerance_high = None
        self._u_vlevel_default_or_custom = None
        self._u_vlevel_lower = None
        self._u_vlevel_upper = None
        self._u_vlevel_max_outside_range = None
        self._low_pass_filter = None
        self._reject_on_error = None
        self._do_correction = None
        self._checked = None
        self.discriminator = None

        if y_level_default_or_custom is not None:
            self.y_level_default_or_custom = y_level_default_or_custom
        if y_level_lower is not None:
            self.y_level_lower = y_level_lower
        if y_level_upper is not None:
            self.y_level_upper = y_level_upper
        if y_level_max_outside_range is not None:
            self.y_level_max_outside_range = y_level_max_outside_range
        if y_level_tolerance_low is not None:
            self.y_level_tolerance_low = y_level_tolerance_low
        if y_level_tolerance_high is not None:
            self.y_level_tolerance_high = y_level_tolerance_high
        if u_vlevel_default_or_custom is not None:
            self.u_vlevel_default_or_custom = u_vlevel_default_or_custom
        if u_vlevel_lower is not None:
            self.u_vlevel_lower = u_vlevel_lower
        if u_vlevel_upper is not None:
            self.u_vlevel_upper = u_vlevel_upper
        if u_vlevel_max_outside_range is not None:
            self.u_vlevel_max_outside_range = u_vlevel_max_outside_range
        if low_pass_filter is not None:
            self.low_pass_filter = low_pass_filter
        if reject_on_error is not None:
            self.reject_on_error = reject_on_error
        if do_correction is not None:
            self.do_correction = do_correction
        if checked is not None:
            self.checked = checked

    @property
    def y_level_default_or_custom(self):
        """Gets the y_level_default_or_custom of this ChromaLevelTest.  # noqa: E501


        :return: The y_level_default_or_custom of this ChromaLevelTest.  # noqa: E501
        :rtype: DefaultOrCustomType
        """
        return self._y_level_default_or_custom

    @y_level_default_or_custom.setter
    def y_level_default_or_custom(self, y_level_default_or_custom):
        """Sets the y_level_default_or_custom of this ChromaLevelTest.


        :param y_level_default_or_custom: The y_level_default_or_custom of this ChromaLevelTest.  # noqa: E501
        :type: DefaultOrCustomType
        """

        self._y_level_default_or_custom = y_level_default_or_custom

    @property
    def y_level_lower(self):
        """Gets the y_level_lower of this ChromaLevelTest.  # noqa: E501


        :return: The y_level_lower of this ChromaLevelTest.  # noqa: E501
        :rtype: int
        """
        return self._y_level_lower

    @y_level_lower.setter
    def y_level_lower(self, y_level_lower):
        """Sets the y_level_lower of this ChromaLevelTest.


        :param y_level_lower: The y_level_lower of this ChromaLevelTest.  # noqa: E501
        :type: int
        """

        self._y_level_lower = y_level_lower

    @property
    def y_level_upper(self):
        """Gets the y_level_upper of this ChromaLevelTest.  # noqa: E501


        :return: The y_level_upper of this ChromaLevelTest.  # noqa: E501
        :rtype: int
        """
        return self._y_level_upper

    @y_level_upper.setter
    def y_level_upper(self, y_level_upper):
        """Sets the y_level_upper of this ChromaLevelTest.


        :param y_level_upper: The y_level_upper of this ChromaLevelTest.  # noqa: E501
        :type: int
        """

        self._y_level_upper = y_level_upper

    @property
    def y_level_max_outside_range(self):
        """Gets the y_level_max_outside_range of this ChromaLevelTest.  # noqa: E501


        :return: The y_level_max_outside_range of this ChromaLevelTest.  # noqa: E501
        :rtype: float
        """
        return self._y_level_max_outside_range

    @y_level_max_outside_range.setter
    def y_level_max_outside_range(self, y_level_max_outside_range):
        """Sets the y_level_max_outside_range of this ChromaLevelTest.


        :param y_level_max_outside_range: The y_level_max_outside_range of this ChromaLevelTest.  # noqa: E501
        :type: float
        """

        self._y_level_max_outside_range = y_level_max_outside_range

    @property
    def y_level_tolerance_low(self):
        """Gets the y_level_tolerance_low of this ChromaLevelTest.  # noqa: E501


        :return: The y_level_tolerance_low of this ChromaLevelTest.  # noqa: E501
        :rtype: float
        """
        return self._y_level_tolerance_low

    @y_level_tolerance_low.setter
    def y_level_tolerance_low(self, y_level_tolerance_low):
        """Sets the y_level_tolerance_low of this ChromaLevelTest.


        :param y_level_tolerance_low: The y_level_tolerance_low of this ChromaLevelTest.  # noqa: E501
        :type: float
        """

        self._y_level_tolerance_low = y_level_tolerance_low

    @property
    def y_level_tolerance_high(self):
        """Gets the y_level_tolerance_high of this ChromaLevelTest.  # noqa: E501


        :return: The y_level_tolerance_high of this ChromaLevelTest.  # noqa: E501
        :rtype: float
        """
        return self._y_level_tolerance_high

    @y_level_tolerance_high.setter
    def y_level_tolerance_high(self, y_level_tolerance_high):
        """Sets the y_level_tolerance_high of this ChromaLevelTest.


        :param y_level_tolerance_high: The y_level_tolerance_high of this ChromaLevelTest.  # noqa: E501
        :type: float
        """

        self._y_level_tolerance_high = y_level_tolerance_high

    @property
    def u_vlevel_default_or_custom(self):
        """Gets the u_vlevel_default_or_custom of this ChromaLevelTest.  # noqa: E501


        :return: The u_vlevel_default_or_custom of this ChromaLevelTest.  # noqa: E501
        :rtype: DefaultOrCustomType
        """
        return self._u_vlevel_default_or_custom

    @u_vlevel_default_or_custom.setter
    def u_vlevel_default_or_custom(self, u_vlevel_default_or_custom):
        """Sets the u_vlevel_default_or_custom of this ChromaLevelTest.


        :param u_vlevel_default_or_custom: The u_vlevel_default_or_custom of this ChromaLevelTest.  # noqa: E501
        :type: DefaultOrCustomType
        """

        self._u_vlevel_default_or_custom = u_vlevel_default_or_custom

    @property
    def u_vlevel_lower(self):
        """Gets the u_vlevel_lower of this ChromaLevelTest.  # noqa: E501


        :return: The u_vlevel_lower of this ChromaLevelTest.  # noqa: E501
        :rtype: int
        """
        return self._u_vlevel_lower

    @u_vlevel_lower.setter
    def u_vlevel_lower(self, u_vlevel_lower):
        """Sets the u_vlevel_lower of this ChromaLevelTest.


        :param u_vlevel_lower: The u_vlevel_lower of this ChromaLevelTest.  # noqa: E501
        :type: int
        """

        self._u_vlevel_lower = u_vlevel_lower

    @property
    def u_vlevel_upper(self):
        """Gets the u_vlevel_upper of this ChromaLevelTest.  # noqa: E501


        :return: The u_vlevel_upper of this ChromaLevelTest.  # noqa: E501
        :rtype: int
        """
        return self._u_vlevel_upper

    @u_vlevel_upper.setter
    def u_vlevel_upper(self, u_vlevel_upper):
        """Sets the u_vlevel_upper of this ChromaLevelTest.


        :param u_vlevel_upper: The u_vlevel_upper of this ChromaLevelTest.  # noqa: E501
        :type: int
        """

        self._u_vlevel_upper = u_vlevel_upper

    @property
    def u_vlevel_max_outside_range(self):
        """Gets the u_vlevel_max_outside_range of this ChromaLevelTest.  # noqa: E501


        :return: The u_vlevel_max_outside_range of this ChromaLevelTest.  # noqa: E501
        :rtype: float
        """
        return self._u_vlevel_max_outside_range

    @u_vlevel_max_outside_range.setter
    def u_vlevel_max_outside_range(self, u_vlevel_max_outside_range):
        """Sets the u_vlevel_max_outside_range of this ChromaLevelTest.


        :param u_vlevel_max_outside_range: The u_vlevel_max_outside_range of this ChromaLevelTest.  # noqa: E501
        :type: float
        """

        self._u_vlevel_max_outside_range = u_vlevel_max_outside_range

    @property
    def low_pass_filter(self):
        """Gets the low_pass_filter of this ChromaLevelTest.  # noqa: E501


        :return: The low_pass_filter of this ChromaLevelTest.  # noqa: E501
        :rtype: LowPassFilterType
        """
        return self._low_pass_filter

    @low_pass_filter.setter
    def low_pass_filter(self, low_pass_filter):
        """Sets the low_pass_filter of this ChromaLevelTest.


        :param low_pass_filter: The low_pass_filter of this ChromaLevelTest.  # noqa: E501
        :type: LowPassFilterType
        """

        self._low_pass_filter = low_pass_filter

    @property
    def reject_on_error(self):
        """Gets the reject_on_error of this ChromaLevelTest.  # noqa: E501


        :return: The reject_on_error of this ChromaLevelTest.  # noqa: E501
        :rtype: bool
        """
        return self._reject_on_error

    @reject_on_error.setter
    def reject_on_error(self, reject_on_error):
        """Sets the reject_on_error of this ChromaLevelTest.


        :param reject_on_error: The reject_on_error of this ChromaLevelTest.  # noqa: E501
        :type: bool
        """

        self._reject_on_error = reject_on_error

    @property
    def do_correction(self):
        """Gets the do_correction of this ChromaLevelTest.  # noqa: E501


        :return: The do_correction of this ChromaLevelTest.  # noqa: E501
        :rtype: bool
        """
        return self._do_correction

    @do_correction.setter
    def do_correction(self, do_correction):
        """Sets the do_correction of this ChromaLevelTest.


        :param do_correction: The do_correction of this ChromaLevelTest.  # noqa: E501
        :type: bool
        """

        self._do_correction = do_correction

    @property
    def checked(self):
        """Gets the checked of this ChromaLevelTest.  # noqa: E501


        :return: The checked of this ChromaLevelTest.  # noqa: E501
        :rtype: bool
        """
        return self._checked

    @checked.setter
    def checked(self, checked):
        """Sets the checked of this ChromaLevelTest.


        :param checked: The checked of this ChromaLevelTest.  # noqa: E501
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
        if not isinstance(other, ChromaLevelTest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ChromaLevelTest):
            return True

        return self.to_dict() != other.to_dict()
