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


class PartitionStatusTest(object):
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
        'closed_complete': 'bool',
        'open_incomplete': 'bool',
        'closed_incomplete': 'bool',
        'open_complete': 'bool',
        'not_present': 'bool',
        'reject_on_error': 'bool',
        'checked': 'bool'
    }

    attribute_map = {
        'closed_complete': 'closed_complete',
        'open_incomplete': 'open_incomplete',
        'closed_incomplete': 'closed_incomplete',
        'open_complete': 'open_complete',
        'not_present': 'not_present',
        'reject_on_error': 'reject_on_error',
        'checked': 'checked'
    }

    def __init__(self, closed_complete=None, open_incomplete=None, closed_incomplete=None, open_complete=None, not_present=None, reject_on_error=None, checked=None, local_vars_configuration=None):  # noqa: E501
        """PartitionStatusTest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._closed_complete = None
        self._open_incomplete = None
        self._closed_incomplete = None
        self._open_complete = None
        self._not_present = None
        self._reject_on_error = None
        self._checked = None
        self.discriminator = None

        if closed_complete is not None:
            self.closed_complete = closed_complete
        if open_incomplete is not None:
            self.open_incomplete = open_incomplete
        if closed_incomplete is not None:
            self.closed_incomplete = closed_incomplete
        if open_complete is not None:
            self.open_complete = open_complete
        if not_present is not None:
            self.not_present = not_present
        if reject_on_error is not None:
            self.reject_on_error = reject_on_error
        if checked is not None:
            self.checked = checked

    @property
    def closed_complete(self):
        """Gets the closed_complete of this PartitionStatusTest.  # noqa: E501


        :return: The closed_complete of this PartitionStatusTest.  # noqa: E501
        :rtype: bool
        """
        return self._closed_complete

    @closed_complete.setter
    def closed_complete(self, closed_complete):
        """Sets the closed_complete of this PartitionStatusTest.


        :param closed_complete: The closed_complete of this PartitionStatusTest.  # noqa: E501
        :type: bool
        """

        self._closed_complete = closed_complete

    @property
    def open_incomplete(self):
        """Gets the open_incomplete of this PartitionStatusTest.  # noqa: E501


        :return: The open_incomplete of this PartitionStatusTest.  # noqa: E501
        :rtype: bool
        """
        return self._open_incomplete

    @open_incomplete.setter
    def open_incomplete(self, open_incomplete):
        """Sets the open_incomplete of this PartitionStatusTest.


        :param open_incomplete: The open_incomplete of this PartitionStatusTest.  # noqa: E501
        :type: bool
        """

        self._open_incomplete = open_incomplete

    @property
    def closed_incomplete(self):
        """Gets the closed_incomplete of this PartitionStatusTest.  # noqa: E501


        :return: The closed_incomplete of this PartitionStatusTest.  # noqa: E501
        :rtype: bool
        """
        return self._closed_incomplete

    @closed_incomplete.setter
    def closed_incomplete(self, closed_incomplete):
        """Sets the closed_incomplete of this PartitionStatusTest.


        :param closed_incomplete: The closed_incomplete of this PartitionStatusTest.  # noqa: E501
        :type: bool
        """

        self._closed_incomplete = closed_incomplete

    @property
    def open_complete(self):
        """Gets the open_complete of this PartitionStatusTest.  # noqa: E501


        :return: The open_complete of this PartitionStatusTest.  # noqa: E501
        :rtype: bool
        """
        return self._open_complete

    @open_complete.setter
    def open_complete(self, open_complete):
        """Sets the open_complete of this PartitionStatusTest.


        :param open_complete: The open_complete of this PartitionStatusTest.  # noqa: E501
        :type: bool
        """

        self._open_complete = open_complete

    @property
    def not_present(self):
        """Gets the not_present of this PartitionStatusTest.  # noqa: E501


        :return: The not_present of this PartitionStatusTest.  # noqa: E501
        :rtype: bool
        """
        return self._not_present

    @not_present.setter
    def not_present(self, not_present):
        """Sets the not_present of this PartitionStatusTest.


        :param not_present: The not_present of this PartitionStatusTest.  # noqa: E501
        :type: bool
        """

        self._not_present = not_present

    @property
    def reject_on_error(self):
        """Gets the reject_on_error of this PartitionStatusTest.  # noqa: E501


        :return: The reject_on_error of this PartitionStatusTest.  # noqa: E501
        :rtype: bool
        """
        return self._reject_on_error

    @reject_on_error.setter
    def reject_on_error(self, reject_on_error):
        """Sets the reject_on_error of this PartitionStatusTest.


        :param reject_on_error: The reject_on_error of this PartitionStatusTest.  # noqa: E501
        :type: bool
        """

        self._reject_on_error = reject_on_error

    @property
    def checked(self):
        """Gets the checked of this PartitionStatusTest.  # noqa: E501


        :return: The checked of this PartitionStatusTest.  # noqa: E501
        :rtype: bool
        """
        return self._checked

    @checked.setter
    def checked(self, checked):
        """Sets the checked of this PartitionStatusTest.


        :param checked: The checked of this PartitionStatusTest.  # noqa: E501
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
        if not isinstance(other, PartitionStatusTest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PartitionStatusTest):
            return True

        return self.to_dict() != other.to_dict()
