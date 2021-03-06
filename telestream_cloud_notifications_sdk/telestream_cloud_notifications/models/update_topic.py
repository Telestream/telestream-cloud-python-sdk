# coding: utf-8

"""
    Notifications API

    Notifications  # noqa: E501

    The version of the OpenAPI document: 2.1.0
    Contact: cloudsupport@telestream.net
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from telestream_cloud_notifications.configuration import Configuration


class UpdateTopic(object):
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
        'name': 'str',
        'event': 'str'
    }

    attribute_map = {
        'name': 'name',
        'event': 'event'
    }

    def __init__(self, name=None, event=None, local_vars_configuration=None):  # noqa: E501
        """UpdateTopic - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._event = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if event is not None:
            self.event = event

    @property
    def name(self):
        """Gets the name of this UpdateTopic.  # noqa: E501


        :return: The name of this UpdateTopic.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UpdateTopic.


        :param name: The name of this UpdateTopic.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def event(self):
        """Gets the event of this UpdateTopic.  # noqa: E501

        Name of the event; Quality Control (media-passed, media-error, media-warning, media-rejected, media-canceled, job-created, job-progress), Flip (video-created, video-encoded, encoding-complete, encoding-progress), Transcription (job-created, job-completed, job-error, job-progress)   # noqa: E501

        :return: The event of this UpdateTopic.  # noqa: E501
        :rtype: str
        """
        return self._event

    @event.setter
    def event(self, event):
        """Sets the event of this UpdateTopic.

        Name of the event; Quality Control (media-passed, media-error, media-warning, media-rejected, media-canceled, job-created, job-progress), Flip (video-created, video-encoded, encoding-complete, encoding-progress), Transcription (job-created, job-completed, job-error, job-progress)   # noqa: E501

        :param event: The event of this UpdateTopic.  # noqa: E501
        :type: str
        """

        self._event = event

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
        if not isinstance(other, UpdateTopic):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UpdateTopic):
            return True

        return self.to_dict() != other.to_dict()
