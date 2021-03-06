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


class Topic(object):
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
        'account': 'str',
        'service': 'str',
        'event': 'str',
        'project': 'str',
        'factory': 'str',
        'workflow': 'str'
    }

    attribute_map = {
        'account': 'account',
        'service': 'service',
        'event': 'event',
        'project': 'project',
        'factory': 'factory',
        'workflow': 'workflow'
    }

    def __init__(self, account=None, service=None, event=None, project=None, factory=None, workflow=None, local_vars_configuration=None):  # noqa: E501
        """Topic - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._account = None
        self._service = None
        self._event = None
        self._project = None
        self._factory = None
        self._workflow = None
        self.discriminator = None

        if account is not None:
            self.account = account
        self.service = service
        self.event = event
        if project is not None:
            self.project = project
        if factory is not None:
            self.factory = factory
        if workflow is not None:
            self.workflow = workflow

    @property
    def account(self):
        """Gets the account of this Topic.  # noqa: E501

        [read-only] Account identifier connected to subscription notification   # noqa: E501

        :return: The account of this Topic.  # noqa: E501
        :rtype: str
        """
        return self._account

    @account.setter
    def account(self, account):
        """Sets the account of this Topic.

        [read-only] Account identifier connected to subscription notification   # noqa: E501

        :param account: The account of this Topic.  # noqa: E501
        :type: str
        """

        self._account = account

    @property
    def service(self):
        """Gets the service of this Topic.  # noqa: E501

        Name of service (qc, flip, tts)   # noqa: E501

        :return: The service of this Topic.  # noqa: E501
        :rtype: str
        """
        return self._service

    @service.setter
    def service(self, service):
        """Sets the service of this Topic.

        Name of service (qc, flip, tts)   # noqa: E501

        :param service: The service of this Topic.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and service is None:  # noqa: E501
            raise ValueError("Invalid value for `service`, must not be `None`")  # noqa: E501

        self._service = service

    @property
    def event(self):
        """Gets the event of this Topic.  # noqa: E501

        Name of the event;  Quality Control (media-passed, media-error, media-warning, media-rejected, media-canceled, job-created, job-progress), Flip (video-created, video-encoded, encoding-complete, encoding-progress), Transcription (job-created, job-completed, job-error, job-progress)   # noqa: E501

        :return: The event of this Topic.  # noqa: E501
        :rtype: str
        """
        return self._event

    @event.setter
    def event(self, event):
        """Sets the event of this Topic.

        Name of the event;  Quality Control (media-passed, media-error, media-warning, media-rejected, media-canceled, job-created, job-progress), Flip (video-created, video-encoded, encoding-complete, encoding-progress), Transcription (job-created, job-completed, job-error, job-progress)   # noqa: E501

        :param event: The event of this Topic.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and event is None:  # noqa: E501
            raise ValueError("Invalid value for `event`, must not be `None`")  # noqa: E501

        self._event = event

    @property
    def project(self):
        """Gets the project of this Topic.  # noqa: E501

        (for tts, qc service); Project ID   # noqa: E501

        :return: The project of this Topic.  # noqa: E501
        :rtype: str
        """
        return self._project

    @project.setter
    def project(self, project):
        """Sets the project of this Topic.

        (for tts, qc service); Project ID   # noqa: E501

        :param project: The project of this Topic.  # noqa: E501
        :type: str
        """

        self._project = project

    @property
    def factory(self):
        """Gets the factory of this Topic.  # noqa: E501

        (for flip service); Factory ID   # noqa: E501

        :return: The factory of this Topic.  # noqa: E501
        :rtype: str
        """
        return self._factory

    @factory.setter
    def factory(self, factory):
        """Sets the factory of this Topic.

        (for flip service); Factory ID   # noqa: E501

        :param factory: The factory of this Topic.  # noqa: E501
        :type: str
        """

        self._factory = factory

    @property
    def workflow(self):
        """Gets the workflow of this Topic.  # noqa: E501

        (for Vantage Cloud Port service); Workflow ID   # noqa: E501

        :return: The workflow of this Topic.  # noqa: E501
        :rtype: str
        """
        return self._workflow

    @workflow.setter
    def workflow(self, workflow):
        """Sets the workflow of this Topic.

        (for Vantage Cloud Port service); Workflow ID   # noqa: E501

        :param workflow: The workflow of this Topic.  # noqa: E501
        :type: str
        """

        self._workflow = workflow

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
        if not isinstance(other, Topic):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Topic):
            return True

        return self.to_dict() != other.to_dict()
