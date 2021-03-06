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


class HdrTest(object):
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
        'hdr_standard': 'HdrStandardType',
        'max_fall_max_enabled': 'bool',
        'max_fall_max': 'int',
        'max_fall_error_enabled': 'bool',
        'max_fall_error': 'int',
        'max_cll_max_enabled': 'bool',
        'max_cll_max': 'int',
        'max_cll_error_enabled': 'bool',
        'max_cll_error': 'int',
        'always_calculate': 'bool',
        'always_report': 'bool',
        'reject_on_error': 'bool',
        'checked': 'bool'
    }

    attribute_map = {
        'hdr_standard': 'hdr_standard',
        'max_fall_max_enabled': 'max_fall_max_enabled',
        'max_fall_max': 'max_fall_max',
        'max_fall_error_enabled': 'max_fall_error_enabled',
        'max_fall_error': 'max_fall_error',
        'max_cll_max_enabled': 'max_cll_max_enabled',
        'max_cll_max': 'max_cll_max',
        'max_cll_error_enabled': 'max_cll_error_enabled',
        'max_cll_error': 'max_cll_error',
        'always_calculate': 'always_calculate',
        'always_report': 'always_report',
        'reject_on_error': 'reject_on_error',
        'checked': 'checked'
    }

    def __init__(self, hdr_standard=None, max_fall_max_enabled=None, max_fall_max=None, max_fall_error_enabled=None, max_fall_error=None, max_cll_max_enabled=None, max_cll_max=None, max_cll_error_enabled=None, max_cll_error=None, always_calculate=None, always_report=None, reject_on_error=None, checked=None, local_vars_configuration=None):  # noqa: E501
        """HdrTest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._hdr_standard = None
        self._max_fall_max_enabled = None
        self._max_fall_max = None
        self._max_fall_error_enabled = None
        self._max_fall_error = None
        self._max_cll_max_enabled = None
        self._max_cll_max = None
        self._max_cll_error_enabled = None
        self._max_cll_error = None
        self._always_calculate = None
        self._always_report = None
        self._reject_on_error = None
        self._checked = None
        self.discriminator = None

        if hdr_standard is not None:
            self.hdr_standard = hdr_standard
        if max_fall_max_enabled is not None:
            self.max_fall_max_enabled = max_fall_max_enabled
        if max_fall_max is not None:
            self.max_fall_max = max_fall_max
        if max_fall_error_enabled is not None:
            self.max_fall_error_enabled = max_fall_error_enabled
        if max_fall_error is not None:
            self.max_fall_error = max_fall_error
        if max_cll_max_enabled is not None:
            self.max_cll_max_enabled = max_cll_max_enabled
        if max_cll_max is not None:
            self.max_cll_max = max_cll_max
        if max_cll_error_enabled is not None:
            self.max_cll_error_enabled = max_cll_error_enabled
        if max_cll_error is not None:
            self.max_cll_error = max_cll_error
        if always_calculate is not None:
            self.always_calculate = always_calculate
        if always_report is not None:
            self.always_report = always_report
        if reject_on_error is not None:
            self.reject_on_error = reject_on_error
        if checked is not None:
            self.checked = checked

    @property
    def hdr_standard(self):
        """Gets the hdr_standard of this HdrTest.  # noqa: E501


        :return: The hdr_standard of this HdrTest.  # noqa: E501
        :rtype: HdrStandardType
        """
        return self._hdr_standard

    @hdr_standard.setter
    def hdr_standard(self, hdr_standard):
        """Sets the hdr_standard of this HdrTest.


        :param hdr_standard: The hdr_standard of this HdrTest.  # noqa: E501
        :type: HdrStandardType
        """

        self._hdr_standard = hdr_standard

    @property
    def max_fall_max_enabled(self):
        """Gets the max_fall_max_enabled of this HdrTest.  # noqa: E501


        :return: The max_fall_max_enabled of this HdrTest.  # noqa: E501
        :rtype: bool
        """
        return self._max_fall_max_enabled

    @max_fall_max_enabled.setter
    def max_fall_max_enabled(self, max_fall_max_enabled):
        """Sets the max_fall_max_enabled of this HdrTest.


        :param max_fall_max_enabled: The max_fall_max_enabled of this HdrTest.  # noqa: E501
        :type: bool
        """

        self._max_fall_max_enabled = max_fall_max_enabled

    @property
    def max_fall_max(self):
        """Gets the max_fall_max of this HdrTest.  # noqa: E501


        :return: The max_fall_max of this HdrTest.  # noqa: E501
        :rtype: int
        """
        return self._max_fall_max

    @max_fall_max.setter
    def max_fall_max(self, max_fall_max):
        """Sets the max_fall_max of this HdrTest.


        :param max_fall_max: The max_fall_max of this HdrTest.  # noqa: E501
        :type: int
        """

        self._max_fall_max = max_fall_max

    @property
    def max_fall_error_enabled(self):
        """Gets the max_fall_error_enabled of this HdrTest.  # noqa: E501


        :return: The max_fall_error_enabled of this HdrTest.  # noqa: E501
        :rtype: bool
        """
        return self._max_fall_error_enabled

    @max_fall_error_enabled.setter
    def max_fall_error_enabled(self, max_fall_error_enabled):
        """Sets the max_fall_error_enabled of this HdrTest.


        :param max_fall_error_enabled: The max_fall_error_enabled of this HdrTest.  # noqa: E501
        :type: bool
        """

        self._max_fall_error_enabled = max_fall_error_enabled

    @property
    def max_fall_error(self):
        """Gets the max_fall_error of this HdrTest.  # noqa: E501


        :return: The max_fall_error of this HdrTest.  # noqa: E501
        :rtype: int
        """
        return self._max_fall_error

    @max_fall_error.setter
    def max_fall_error(self, max_fall_error):
        """Sets the max_fall_error of this HdrTest.


        :param max_fall_error: The max_fall_error of this HdrTest.  # noqa: E501
        :type: int
        """

        self._max_fall_error = max_fall_error

    @property
    def max_cll_max_enabled(self):
        """Gets the max_cll_max_enabled of this HdrTest.  # noqa: E501


        :return: The max_cll_max_enabled of this HdrTest.  # noqa: E501
        :rtype: bool
        """
        return self._max_cll_max_enabled

    @max_cll_max_enabled.setter
    def max_cll_max_enabled(self, max_cll_max_enabled):
        """Sets the max_cll_max_enabled of this HdrTest.


        :param max_cll_max_enabled: The max_cll_max_enabled of this HdrTest.  # noqa: E501
        :type: bool
        """

        self._max_cll_max_enabled = max_cll_max_enabled

    @property
    def max_cll_max(self):
        """Gets the max_cll_max of this HdrTest.  # noqa: E501


        :return: The max_cll_max of this HdrTest.  # noqa: E501
        :rtype: int
        """
        return self._max_cll_max

    @max_cll_max.setter
    def max_cll_max(self, max_cll_max):
        """Sets the max_cll_max of this HdrTest.


        :param max_cll_max: The max_cll_max of this HdrTest.  # noqa: E501
        :type: int
        """

        self._max_cll_max = max_cll_max

    @property
    def max_cll_error_enabled(self):
        """Gets the max_cll_error_enabled of this HdrTest.  # noqa: E501


        :return: The max_cll_error_enabled of this HdrTest.  # noqa: E501
        :rtype: bool
        """
        return self._max_cll_error_enabled

    @max_cll_error_enabled.setter
    def max_cll_error_enabled(self, max_cll_error_enabled):
        """Sets the max_cll_error_enabled of this HdrTest.


        :param max_cll_error_enabled: The max_cll_error_enabled of this HdrTest.  # noqa: E501
        :type: bool
        """

        self._max_cll_error_enabled = max_cll_error_enabled

    @property
    def max_cll_error(self):
        """Gets the max_cll_error of this HdrTest.  # noqa: E501


        :return: The max_cll_error of this HdrTest.  # noqa: E501
        :rtype: int
        """
        return self._max_cll_error

    @max_cll_error.setter
    def max_cll_error(self, max_cll_error):
        """Sets the max_cll_error of this HdrTest.


        :param max_cll_error: The max_cll_error of this HdrTest.  # noqa: E501
        :type: int
        """

        self._max_cll_error = max_cll_error

    @property
    def always_calculate(self):
        """Gets the always_calculate of this HdrTest.  # noqa: E501


        :return: The always_calculate of this HdrTest.  # noqa: E501
        :rtype: bool
        """
        return self._always_calculate

    @always_calculate.setter
    def always_calculate(self, always_calculate):
        """Sets the always_calculate of this HdrTest.


        :param always_calculate: The always_calculate of this HdrTest.  # noqa: E501
        :type: bool
        """

        self._always_calculate = always_calculate

    @property
    def always_report(self):
        """Gets the always_report of this HdrTest.  # noqa: E501


        :return: The always_report of this HdrTest.  # noqa: E501
        :rtype: bool
        """
        return self._always_report

    @always_report.setter
    def always_report(self, always_report):
        """Sets the always_report of this HdrTest.


        :param always_report: The always_report of this HdrTest.  # noqa: E501
        :type: bool
        """

        self._always_report = always_report

    @property
    def reject_on_error(self):
        """Gets the reject_on_error of this HdrTest.  # noqa: E501


        :return: The reject_on_error of this HdrTest.  # noqa: E501
        :rtype: bool
        """
        return self._reject_on_error

    @reject_on_error.setter
    def reject_on_error(self, reject_on_error):
        """Sets the reject_on_error of this HdrTest.


        :param reject_on_error: The reject_on_error of this HdrTest.  # noqa: E501
        :type: bool
        """

        self._reject_on_error = reject_on_error

    @property
    def checked(self):
        """Gets the checked of this HdrTest.  # noqa: E501


        :return: The checked of this HdrTest.  # noqa: E501
        :rtype: bool
        """
        return self._checked

    @checked.setter
    def checked(self, checked):
        """Sets the checked of this HdrTest.


        :param checked: The checked of this HdrTest.  # noqa: E501
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
        if not isinstance(other, HdrTest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, HdrTest):
            return True

        return self.to_dict() != other.to_dict()
