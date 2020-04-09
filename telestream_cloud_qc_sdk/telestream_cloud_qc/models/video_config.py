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


class VideoConfig(object):
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
        'track_select_test': 'TrackSelectTest',
        'track_id_test': 'TrackIdTest',
        'ignore_vbi_test': 'IgnoreVbiTest',
        'force_color_space_test': 'ForceColorSpaceTest',
        'video_segment_detection_test': 'VideoSegmentDetectionTest',
        'video_layout_test': 'LayoutTest',
        'letterboxing_test': 'LetterboxingTest',
        'blanking_test': 'BlankingTest',
        'loss_of_chroma_test': 'LossOfChromaTest',
        'chroma_level_test': 'ChromaLevelTest',
        'black_level_test': 'BlackLevelTest',
        'rgb_gamut_test': 'RgbGamutTest',
        'hdr_test': 'HdrTest',
        'colour_bars_test': 'ColourBarsTest',
        'black_frame_test': 'BlackFrameTest',
        'single_color_test': 'SingleColorTest',
        'freeze_frame_test': 'FreezeFrameTest',
        'blockiness_test': 'BlockinessTest',
        'field_order_test': 'FieldOrderTest',
        'cadence_test': 'CadenceTest',
        'dropout_test': 'DropoutTest',
        'digital_dropout_test': 'DigitalDropoutTest',
        'stripe_test': 'StripeTest',
        'corrupt_frame_test': 'CorruptFrameTest',
        'flash_test': 'FlashTest',
        'media_offline_test': 'MediaOfflineTest'
    }

    attribute_map = {
        'track_select_test': 'track_select_test',
        'track_id_test': 'track_id_test',
        'ignore_vbi_test': 'ignore_vbi_test',
        'force_color_space_test': 'force_color_space_test',
        'video_segment_detection_test': 'video_segment_detection_test',
        'video_layout_test': 'video_layout_test',
        'letterboxing_test': 'letterboxing_test',
        'blanking_test': 'blanking_test',
        'loss_of_chroma_test': 'loss_of_chroma_test',
        'chroma_level_test': 'chroma_level_test',
        'black_level_test': 'black_level_test',
        'rgb_gamut_test': 'rgb_gamut_test',
        'hdr_test': 'hdr_test',
        'colour_bars_test': 'colour_bars_test',
        'black_frame_test': 'black_frame_test',
        'single_color_test': 'single_color_test',
        'freeze_frame_test': 'freeze_frame_test',
        'blockiness_test': 'blockiness_test',
        'field_order_test': 'field_order_test',
        'cadence_test': 'cadence_test',
        'dropout_test': 'dropout_test',
        'digital_dropout_test': 'digital_dropout_test',
        'stripe_test': 'stripe_test',
        'corrupt_frame_test': 'corrupt_frame_test',
        'flash_test': 'flash_test',
        'media_offline_test': 'media_offline_test'
    }

    def __init__(self, track_select_test=None, track_id_test=None, ignore_vbi_test=None, force_color_space_test=None, video_segment_detection_test=None, video_layout_test=None, letterboxing_test=None, blanking_test=None, loss_of_chroma_test=None, chroma_level_test=None, black_level_test=None, rgb_gamut_test=None, hdr_test=None, colour_bars_test=None, black_frame_test=None, single_color_test=None, freeze_frame_test=None, blockiness_test=None, field_order_test=None, cadence_test=None, dropout_test=None, digital_dropout_test=None, stripe_test=None, corrupt_frame_test=None, flash_test=None, media_offline_test=None, local_vars_configuration=None):  # noqa: E501
        """VideoConfig - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._track_select_test = None
        self._track_id_test = None
        self._ignore_vbi_test = None
        self._force_color_space_test = None
        self._video_segment_detection_test = None
        self._video_layout_test = None
        self._letterboxing_test = None
        self._blanking_test = None
        self._loss_of_chroma_test = None
        self._chroma_level_test = None
        self._black_level_test = None
        self._rgb_gamut_test = None
        self._hdr_test = None
        self._colour_bars_test = None
        self._black_frame_test = None
        self._single_color_test = None
        self._freeze_frame_test = None
        self._blockiness_test = None
        self._field_order_test = None
        self._cadence_test = None
        self._dropout_test = None
        self._digital_dropout_test = None
        self._stripe_test = None
        self._corrupt_frame_test = None
        self._flash_test = None
        self._media_offline_test = None
        self.discriminator = None

        if track_select_test is not None:
            self.track_select_test = track_select_test
        if track_id_test is not None:
            self.track_id_test = track_id_test
        if ignore_vbi_test is not None:
            self.ignore_vbi_test = ignore_vbi_test
        if force_color_space_test is not None:
            self.force_color_space_test = force_color_space_test
        if video_segment_detection_test is not None:
            self.video_segment_detection_test = video_segment_detection_test
        if video_layout_test is not None:
            self.video_layout_test = video_layout_test
        if letterboxing_test is not None:
            self.letterboxing_test = letterboxing_test
        if blanking_test is not None:
            self.blanking_test = blanking_test
        if loss_of_chroma_test is not None:
            self.loss_of_chroma_test = loss_of_chroma_test
        if chroma_level_test is not None:
            self.chroma_level_test = chroma_level_test
        if black_level_test is not None:
            self.black_level_test = black_level_test
        if rgb_gamut_test is not None:
            self.rgb_gamut_test = rgb_gamut_test
        if hdr_test is not None:
            self.hdr_test = hdr_test
        if colour_bars_test is not None:
            self.colour_bars_test = colour_bars_test
        if black_frame_test is not None:
            self.black_frame_test = black_frame_test
        if single_color_test is not None:
            self.single_color_test = single_color_test
        if freeze_frame_test is not None:
            self.freeze_frame_test = freeze_frame_test
        if blockiness_test is not None:
            self.blockiness_test = blockiness_test
        if field_order_test is not None:
            self.field_order_test = field_order_test
        if cadence_test is not None:
            self.cadence_test = cadence_test
        if dropout_test is not None:
            self.dropout_test = dropout_test
        if digital_dropout_test is not None:
            self.digital_dropout_test = digital_dropout_test
        if stripe_test is not None:
            self.stripe_test = stripe_test
        if corrupt_frame_test is not None:
            self.corrupt_frame_test = corrupt_frame_test
        if flash_test is not None:
            self.flash_test = flash_test
        if media_offline_test is not None:
            self.media_offline_test = media_offline_test

    @property
    def track_select_test(self):
        """Gets the track_select_test of this VideoConfig.  # noqa: E501


        :return: The track_select_test of this VideoConfig.  # noqa: E501
        :rtype: TrackSelectTest
        """
        return self._track_select_test

    @track_select_test.setter
    def track_select_test(self, track_select_test):
        """Sets the track_select_test of this VideoConfig.


        :param track_select_test: The track_select_test of this VideoConfig.  # noqa: E501
        :type: TrackSelectTest
        """

        self._track_select_test = track_select_test

    @property
    def track_id_test(self):
        """Gets the track_id_test of this VideoConfig.  # noqa: E501


        :return: The track_id_test of this VideoConfig.  # noqa: E501
        :rtype: TrackIdTest
        """
        return self._track_id_test

    @track_id_test.setter
    def track_id_test(self, track_id_test):
        """Sets the track_id_test of this VideoConfig.


        :param track_id_test: The track_id_test of this VideoConfig.  # noqa: E501
        :type: TrackIdTest
        """

        self._track_id_test = track_id_test

    @property
    def ignore_vbi_test(self):
        """Gets the ignore_vbi_test of this VideoConfig.  # noqa: E501


        :return: The ignore_vbi_test of this VideoConfig.  # noqa: E501
        :rtype: IgnoreVbiTest
        """
        return self._ignore_vbi_test

    @ignore_vbi_test.setter
    def ignore_vbi_test(self, ignore_vbi_test):
        """Sets the ignore_vbi_test of this VideoConfig.


        :param ignore_vbi_test: The ignore_vbi_test of this VideoConfig.  # noqa: E501
        :type: IgnoreVbiTest
        """

        self._ignore_vbi_test = ignore_vbi_test

    @property
    def force_color_space_test(self):
        """Gets the force_color_space_test of this VideoConfig.  # noqa: E501


        :return: The force_color_space_test of this VideoConfig.  # noqa: E501
        :rtype: ForceColorSpaceTest
        """
        return self._force_color_space_test

    @force_color_space_test.setter
    def force_color_space_test(self, force_color_space_test):
        """Sets the force_color_space_test of this VideoConfig.


        :param force_color_space_test: The force_color_space_test of this VideoConfig.  # noqa: E501
        :type: ForceColorSpaceTest
        """

        self._force_color_space_test = force_color_space_test

    @property
    def video_segment_detection_test(self):
        """Gets the video_segment_detection_test of this VideoConfig.  # noqa: E501


        :return: The video_segment_detection_test of this VideoConfig.  # noqa: E501
        :rtype: VideoSegmentDetectionTest
        """
        return self._video_segment_detection_test

    @video_segment_detection_test.setter
    def video_segment_detection_test(self, video_segment_detection_test):
        """Sets the video_segment_detection_test of this VideoConfig.


        :param video_segment_detection_test: The video_segment_detection_test of this VideoConfig.  # noqa: E501
        :type: VideoSegmentDetectionTest
        """

        self._video_segment_detection_test = video_segment_detection_test

    @property
    def video_layout_test(self):
        """Gets the video_layout_test of this VideoConfig.  # noqa: E501


        :return: The video_layout_test of this VideoConfig.  # noqa: E501
        :rtype: LayoutTest
        """
        return self._video_layout_test

    @video_layout_test.setter
    def video_layout_test(self, video_layout_test):
        """Sets the video_layout_test of this VideoConfig.


        :param video_layout_test: The video_layout_test of this VideoConfig.  # noqa: E501
        :type: LayoutTest
        """

        self._video_layout_test = video_layout_test

    @property
    def letterboxing_test(self):
        """Gets the letterboxing_test of this VideoConfig.  # noqa: E501


        :return: The letterboxing_test of this VideoConfig.  # noqa: E501
        :rtype: LetterboxingTest
        """
        return self._letterboxing_test

    @letterboxing_test.setter
    def letterboxing_test(self, letterboxing_test):
        """Sets the letterboxing_test of this VideoConfig.


        :param letterboxing_test: The letterboxing_test of this VideoConfig.  # noqa: E501
        :type: LetterboxingTest
        """

        self._letterboxing_test = letterboxing_test

    @property
    def blanking_test(self):
        """Gets the blanking_test of this VideoConfig.  # noqa: E501


        :return: The blanking_test of this VideoConfig.  # noqa: E501
        :rtype: BlankingTest
        """
        return self._blanking_test

    @blanking_test.setter
    def blanking_test(self, blanking_test):
        """Sets the blanking_test of this VideoConfig.


        :param blanking_test: The blanking_test of this VideoConfig.  # noqa: E501
        :type: BlankingTest
        """

        self._blanking_test = blanking_test

    @property
    def loss_of_chroma_test(self):
        """Gets the loss_of_chroma_test of this VideoConfig.  # noqa: E501


        :return: The loss_of_chroma_test of this VideoConfig.  # noqa: E501
        :rtype: LossOfChromaTest
        """
        return self._loss_of_chroma_test

    @loss_of_chroma_test.setter
    def loss_of_chroma_test(self, loss_of_chroma_test):
        """Sets the loss_of_chroma_test of this VideoConfig.


        :param loss_of_chroma_test: The loss_of_chroma_test of this VideoConfig.  # noqa: E501
        :type: LossOfChromaTest
        """

        self._loss_of_chroma_test = loss_of_chroma_test

    @property
    def chroma_level_test(self):
        """Gets the chroma_level_test of this VideoConfig.  # noqa: E501


        :return: The chroma_level_test of this VideoConfig.  # noqa: E501
        :rtype: ChromaLevelTest
        """
        return self._chroma_level_test

    @chroma_level_test.setter
    def chroma_level_test(self, chroma_level_test):
        """Sets the chroma_level_test of this VideoConfig.


        :param chroma_level_test: The chroma_level_test of this VideoConfig.  # noqa: E501
        :type: ChromaLevelTest
        """

        self._chroma_level_test = chroma_level_test

    @property
    def black_level_test(self):
        """Gets the black_level_test of this VideoConfig.  # noqa: E501


        :return: The black_level_test of this VideoConfig.  # noqa: E501
        :rtype: BlackLevelTest
        """
        return self._black_level_test

    @black_level_test.setter
    def black_level_test(self, black_level_test):
        """Sets the black_level_test of this VideoConfig.


        :param black_level_test: The black_level_test of this VideoConfig.  # noqa: E501
        :type: BlackLevelTest
        """

        self._black_level_test = black_level_test

    @property
    def rgb_gamut_test(self):
        """Gets the rgb_gamut_test of this VideoConfig.  # noqa: E501


        :return: The rgb_gamut_test of this VideoConfig.  # noqa: E501
        :rtype: RgbGamutTest
        """
        return self._rgb_gamut_test

    @rgb_gamut_test.setter
    def rgb_gamut_test(self, rgb_gamut_test):
        """Sets the rgb_gamut_test of this VideoConfig.


        :param rgb_gamut_test: The rgb_gamut_test of this VideoConfig.  # noqa: E501
        :type: RgbGamutTest
        """

        self._rgb_gamut_test = rgb_gamut_test

    @property
    def hdr_test(self):
        """Gets the hdr_test of this VideoConfig.  # noqa: E501


        :return: The hdr_test of this VideoConfig.  # noqa: E501
        :rtype: HdrTest
        """
        return self._hdr_test

    @hdr_test.setter
    def hdr_test(self, hdr_test):
        """Sets the hdr_test of this VideoConfig.


        :param hdr_test: The hdr_test of this VideoConfig.  # noqa: E501
        :type: HdrTest
        """

        self._hdr_test = hdr_test

    @property
    def colour_bars_test(self):
        """Gets the colour_bars_test of this VideoConfig.  # noqa: E501


        :return: The colour_bars_test of this VideoConfig.  # noqa: E501
        :rtype: ColourBarsTest
        """
        return self._colour_bars_test

    @colour_bars_test.setter
    def colour_bars_test(self, colour_bars_test):
        """Sets the colour_bars_test of this VideoConfig.


        :param colour_bars_test: The colour_bars_test of this VideoConfig.  # noqa: E501
        :type: ColourBarsTest
        """

        self._colour_bars_test = colour_bars_test

    @property
    def black_frame_test(self):
        """Gets the black_frame_test of this VideoConfig.  # noqa: E501


        :return: The black_frame_test of this VideoConfig.  # noqa: E501
        :rtype: BlackFrameTest
        """
        return self._black_frame_test

    @black_frame_test.setter
    def black_frame_test(self, black_frame_test):
        """Sets the black_frame_test of this VideoConfig.


        :param black_frame_test: The black_frame_test of this VideoConfig.  # noqa: E501
        :type: BlackFrameTest
        """

        self._black_frame_test = black_frame_test

    @property
    def single_color_test(self):
        """Gets the single_color_test of this VideoConfig.  # noqa: E501


        :return: The single_color_test of this VideoConfig.  # noqa: E501
        :rtype: SingleColorTest
        """
        return self._single_color_test

    @single_color_test.setter
    def single_color_test(self, single_color_test):
        """Sets the single_color_test of this VideoConfig.


        :param single_color_test: The single_color_test of this VideoConfig.  # noqa: E501
        :type: SingleColorTest
        """

        self._single_color_test = single_color_test

    @property
    def freeze_frame_test(self):
        """Gets the freeze_frame_test of this VideoConfig.  # noqa: E501


        :return: The freeze_frame_test of this VideoConfig.  # noqa: E501
        :rtype: FreezeFrameTest
        """
        return self._freeze_frame_test

    @freeze_frame_test.setter
    def freeze_frame_test(self, freeze_frame_test):
        """Sets the freeze_frame_test of this VideoConfig.


        :param freeze_frame_test: The freeze_frame_test of this VideoConfig.  # noqa: E501
        :type: FreezeFrameTest
        """

        self._freeze_frame_test = freeze_frame_test

    @property
    def blockiness_test(self):
        """Gets the blockiness_test of this VideoConfig.  # noqa: E501


        :return: The blockiness_test of this VideoConfig.  # noqa: E501
        :rtype: BlockinessTest
        """
        return self._blockiness_test

    @blockiness_test.setter
    def blockiness_test(self, blockiness_test):
        """Sets the blockiness_test of this VideoConfig.


        :param blockiness_test: The blockiness_test of this VideoConfig.  # noqa: E501
        :type: BlockinessTest
        """

        self._blockiness_test = blockiness_test

    @property
    def field_order_test(self):
        """Gets the field_order_test of this VideoConfig.  # noqa: E501


        :return: The field_order_test of this VideoConfig.  # noqa: E501
        :rtype: FieldOrderTest
        """
        return self._field_order_test

    @field_order_test.setter
    def field_order_test(self, field_order_test):
        """Sets the field_order_test of this VideoConfig.


        :param field_order_test: The field_order_test of this VideoConfig.  # noqa: E501
        :type: FieldOrderTest
        """

        self._field_order_test = field_order_test

    @property
    def cadence_test(self):
        """Gets the cadence_test of this VideoConfig.  # noqa: E501


        :return: The cadence_test of this VideoConfig.  # noqa: E501
        :rtype: CadenceTest
        """
        return self._cadence_test

    @cadence_test.setter
    def cadence_test(self, cadence_test):
        """Sets the cadence_test of this VideoConfig.


        :param cadence_test: The cadence_test of this VideoConfig.  # noqa: E501
        :type: CadenceTest
        """

        self._cadence_test = cadence_test

    @property
    def dropout_test(self):
        """Gets the dropout_test of this VideoConfig.  # noqa: E501


        :return: The dropout_test of this VideoConfig.  # noqa: E501
        :rtype: DropoutTest
        """
        return self._dropout_test

    @dropout_test.setter
    def dropout_test(self, dropout_test):
        """Sets the dropout_test of this VideoConfig.


        :param dropout_test: The dropout_test of this VideoConfig.  # noqa: E501
        :type: DropoutTest
        """

        self._dropout_test = dropout_test

    @property
    def digital_dropout_test(self):
        """Gets the digital_dropout_test of this VideoConfig.  # noqa: E501


        :return: The digital_dropout_test of this VideoConfig.  # noqa: E501
        :rtype: DigitalDropoutTest
        """
        return self._digital_dropout_test

    @digital_dropout_test.setter
    def digital_dropout_test(self, digital_dropout_test):
        """Sets the digital_dropout_test of this VideoConfig.


        :param digital_dropout_test: The digital_dropout_test of this VideoConfig.  # noqa: E501
        :type: DigitalDropoutTest
        """

        self._digital_dropout_test = digital_dropout_test

    @property
    def stripe_test(self):
        """Gets the stripe_test of this VideoConfig.  # noqa: E501


        :return: The stripe_test of this VideoConfig.  # noqa: E501
        :rtype: StripeTest
        """
        return self._stripe_test

    @stripe_test.setter
    def stripe_test(self, stripe_test):
        """Sets the stripe_test of this VideoConfig.


        :param stripe_test: The stripe_test of this VideoConfig.  # noqa: E501
        :type: StripeTest
        """

        self._stripe_test = stripe_test

    @property
    def corrupt_frame_test(self):
        """Gets the corrupt_frame_test of this VideoConfig.  # noqa: E501


        :return: The corrupt_frame_test of this VideoConfig.  # noqa: E501
        :rtype: CorruptFrameTest
        """
        return self._corrupt_frame_test

    @corrupt_frame_test.setter
    def corrupt_frame_test(self, corrupt_frame_test):
        """Sets the corrupt_frame_test of this VideoConfig.


        :param corrupt_frame_test: The corrupt_frame_test of this VideoConfig.  # noqa: E501
        :type: CorruptFrameTest
        """

        self._corrupt_frame_test = corrupt_frame_test

    @property
    def flash_test(self):
        """Gets the flash_test of this VideoConfig.  # noqa: E501


        :return: The flash_test of this VideoConfig.  # noqa: E501
        :rtype: FlashTest
        """
        return self._flash_test

    @flash_test.setter
    def flash_test(self, flash_test):
        """Sets the flash_test of this VideoConfig.


        :param flash_test: The flash_test of this VideoConfig.  # noqa: E501
        :type: FlashTest
        """

        self._flash_test = flash_test

    @property
    def media_offline_test(self):
        """Gets the media_offline_test of this VideoConfig.  # noqa: E501


        :return: The media_offline_test of this VideoConfig.  # noqa: E501
        :rtype: MediaOfflineTest
        """
        return self._media_offline_test

    @media_offline_test.setter
    def media_offline_test(self, media_offline_test):
        """Sets the media_offline_test of this VideoConfig.


        :param media_offline_test: The media_offline_test of this VideoConfig.  # noqa: E501
        :type: MediaOfflineTest
        """

        self._media_offline_test = media_offline_test

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
        if not isinstance(other, VideoConfig):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, VideoConfig):
            return True

        return self.to_dict() != other.to_dict()