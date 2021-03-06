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


class FlashTest(object):
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
        'check_type': 'PSeParameterType',
        'check_for_extended': 'bool',
        'check_for_red': 'bool',
        'check_for_patterns': 'bool',
        'reject_on_error': 'bool',
        'do_correction': 'bool',
        'checked': 'bool'
    }

    attribute_map = {
        'check_type': 'check_type',
        'check_for_extended': 'check_for_extended',
        'check_for_red': 'check_for_red',
        'check_for_patterns': 'check_for_patterns',
        'reject_on_error': 'reject_on_error',
        'do_correction': 'do_correction',
        'checked': 'checked'
    }

    def __init__(self, check_type=None, check_for_extended=None, check_for_red=None, check_for_patterns=None, reject_on_error=None, do_correction=None, checked=None, local_vars_configuration=None):  # noqa: E501
        """FlashTest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._check_type = None
        self._check_for_extended = None
        self._check_for_red = None
        self._check_for_patterns = None
        self._reject_on_error = None
        self._do_correction = None
        self._checked = None
        self.discriminator = None

        if check_type is not None:
            self.check_type = check_type
        if check_for_extended is not None:
            self.check_for_extended = check_for_extended
        if check_for_red is not None:
            self.check_for_red = check_for_red
        if check_for_patterns is not None:
            self.check_for_patterns = check_for_patterns
        if reject_on_error is not None:
            self.reject_on_error = reject_on_error
        if do_correction is not None:
            self.do_correction = do_correction
        if checked is not None:
            self.checked = checked

    @property
    def check_type(self):
        """Gets the check_type of this FlashTest.  # noqa: E501


        :return: The check_type of this FlashTest.  # noqa: E501
        :rtype: PSeParameterType
        """
        return self._check_type

    @check_type.setter
    def check_type(self, check_type):
        """Sets the check_type of this FlashTest.


        :param check_type: The check_type of this FlashTest.  # noqa: E501
        :type: PSeParameterType
        """

        self._check_type = check_type

    @property
    def check_for_extended(self):
        """Gets the check_for_extended of this FlashTest.  # noqa: E501


        :return: The check_for_extended of this FlashTest.  # noqa: E501
        :rtype: bool
        """
        return self._check_for_extended

    @check_for_extended.setter
    def check_for_extended(self, check_for_extended):
        """Sets the check_for_extended of this FlashTest.


        :param check_for_extended: The check_for_extended of this FlashTest.  # noqa: E501
        :type: bool
        """

        self._check_for_extended = check_for_extended

    @property
    def check_for_red(self):
        """Gets the check_for_red of this FlashTest.  # noqa: E501


        :return: The check_for_red of this FlashTest.  # noqa: E501
        :rtype: bool
        """
        return self._check_for_red

    @check_for_red.setter
    def check_for_red(self, check_for_red):
        """Sets the check_for_red of this FlashTest.


        :param check_for_red: The check_for_red of this FlashTest.  # noqa: E501
        :type: bool
        """

        self._check_for_red = check_for_red

    @property
    def check_for_patterns(self):
        """Gets the check_for_patterns of this FlashTest.  # noqa: E501


        :return: The check_for_patterns of this FlashTest.  # noqa: E501
        :rtype: bool
        """
        return self._check_for_patterns

    @check_for_patterns.setter
    def check_for_patterns(self, check_for_patterns):
        """Sets the check_for_patterns of this FlashTest.


        :param check_for_patterns: The check_for_patterns of this FlashTest.  # noqa: E501
        :type: bool
        """

        self._check_for_patterns = check_for_patterns

    @property
    def reject_on_error(self):
        """Gets the reject_on_error of this FlashTest.  # noqa: E501


        :return: The reject_on_error of this FlashTest.  # noqa: E501
        :rtype: bool
        """
        return self._reject_on_error

    @reject_on_error.setter
    def reject_on_error(self, reject_on_error):
        """Sets the reject_on_error of this FlashTest.


        :param reject_on_error: The reject_on_error of this FlashTest.  # noqa: E501
        :type: bool
        """

        self._reject_on_error = reject_on_error

    @property
    def do_correction(self):
        """Gets the do_correction of this FlashTest.  # noqa: E501


        :return: The do_correction of this FlashTest.  # noqa: E501
        :rtype: bool
        """
        return self._do_correction

    @do_correction.setter
    def do_correction(self, do_correction):
        """Sets the do_correction of this FlashTest.


        :param do_correction: The do_correction of this FlashTest.  # noqa: E501
        :type: bool
        """

        self._do_correction = do_correction

    @property
    def checked(self):
        """Gets the checked of this FlashTest.  # noqa: E501


        :return: The checked of this FlashTest.  # noqa: E501
        :rtype: bool
        """
        return self._checked

    @checked.setter
    def checked(self, checked):
        """Sets the checked of this FlashTest.


        :param checked: The checked of this FlashTest.  # noqa: E501
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
        if not isinstance(other, FlashTest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, FlashTest):
            return True

        return self.to_dict() != other.to_dict()
