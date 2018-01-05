# coding: utf-8

"""
    Qc API

    QC API

    OpenAPI spec version: 1.0.0
    Contact: cloudsupport@telestream.net
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class Proxy(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
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
        'status': 'str',
        'progress': 'int',
        'url': 'str',
        'id': 'str',
        'updated_at': 'str'
    }

    attribute_map = {
        'status': 'status',
        'progress': 'progress',
        'url': 'url',
        'id': 'id',
        'updated_at': 'updated_at'
    }

    def __init__(self, status=None, progress=None, url=None, id=None, updated_at=None):
        """
        Proxy - a model defined in Swagger
        """

        self._status = None
        self._progress = None
        self._url = None
        self._id = None
        self._updated_at = None

        if status is not None:
          self.status = status
        if progress is not None:
          self.progress = progress
        if url is not None:
          self.url = url
        if id is not None:
          self.id = id
        if updated_at is not None:
          self.updated_at = updated_at

    @property
    def status(self):
        """
        Gets the status of this Proxy.

        :return: The status of this Proxy.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this Proxy.

        :param status: The status of this Proxy.
        :type: str
        """

        self._status = status

    @property
    def progress(self):
        """
        Gets the progress of this Proxy.

        :return: The progress of this Proxy.
        :rtype: int
        """
        return self._progress

    @progress.setter
    def progress(self, progress):
        """
        Sets the progress of this Proxy.

        :param progress: The progress of this Proxy.
        :type: int
        """

        self._progress = progress

    @property
    def url(self):
        """
        Gets the url of this Proxy.

        :return: The url of this Proxy.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """
        Sets the url of this Proxy.

        :param url: The url of this Proxy.
        :type: str
        """

        self._url = url

    @property
    def id(self):
        """
        Gets the id of this Proxy.

        :return: The id of this Proxy.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Proxy.

        :param id: The id of this Proxy.
        :type: str
        """

        self._id = id

    @property
    def updated_at(self):
        """
        Gets the updated_at of this Proxy.

        :return: The updated_at of this Proxy.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """
        Sets the updated_at of this Proxy.

        :param updated_at: The updated_at of this Proxy.
        :type: str
        """

        self._updated_at = updated_at

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, Proxy):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other