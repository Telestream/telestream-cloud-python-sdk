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


class VideoCodecType(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    allowed enum values
    """
    MPEG2 = "Mpeg2"
    H264 = "H264"
    VC1 = "Vc1"
    JPEG2000 = "Jpeg2000"
    DV25 = "Dv25"
    DVCPRO25 = "DvcPro25"
    DVCPRO50 = "DvcPro50"
    DVCPRO100 = "DvcPro100"
    PRORES = "ProRes"
    MJPEG = "Mjpeg"
    DNXHD = "Dnxhd"
    UNCOMPRESSEDRGB = "UncompressedRgb"
    UNCOMPRESSEDYUV = "UncompressedYuv"
    MPEG4 = "Mpeg4"
    HUFFYUV = "HuffYuv"
    AVIDMERIDIEN = "AvidMeridien"
    HEVC = "Hevc"
    CANOPUS = "Canopus"
    DNXHR = "Dnxhr"

    allowable_values = [MPEG2, H264, VC1, JPEG2000, DV25, DVCPRO25, DVCPRO50, DVCPRO100, PRORES, MJPEG, DNXHD, UNCOMPRESSEDRGB, UNCOMPRESSEDYUV, MPEG4, HUFFYUV, AVIDMERIDIEN, HEVC, CANOPUS, DNXHR]  # noqa: E501

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
    }

    attribute_map = {
    }

    def __init__(self, local_vars_configuration=None):  # noqa: E501
        """VideoCodecType - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration
        self.discriminator = None

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
        if not isinstance(other, VideoCodecType):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, VideoCodecType):
            return True

        return self.to_dict() != other.to_dict()