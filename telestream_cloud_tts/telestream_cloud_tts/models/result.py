# coding: utf-8

"""
    Tts API

    Description  # noqa: E501

    OpenAPI spec version: 3.1.0
    Contact: cloudsupport@telestream.net
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from telestream_cloud_tts.models.fragment import Fragment  # noqa: F401,E501


class Result(object):
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
        'transcript': 'str',
        'start_time': 'float',
        'fragments': 'list[Fragment]',
        'end_time': 'float',
        'confidence': 'float'
    }

    attribute_map = {
        'transcript': 'transcript',
        'start_time': 'start_time',
        'fragments': 'fragments',
        'end_time': 'end_time',
        'confidence': 'confidence'
    }

    def __init__(self, transcript=None, start_time=None, fragments=None, end_time=None, confidence=None):  # noqa: E501
        """Result - a model defined in Swagger"""  # noqa: E501

        self._transcript = None
        self._start_time = None
        self._fragments = None
        self._end_time = None
        self._confidence = None
        self.discriminator = None

        if transcript is not None:
            self.transcript = transcript
        if start_time is not None:
            self.start_time = start_time
        if fragments is not None:
            self.fragments = fragments
        if end_time is not None:
            self.end_time = end_time
        if confidence is not None:
            self.confidence = confidence

    @property
    def transcript(self):
        """Gets the transcript of this Result.  # noqa: E501


        :return: The transcript of this Result.  # noqa: E501
        :rtype: str
        """
        return self._transcript

    @transcript.setter
    def transcript(self, transcript):
        """Sets the transcript of this Result.


        :param transcript: The transcript of this Result.  # noqa: E501
        :type: str
        """

        self._transcript = transcript

    @property
    def start_time(self):
        """Gets the start_time of this Result.  # noqa: E501

        The start time in seconds of the transcript from the input audio  # noqa: E501

        :return: The start_time of this Result.  # noqa: E501
        :rtype: float
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this Result.

        The start time in seconds of the transcript from the input audio  # noqa: E501

        :param start_time: The start_time of this Result.  # noqa: E501
        :type: float
        """

        self._start_time = start_time

    @property
    def fragments(self):
        """Gets the fragments of this Result.  # noqa: E501

        An array of Fragments  # noqa: E501

        :return: The fragments of this Result.  # noqa: E501
        :rtype: list[Fragment]
        """
        return self._fragments

    @fragments.setter
    def fragments(self, fragments):
        """Sets the fragments of this Result.

        An array of Fragments  # noqa: E501

        :param fragments: The fragments of this Result.  # noqa: E501
        :type: list[Fragment]
        """

        self._fragments = fragments

    @property
    def end_time(self):
        """Gets the end_time of this Result.  # noqa: E501

        The end time time in seconds of the transcript from the input audio  # noqa: E501

        :return: The end_time of this Result.  # noqa: E501
        :rtype: float
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this Result.

        The end time time in seconds of the transcript from the input audio  # noqa: E501

        :param end_time: The end_time of this Result.  # noqa: E501
        :type: float
        """

        self._end_time = end_time

    @property
    def confidence(self):
        """Gets the confidence of this Result.  # noqa: E501

        The confidence score of the result in the range of 0 to 1  # noqa: E501

        :return: The confidence of this Result.  # noqa: E501
        :rtype: float
        """
        return self._confidence

    @confidence.setter
    def confidence(self, confidence):
        """Sets the confidence of this Result.

        The confidence score of the result in the range of 0 to 1  # noqa: E501

        :param confidence: The confidence of this Result.  # noqa: E501
        :type: float
        """

        self._confidence = confidence

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
        if not isinstance(other, Result):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
