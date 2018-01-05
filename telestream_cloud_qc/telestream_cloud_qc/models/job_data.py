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


class JobData(object):
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
        'options': 'Options',
        'url': 'str'
    }

    attribute_map = {
        'options': 'options',
        'url': 'url'
    }

    def __init__(self, options=None, url=None):
        """
        JobData - a model defined in Swagger
        """

        self._options = None
        self._url = None

        if options is not None:
          self.options = options
        if url is not None:
          self.url = url

    @property
    def options(self):
        """
        Gets the options of this JobData.

        :return: The options of this JobData.
        :rtype: Options
        """
        return self._options

    @options.setter
    def options(self, options):
        """
        Sets the options of this JobData.

        :param options: The options of this JobData.
        :type: Options
        """

        self._options = options

    @property
    def url(self):
        """
        Gets the url of this JobData.

        :return: The url of this JobData.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """
        Sets the url of this JobData.

        :param url: The url of this JobData.
        :type: str
        """

        self._url = url

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
        if not isinstance(other, JobData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other