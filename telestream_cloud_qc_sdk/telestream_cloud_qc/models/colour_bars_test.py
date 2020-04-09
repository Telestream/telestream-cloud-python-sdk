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


class ColourBarsTest(object):
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
        'color_bar_standard': 'ColorBarStandardType',
        'tolerance': 'int',
        'time_range_enabled': 'bool',
        'start_time': 'float',
        'end_time': 'float',
        'range_tolerance': 'float',
        'time_secs_or_frames': 'SecsOrFramesType',
        'not_at_any_other_time': 'bool',
        'reject_on_error': 'bool',
        'do_correction': 'bool',
        'checked': 'bool'
    }

    attribute_map = {
        'color_bar_standard': 'color_bar_standard',
        'tolerance': 'tolerance',
        'time_range_enabled': 'time_range_enabled',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'range_tolerance': 'range_tolerance',
        'time_secs_or_frames': 'time_secs_or_frames',
        'not_at_any_other_time': 'not_at_any_other_time',
        'reject_on_error': 'reject_on_error',
        'do_correction': 'do_correction',
        'checked': 'checked'
    }

    def __init__(self, color_bar_standard=None, tolerance=None, time_range_enabled=None, start_time=None, end_time=None, range_tolerance=None, time_secs_or_frames=None, not_at_any_other_time=None, reject_on_error=None, do_correction=None, checked=None, local_vars_configuration=None):  # noqa: E501
        """ColourBarsTest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._color_bar_standard = None
        self._tolerance = None
        self._time_range_enabled = None
        self._start_time = None
        self._end_time = None
        self._range_tolerance = None
        self._time_secs_or_frames = None
        self._not_at_any_other_time = None
        self._reject_on_error = None
        self._do_correction = None
        self._checked = None
        self.discriminator = None

        if color_bar_standard is not None:
            self.color_bar_standard = color_bar_standard
        if tolerance is not None:
            self.tolerance = tolerance
        if time_range_enabled is not None:
            self.time_range_enabled = time_range_enabled
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if range_tolerance is not None:
            self.range_tolerance = range_tolerance
        if time_secs_or_frames is not None:
            self.time_secs_or_frames = time_secs_or_frames
        if not_at_any_other_time is not None:
            self.not_at_any_other_time = not_at_any_other_time
        if reject_on_error is not None:
            self.reject_on_error = reject_on_error
        if do_correction is not None:
            self.do_correction = do_correction
        if checked is not None:
            self.checked = checked

    @property
    def color_bar_standard(self):
        """Gets the color_bar_standard of this ColourBarsTest.  # noqa: E501


        :return: The color_bar_standard of this ColourBarsTest.  # noqa: E501
        :rtype: ColorBarStandardType
        """
        return self._color_bar_standard

    @color_bar_standard.setter
    def color_bar_standard(self, color_bar_standard):
        """Sets the color_bar_standard of this ColourBarsTest.


        :param color_bar_standard: The color_bar_standard of this ColourBarsTest.  # noqa: E501
        :type: ColorBarStandardType
        """

        self._color_bar_standard = color_bar_standard

    @property
    def tolerance(self):
        """Gets the tolerance of this ColourBarsTest.  # noqa: E501


        :return: The tolerance of this ColourBarsTest.  # noqa: E501
        :rtype: int
        """
        return self._tolerance

    @tolerance.setter
    def tolerance(self, tolerance):
        """Sets the tolerance of this ColourBarsTest.


        :param tolerance: The tolerance of this ColourBarsTest.  # noqa: E501
        :type: int
        """

        self._tolerance = tolerance

    @property
    def time_range_enabled(self):
        """Gets the time_range_enabled of this ColourBarsTest.  # noqa: E501


        :return: The time_range_enabled of this ColourBarsTest.  # noqa: E501
        :rtype: bool
        """
        return self._time_range_enabled

    @time_range_enabled.setter
    def time_range_enabled(self, time_range_enabled):
        """Sets the time_range_enabled of this ColourBarsTest.


        :param time_range_enabled: The time_range_enabled of this ColourBarsTest.  # noqa: E501
        :type: bool
        """

        self._time_range_enabled = time_range_enabled

    @property
    def start_time(self):
        """Gets the start_time of this ColourBarsTest.  # noqa: E501


        :return: The start_time of this ColourBarsTest.  # noqa: E501
        :rtype: float
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this ColourBarsTest.


        :param start_time: The start_time of this ColourBarsTest.  # noqa: E501
        :type: float
        """

        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this ColourBarsTest.  # noqa: E501


        :return: The end_time of this ColourBarsTest.  # noqa: E501
        :rtype: float
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this ColourBarsTest.


        :param end_time: The end_time of this ColourBarsTest.  # noqa: E501
        :type: float
        """

        self._end_time = end_time

    @property
    def range_tolerance(self):
        """Gets the range_tolerance of this ColourBarsTest.  # noqa: E501


        :return: The range_tolerance of this ColourBarsTest.  # noqa: E501
        :rtype: float
        """
        return self._range_tolerance

    @range_tolerance.setter
    def range_tolerance(self, range_tolerance):
        """Sets the range_tolerance of this ColourBarsTest.


        :param range_tolerance: The range_tolerance of this ColourBarsTest.  # noqa: E501
        :type: float
        """

        self._range_tolerance = range_tolerance

    @property
    def time_secs_or_frames(self):
        """Gets the time_secs_or_frames of this ColourBarsTest.  # noqa: E501


        :return: The time_secs_or_frames of this ColourBarsTest.  # noqa: E501
        :rtype: SecsOrFramesType
        """
        return self._time_secs_or_frames

    @time_secs_or_frames.setter
    def time_secs_or_frames(self, time_secs_or_frames):
        """Sets the time_secs_or_frames of this ColourBarsTest.


        :param time_secs_or_frames: The time_secs_or_frames of this ColourBarsTest.  # noqa: E501
        :type: SecsOrFramesType
        """

        self._time_secs_or_frames = time_secs_or_frames

    @property
    def not_at_any_other_time(self):
        """Gets the not_at_any_other_time of this ColourBarsTest.  # noqa: E501


        :return: The not_at_any_other_time of this ColourBarsTest.  # noqa: E501
        :rtype: bool
        """
        return self._not_at_any_other_time

    @not_at_any_other_time.setter
    def not_at_any_other_time(self, not_at_any_other_time):
        """Sets the not_at_any_other_time of this ColourBarsTest.


        :param not_at_any_other_time: The not_at_any_other_time of this ColourBarsTest.  # noqa: E501
        :type: bool
        """

        self._not_at_any_other_time = not_at_any_other_time

    @property
    def reject_on_error(self):
        """Gets the reject_on_error of this ColourBarsTest.  # noqa: E501


        :return: The reject_on_error of this ColourBarsTest.  # noqa: E501
        :rtype: bool
        """
        return self._reject_on_error

    @reject_on_error.setter
    def reject_on_error(self, reject_on_error):
        """Sets the reject_on_error of this ColourBarsTest.


        :param reject_on_error: The reject_on_error of this ColourBarsTest.  # noqa: E501
        :type: bool
        """

        self._reject_on_error = reject_on_error

    @property
    def do_correction(self):
        """Gets the do_correction of this ColourBarsTest.  # noqa: E501


        :return: The do_correction of this ColourBarsTest.  # noqa: E501
        :rtype: bool
        """
        return self._do_correction

    @do_correction.setter
    def do_correction(self, do_correction):
        """Sets the do_correction of this ColourBarsTest.


        :param do_correction: The do_correction of this ColourBarsTest.  # noqa: E501
        :type: bool
        """

        self._do_correction = do_correction

    @property
    def checked(self):
        """Gets the checked of this ColourBarsTest.  # noqa: E501


        :return: The checked of this ColourBarsTest.  # noqa: E501
        :rtype: bool
        """
        return self._checked

    @checked.setter
    def checked(self, checked):
        """Sets the checked of this ColourBarsTest.


        :param checked: The checked of this ColourBarsTest.  # noqa: E501
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
        if not isinstance(other, ColourBarsTest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ColourBarsTest):
            return True

        return self.to_dict() != other.to_dict()