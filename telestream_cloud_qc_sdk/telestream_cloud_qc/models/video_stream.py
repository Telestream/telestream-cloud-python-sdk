# coding: utf-8

"""
    Qc API

    QC API  # noqa: E501

    OpenAPI spec version: 2.0.2
    Contact: cloudsupport@telestream.net
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class VideoStream(object):
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
        'duration': 'float',
        'codec': 'str',
        'width': 'int',
        'height': 'int',
        'bitrate': 'int',
        'fps': 'float'
    }

    attribute_map = {
        'duration': 'duration',
        'codec': 'codec',
        'width': 'width',
        'height': 'height',
        'bitrate': 'bitrate',
        'fps': 'fps'
    }

    def __init__(self, duration=None, codec=None, width=None, height=None, bitrate=None, fps=None):  # noqa: E501
        """VideoStream - a model defined in Swagger"""  # noqa: E501

        self._duration = None
        self._codec = None
        self._width = None
        self._height = None
        self._bitrate = None
        self._fps = None
        self.discriminator = None

        if duration is not None:
            self.duration = duration
        if codec is not None:
            self.codec = codec
        if width is not None:
            self.width = width
        if height is not None:
            self.height = height
        if bitrate is not None:
            self.bitrate = bitrate
        if fps is not None:
            self.fps = fps

    @property
    def duration(self):
        """Gets the duration of this VideoStream.  # noqa: E501

        Video stream duration measured in seconds.  # noqa: E501

        :return: The duration of this VideoStream.  # noqa: E501
        :rtype: float
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this VideoStream.

        Video stream duration measured in seconds.  # noqa: E501

        :param duration: The duration of this VideoStream.  # noqa: E501
        :type: float
        """

        self._duration = duration

    @property
    def codec(self):
        """Gets the codec of this VideoStream.  # noqa: E501


        :return: The codec of this VideoStream.  # noqa: E501
        :rtype: str
        """
        return self._codec

    @codec.setter
    def codec(self, codec):
        """Sets the codec of this VideoStream.


        :param codec: The codec of this VideoStream.  # noqa: E501
        :type: str
        """

        self._codec = codec

    @property
    def width(self):
        """Gets the width of this VideoStream.  # noqa: E501


        :return: The width of this VideoStream.  # noqa: E501
        :rtype: int
        """
        return self._width

    @width.setter
    def width(self, width):
        """Sets the width of this VideoStream.


        :param width: The width of this VideoStream.  # noqa: E501
        :type: int
        """

        self._width = width

    @property
    def height(self):
        """Gets the height of this VideoStream.  # noqa: E501


        :return: The height of this VideoStream.  # noqa: E501
        :rtype: int
        """
        return self._height

    @height.setter
    def height(self, height):
        """Sets the height of this VideoStream.


        :param height: The height of this VideoStream.  # noqa: E501
        :type: int
        """

        self._height = height

    @property
    def bitrate(self):
        """Gets the bitrate of this VideoStream.  # noqa: E501

        Video stream bitrate measured in bps  # noqa: E501

        :return: The bitrate of this VideoStream.  # noqa: E501
        :rtype: int
        """
        return self._bitrate

    @bitrate.setter
    def bitrate(self, bitrate):
        """Sets the bitrate of this VideoStream.

        Video stream bitrate measured in bps  # noqa: E501

        :param bitrate: The bitrate of this VideoStream.  # noqa: E501
        :type: int
        """

        self._bitrate = bitrate

    @property
    def fps(self):
        """Gets the fps of this VideoStream.  # noqa: E501


        :return: The fps of this VideoStream.  # noqa: E501
        :rtype: float
        """
        return self._fps

    @fps.setter
    def fps(self, fps):
        """Sets the fps of this VideoStream.


        :param fps: The fps of this VideoStream.  # noqa: E501
        :type: float
        """

        self._fps = fps

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
        if not isinstance(other, VideoStream):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
