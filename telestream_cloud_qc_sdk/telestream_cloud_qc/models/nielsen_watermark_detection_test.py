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


class NielsenWatermarkDetectionTest(object):
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
        'naes2_enabled': 'bool',
        'naes2_sids_any_or_specific': 'SidsAnyOrSpecific',
        'naes2_sids': 'str',
        'naes2_high_frequency_enabled': 'bool',
        'naes2_high_frequency_sids_any_or_specific': 'SidsAnyOrSpecific',
        'naes2_high_frequency_sids': 'str',
        'naes6_enabled': 'bool',
        'naes6_sids_any_or_specific': 'SidsAnyOrSpecific',
        'naes6_sids': 'str',
        'channels': 'Channels',
        'reject_on_error': 'bool',
        'checked': 'bool'
    }

    attribute_map = {
        'naes2_enabled': 'naes2_enabled',
        'naes2_sids_any_or_specific': 'naes2_sids_any_or_specific',
        'naes2_sids': 'naes2_sids',
        'naes2_high_frequency_enabled': 'naes2_high_frequency_enabled',
        'naes2_high_frequency_sids_any_or_specific': 'naes2_high_frequency_sids_any_or_specific',
        'naes2_high_frequency_sids': 'naes2_high_frequency_sids',
        'naes6_enabled': 'naes6_enabled',
        'naes6_sids_any_or_specific': 'naes6_sids_any_or_specific',
        'naes6_sids': 'naes6_sids',
        'channels': 'channels',
        'reject_on_error': 'reject_on_error',
        'checked': 'checked'
    }

    def __init__(self, naes2_enabled=None, naes2_sids_any_or_specific=None, naes2_sids=None, naes2_high_frequency_enabled=None, naes2_high_frequency_sids_any_or_specific=None, naes2_high_frequency_sids=None, naes6_enabled=None, naes6_sids_any_or_specific=None, naes6_sids=None, channels=None, reject_on_error=None, checked=None, local_vars_configuration=None):  # noqa: E501
        """NielsenWatermarkDetectionTest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._naes2_enabled = None
        self._naes2_sids_any_or_specific = None
        self._naes2_sids = None
        self._naes2_high_frequency_enabled = None
        self._naes2_high_frequency_sids_any_or_specific = None
        self._naes2_high_frequency_sids = None
        self._naes6_enabled = None
        self._naes6_sids_any_or_specific = None
        self._naes6_sids = None
        self._channels = None
        self._reject_on_error = None
        self._checked = None
        self.discriminator = None

        if naes2_enabled is not None:
            self.naes2_enabled = naes2_enabled
        if naes2_sids_any_or_specific is not None:
            self.naes2_sids_any_or_specific = naes2_sids_any_or_specific
        if naes2_sids is not None:
            self.naes2_sids = naes2_sids
        if naes2_high_frequency_enabled is not None:
            self.naes2_high_frequency_enabled = naes2_high_frequency_enabled
        if naes2_high_frequency_sids_any_or_specific is not None:
            self.naes2_high_frequency_sids_any_or_specific = naes2_high_frequency_sids_any_or_specific
        if naes2_high_frequency_sids is not None:
            self.naes2_high_frequency_sids = naes2_high_frequency_sids
        if naes6_enabled is not None:
            self.naes6_enabled = naes6_enabled
        if naes6_sids_any_or_specific is not None:
            self.naes6_sids_any_or_specific = naes6_sids_any_or_specific
        if naes6_sids is not None:
            self.naes6_sids = naes6_sids
        if channels is not None:
            self.channels = channels
        if reject_on_error is not None:
            self.reject_on_error = reject_on_error
        if checked is not None:
            self.checked = checked

    @property
    def naes2_enabled(self):
        """Gets the naes2_enabled of this NielsenWatermarkDetectionTest.  # noqa: E501


        :return: The naes2_enabled of this NielsenWatermarkDetectionTest.  # noqa: E501
        :rtype: bool
        """
        return self._naes2_enabled

    @naes2_enabled.setter
    def naes2_enabled(self, naes2_enabled):
        """Sets the naes2_enabled of this NielsenWatermarkDetectionTest.


        :param naes2_enabled: The naes2_enabled of this NielsenWatermarkDetectionTest.  # noqa: E501
        :type: bool
        """

        self._naes2_enabled = naes2_enabled

    @property
    def naes2_sids_any_or_specific(self):
        """Gets the naes2_sids_any_or_specific of this NielsenWatermarkDetectionTest.  # noqa: E501


        :return: The naes2_sids_any_or_specific of this NielsenWatermarkDetectionTest.  # noqa: E501
        :rtype: SidsAnyOrSpecific
        """
        return self._naes2_sids_any_or_specific

    @naes2_sids_any_or_specific.setter
    def naes2_sids_any_or_specific(self, naes2_sids_any_or_specific):
        """Sets the naes2_sids_any_or_specific of this NielsenWatermarkDetectionTest.


        :param naes2_sids_any_or_specific: The naes2_sids_any_or_specific of this NielsenWatermarkDetectionTest.  # noqa: E501
        :type: SidsAnyOrSpecific
        """

        self._naes2_sids_any_or_specific = naes2_sids_any_or_specific

    @property
    def naes2_sids(self):
        """Gets the naes2_sids of this NielsenWatermarkDetectionTest.  # noqa: E501


        :return: The naes2_sids of this NielsenWatermarkDetectionTest.  # noqa: E501
        :rtype: str
        """
        return self._naes2_sids

    @naes2_sids.setter
    def naes2_sids(self, naes2_sids):
        """Sets the naes2_sids of this NielsenWatermarkDetectionTest.


        :param naes2_sids: The naes2_sids of this NielsenWatermarkDetectionTest.  # noqa: E501
        :type: str
        """

        self._naes2_sids = naes2_sids

    @property
    def naes2_high_frequency_enabled(self):
        """Gets the naes2_high_frequency_enabled of this NielsenWatermarkDetectionTest.  # noqa: E501


        :return: The naes2_high_frequency_enabled of this NielsenWatermarkDetectionTest.  # noqa: E501
        :rtype: bool
        """
        return self._naes2_high_frequency_enabled

    @naes2_high_frequency_enabled.setter
    def naes2_high_frequency_enabled(self, naes2_high_frequency_enabled):
        """Sets the naes2_high_frequency_enabled of this NielsenWatermarkDetectionTest.


        :param naes2_high_frequency_enabled: The naes2_high_frequency_enabled of this NielsenWatermarkDetectionTest.  # noqa: E501
        :type: bool
        """

        self._naes2_high_frequency_enabled = naes2_high_frequency_enabled

    @property
    def naes2_high_frequency_sids_any_or_specific(self):
        """Gets the naes2_high_frequency_sids_any_or_specific of this NielsenWatermarkDetectionTest.  # noqa: E501


        :return: The naes2_high_frequency_sids_any_or_specific of this NielsenWatermarkDetectionTest.  # noqa: E501
        :rtype: SidsAnyOrSpecific
        """
        return self._naes2_high_frequency_sids_any_or_specific

    @naes2_high_frequency_sids_any_or_specific.setter
    def naes2_high_frequency_sids_any_or_specific(self, naes2_high_frequency_sids_any_or_specific):
        """Sets the naes2_high_frequency_sids_any_or_specific of this NielsenWatermarkDetectionTest.


        :param naes2_high_frequency_sids_any_or_specific: The naes2_high_frequency_sids_any_or_specific of this NielsenWatermarkDetectionTest.  # noqa: E501
        :type: SidsAnyOrSpecific
        """

        self._naes2_high_frequency_sids_any_or_specific = naes2_high_frequency_sids_any_or_specific

    @property
    def naes2_high_frequency_sids(self):
        """Gets the naes2_high_frequency_sids of this NielsenWatermarkDetectionTest.  # noqa: E501


        :return: The naes2_high_frequency_sids of this NielsenWatermarkDetectionTest.  # noqa: E501
        :rtype: str
        """
        return self._naes2_high_frequency_sids

    @naes2_high_frequency_sids.setter
    def naes2_high_frequency_sids(self, naes2_high_frequency_sids):
        """Sets the naes2_high_frequency_sids of this NielsenWatermarkDetectionTest.


        :param naes2_high_frequency_sids: The naes2_high_frequency_sids of this NielsenWatermarkDetectionTest.  # noqa: E501
        :type: str
        """

        self._naes2_high_frequency_sids = naes2_high_frequency_sids

    @property
    def naes6_enabled(self):
        """Gets the naes6_enabled of this NielsenWatermarkDetectionTest.  # noqa: E501


        :return: The naes6_enabled of this NielsenWatermarkDetectionTest.  # noqa: E501
        :rtype: bool
        """
        return self._naes6_enabled

    @naes6_enabled.setter
    def naes6_enabled(self, naes6_enabled):
        """Sets the naes6_enabled of this NielsenWatermarkDetectionTest.


        :param naes6_enabled: The naes6_enabled of this NielsenWatermarkDetectionTest.  # noqa: E501
        :type: bool
        """

        self._naes6_enabled = naes6_enabled

    @property
    def naes6_sids_any_or_specific(self):
        """Gets the naes6_sids_any_or_specific of this NielsenWatermarkDetectionTest.  # noqa: E501


        :return: The naes6_sids_any_or_specific of this NielsenWatermarkDetectionTest.  # noqa: E501
        :rtype: SidsAnyOrSpecific
        """
        return self._naes6_sids_any_or_specific

    @naes6_sids_any_or_specific.setter
    def naes6_sids_any_or_specific(self, naes6_sids_any_or_specific):
        """Sets the naes6_sids_any_or_specific of this NielsenWatermarkDetectionTest.


        :param naes6_sids_any_or_specific: The naes6_sids_any_or_specific of this NielsenWatermarkDetectionTest.  # noqa: E501
        :type: SidsAnyOrSpecific
        """

        self._naes6_sids_any_or_specific = naes6_sids_any_or_specific

    @property
    def naes6_sids(self):
        """Gets the naes6_sids of this NielsenWatermarkDetectionTest.  # noqa: E501


        :return: The naes6_sids of this NielsenWatermarkDetectionTest.  # noqa: E501
        :rtype: str
        """
        return self._naes6_sids

    @naes6_sids.setter
    def naes6_sids(self, naes6_sids):
        """Sets the naes6_sids of this NielsenWatermarkDetectionTest.


        :param naes6_sids: The naes6_sids of this NielsenWatermarkDetectionTest.  # noqa: E501
        :type: str
        """

        self._naes6_sids = naes6_sids

    @property
    def channels(self):
        """Gets the channels of this NielsenWatermarkDetectionTest.  # noqa: E501


        :return: The channels of this NielsenWatermarkDetectionTest.  # noqa: E501
        :rtype: Channels
        """
        return self._channels

    @channels.setter
    def channels(self, channels):
        """Sets the channels of this NielsenWatermarkDetectionTest.


        :param channels: The channels of this NielsenWatermarkDetectionTest.  # noqa: E501
        :type: Channels
        """

        self._channels = channels

    @property
    def reject_on_error(self):
        """Gets the reject_on_error of this NielsenWatermarkDetectionTest.  # noqa: E501


        :return: The reject_on_error of this NielsenWatermarkDetectionTest.  # noqa: E501
        :rtype: bool
        """
        return self._reject_on_error

    @reject_on_error.setter
    def reject_on_error(self, reject_on_error):
        """Sets the reject_on_error of this NielsenWatermarkDetectionTest.


        :param reject_on_error: The reject_on_error of this NielsenWatermarkDetectionTest.  # noqa: E501
        :type: bool
        """

        self._reject_on_error = reject_on_error

    @property
    def checked(self):
        """Gets the checked of this NielsenWatermarkDetectionTest.  # noqa: E501


        :return: The checked of this NielsenWatermarkDetectionTest.  # noqa: E501
        :rtype: bool
        """
        return self._checked

    @checked.setter
    def checked(self, checked):
        """Sets the checked of this NielsenWatermarkDetectionTest.


        :param checked: The checked of this NielsenWatermarkDetectionTest.  # noqa: E501
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
        if not isinstance(other, NielsenWatermarkDetectionTest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, NielsenWatermarkDetectionTest):
            return True

        return self.to_dict() != other.to_dict()
