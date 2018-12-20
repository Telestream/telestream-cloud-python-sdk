# coding: utf-8

"""
    Qc API

    QC API  # noqa: E501

    OpenAPI spec version: 2.0.3
    Contact: cloudsupport@telestream.net
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class UploadSession(object):
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
        'id': 'str',
        'location': 'str',
        'parts': 'int',
        'part_size': 'int',
        'max_connections': 'int',
        'extra_files': 'object'
    }

    attribute_map = {
        'id': 'id',
        'location': 'location',
        'parts': 'parts',
        'part_size': 'part_size',
        'max_connections': 'max_connections',
        'extra_files': 'extra_files'
    }

    def __init__(self, id=None, location=None, parts=None, part_size=None, max_connections=None, extra_files=None):  # noqa: E501
        """UploadSession - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._location = None
        self._parts = None
        self._part_size = None
        self._max_connections = None
        self._extra_files = None
        self.discriminator = None

        self.id = id
        self.location = location
        if parts is not None:
            self.parts = parts
        if part_size is not None:
            self.part_size = part_size
        if max_connections is not None:
            self.max_connections = max_connections
        if extra_files is not None:
            self.extra_files = extra_files

    @property
    def id(self):
        """Gets the id of this UploadSession.  # noqa: E501

        An unique identifier of the UploadSession.  # noqa: E501

        :return: The id of this UploadSession.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this UploadSession.

        An unique identifier of the UploadSession.  # noqa: E501

        :param id: The id of this UploadSession.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def location(self):
        """Gets the location of this UploadSession.  # noqa: E501

        An URL to which chunks of the uploaded file should be sent  # noqa: E501

        :return: The location of this UploadSession.  # noqa: E501
        :rtype: str
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this UploadSession.

        An URL to which chunks of the uploaded file should be sent  # noqa: E501

        :param location: The location of this UploadSession.  # noqa: E501
        :type: str
        """
        if location is None:
            raise ValueError("Invalid value for `location`, must not be `None`")  # noqa: E501

        self._location = location

    @property
    def parts(self):
        """Gets the parts of this UploadSession.  # noqa: E501

        A number of chunks that are expected by the upstream.  # noqa: E501

        :return: The parts of this UploadSession.  # noqa: E501
        :rtype: int
        """
        return self._parts

    @parts.setter
    def parts(self, parts):
        """Sets the parts of this UploadSession.

        A number of chunks that are expected by the upstream.  # noqa: E501

        :param parts: The parts of this UploadSession.  # noqa: E501
        :type: int
        """

        self._parts = parts

    @property
    def part_size(self):
        """Gets the part_size of this UploadSession.  # noqa: E501

        An expected size of uploaded chunks.  # noqa: E501

        :return: The part_size of this UploadSession.  # noqa: E501
        :rtype: int
        """
        return self._part_size

    @part_size.setter
    def part_size(self, part_size):
        """Sets the part_size of this UploadSession.

        An expected size of uploaded chunks.  # noqa: E501

        :param part_size: The part_size of this UploadSession.  # noqa: E501
        :type: int
        """

        self._part_size = part_size

    @property
    def max_connections(self):
        """Gets the max_connections of this UploadSession.  # noqa: E501

        A maximum number of concurrent connections.  # noqa: E501

        :return: The max_connections of this UploadSession.  # noqa: E501
        :rtype: int
        """
        return self._max_connections

    @max_connections.setter
    def max_connections(self, max_connections):
        """Sets the max_connections of this UploadSession.

        A maximum number of concurrent connections.  # noqa: E501

        :param max_connections: The max_connections of this UploadSession.  # noqa: E501
        :type: int
        """

        self._max_connections = max_connections

    @property
    def extra_files(self):
        """Gets the extra_files of this UploadSession.  # noqa: E501

        An object containing additional files uploaded using the session.  # noqa: E501

        :return: The extra_files of this UploadSession.  # noqa: E501
        :rtype: object
        """
        return self._extra_files

    @extra_files.setter
    def extra_files(self, extra_files):
        """Sets the extra_files of this UploadSession.

        An object containing additional files uploaded using the session.  # noqa: E501

        :param extra_files: The extra_files of this UploadSession.  # noqa: E501
        :type: object
        """

        self._extra_files = extra_files

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
        if not isinstance(other, UploadSession):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
