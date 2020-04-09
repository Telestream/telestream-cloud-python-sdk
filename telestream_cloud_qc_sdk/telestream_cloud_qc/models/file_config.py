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


class FileConfig(object):
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
        'container_test': 'ContainerTest',
        'mxf_op_test': 'MxfOpTest',
        'video_codec_test': 'VideoCodecTest',
        'container_essence_consistency_test': 'ContainerEssenceConsistencyTest',
        'imf_conformance_test': 'ImfConformanceTest',
        'netflix_photon_test': 'NetflixPhotonTest',
        'sps_pps_test': 'SpsPpsTest',
        'mbaff_test': 'MbaffTest',
        'cabac_test': 'CabacTest',
        'enhanced_syntax_test': 'EnhancedSyntaxTest',
        'framesize_test': 'FramesizeTest',
        'chroma_subsampling_test': 'ChromaSubsamplingTest',
        'pixel_aspect_ratio_test': 'PixelAspectRatioTest',
        'frame_aspect_ratio_test': 'FrameAspectRatioTest',
        'clean_aperture_test': 'CleanApertureTest',
        'i_tunes_compatibility_test': 'ITunesCompatibilityTest',
        'single_sample_description_test': 'SingleSampleDescriptionTest',
        'framerate_test': 'FramerateTest',
        'video_bit_depth_test': 'VideoBitDepthTest',
        'video_bit_rate_mode_test': 'BitRateModeTest',
        'video_bitrate_test': 'VideoBitrateTest',
        'gop_length_test': 'GopLengthTest',
        'advanced_gop_length_test': 'AdvancedGopLengthTest',
        'buffer_size_test': 'BufferSizeTest',
        'closed_caps608_test': 'TextStreamTest',
        'closed_caps708_test': 'TextStreamTest',
        'dvb_subtitles_test': 'TextStreamTest',
        'teletext_test': 'TextStreamTest',
        'captions_test': 'CaptionsTest',
        'active_format_test': 'ActiveFormatTest',
        'file_bitrate_test': 'FileBitrateTest',
        'file_duration_test': 'FileDurationTest',
        'audio_tracks_test': 'AudioTracksTest',
        'use_start_timecode_test': 'UseStartTimecodeTest',
        'start_timecode_test': 'StartTimecodeTest',
        'dont_copy_av_delay_test': 'DontCopyAvDelayTest',
        'container_drop_frame_test': 'DropFrameTest',
        'video_drop_frame_test': 'DropFrameTest',
        'timecode_continuity_test': 'TimecodeContinuityTest'
    }

    attribute_map = {
        'container_test': 'container_test',
        'mxf_op_test': 'mxf_op_test',
        'video_codec_test': 'video_codec_test',
        'container_essence_consistency_test': 'container_essence_consistency_test',
        'imf_conformance_test': 'imf_conformance_test',
        'netflix_photon_test': 'netflix_photon_test',
        'sps_pps_test': 'sps_pps_test',
        'mbaff_test': 'mbaff_test',
        'cabac_test': 'cabac_test',
        'enhanced_syntax_test': 'enhanced_syntax_test',
        'framesize_test': 'framesize_test',
        'chroma_subsampling_test': 'chroma_subsampling_test',
        'pixel_aspect_ratio_test': 'pixel_aspect_ratio_test',
        'frame_aspect_ratio_test': 'frame_aspect_ratio_test',
        'clean_aperture_test': 'clean_aperture_test',
        'i_tunes_compatibility_test': 'i_tunes_compatibility_test',
        'single_sample_description_test': 'single_sample_description_test',
        'framerate_test': 'framerate_test',
        'video_bit_depth_test': 'video_bit_depth_test',
        'video_bit_rate_mode_test': 'video_bit_rate_mode_test',
        'video_bitrate_test': 'video_bitrate_test',
        'gop_length_test': 'gop_length_test',
        'advanced_gop_length_test': 'advanced_gop_length_test',
        'buffer_size_test': 'buffer_size_test',
        'closed_caps608_test': 'closed_caps608_test',
        'closed_caps708_test': 'closed_caps708_test',
        'dvb_subtitles_test': 'dvb_subtitles_test',
        'teletext_test': 'teletext_test',
        'captions_test': 'captions_test',
        'active_format_test': 'active_format_test',
        'file_bitrate_test': 'file_bitrate_test',
        'file_duration_test': 'file_duration_test',
        'audio_tracks_test': 'audio_tracks_test',
        'use_start_timecode_test': 'use_start_timecode_test',
        'start_timecode_test': 'start_timecode_test',
        'dont_copy_av_delay_test': 'dont_copy_av_delay_test',
        'container_drop_frame_test': 'container_drop_frame_test',
        'video_drop_frame_test': 'video_drop_frame_test',
        'timecode_continuity_test': 'timecode_continuity_test'
    }

    def __init__(self, container_test=None, mxf_op_test=None, video_codec_test=None, container_essence_consistency_test=None, imf_conformance_test=None, netflix_photon_test=None, sps_pps_test=None, mbaff_test=None, cabac_test=None, enhanced_syntax_test=None, framesize_test=None, chroma_subsampling_test=None, pixel_aspect_ratio_test=None, frame_aspect_ratio_test=None, clean_aperture_test=None, i_tunes_compatibility_test=None, single_sample_description_test=None, framerate_test=None, video_bit_depth_test=None, video_bit_rate_mode_test=None, video_bitrate_test=None, gop_length_test=None, advanced_gop_length_test=None, buffer_size_test=None, closed_caps608_test=None, closed_caps708_test=None, dvb_subtitles_test=None, teletext_test=None, captions_test=None, active_format_test=None, file_bitrate_test=None, file_duration_test=None, audio_tracks_test=None, use_start_timecode_test=None, start_timecode_test=None, dont_copy_av_delay_test=None, container_drop_frame_test=None, video_drop_frame_test=None, timecode_continuity_test=None, local_vars_configuration=None):  # noqa: E501
        """FileConfig - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._container_test = None
        self._mxf_op_test = None
        self._video_codec_test = None
        self._container_essence_consistency_test = None
        self._imf_conformance_test = None
        self._netflix_photon_test = None
        self._sps_pps_test = None
        self._mbaff_test = None
        self._cabac_test = None
        self._enhanced_syntax_test = None
        self._framesize_test = None
        self._chroma_subsampling_test = None
        self._pixel_aspect_ratio_test = None
        self._frame_aspect_ratio_test = None
        self._clean_aperture_test = None
        self._i_tunes_compatibility_test = None
        self._single_sample_description_test = None
        self._framerate_test = None
        self._video_bit_depth_test = None
        self._video_bit_rate_mode_test = None
        self._video_bitrate_test = None
        self._gop_length_test = None
        self._advanced_gop_length_test = None
        self._buffer_size_test = None
        self._closed_caps608_test = None
        self._closed_caps708_test = None
        self._dvb_subtitles_test = None
        self._teletext_test = None
        self._captions_test = None
        self._active_format_test = None
        self._file_bitrate_test = None
        self._file_duration_test = None
        self._audio_tracks_test = None
        self._use_start_timecode_test = None
        self._start_timecode_test = None
        self._dont_copy_av_delay_test = None
        self._container_drop_frame_test = None
        self._video_drop_frame_test = None
        self._timecode_continuity_test = None
        self.discriminator = None

        if container_test is not None:
            self.container_test = container_test
        if mxf_op_test is not None:
            self.mxf_op_test = mxf_op_test
        if video_codec_test is not None:
            self.video_codec_test = video_codec_test
        if container_essence_consistency_test is not None:
            self.container_essence_consistency_test = container_essence_consistency_test
        if imf_conformance_test is not None:
            self.imf_conformance_test = imf_conformance_test
        if netflix_photon_test is not None:
            self.netflix_photon_test = netflix_photon_test
        if sps_pps_test is not None:
            self.sps_pps_test = sps_pps_test
        if mbaff_test is not None:
            self.mbaff_test = mbaff_test
        if cabac_test is not None:
            self.cabac_test = cabac_test
        if enhanced_syntax_test is not None:
            self.enhanced_syntax_test = enhanced_syntax_test
        if framesize_test is not None:
            self.framesize_test = framesize_test
        if chroma_subsampling_test is not None:
            self.chroma_subsampling_test = chroma_subsampling_test
        if pixel_aspect_ratio_test is not None:
            self.pixel_aspect_ratio_test = pixel_aspect_ratio_test
        if frame_aspect_ratio_test is not None:
            self.frame_aspect_ratio_test = frame_aspect_ratio_test
        if clean_aperture_test is not None:
            self.clean_aperture_test = clean_aperture_test
        if i_tunes_compatibility_test is not None:
            self.i_tunes_compatibility_test = i_tunes_compatibility_test
        if single_sample_description_test is not None:
            self.single_sample_description_test = single_sample_description_test
        if framerate_test is not None:
            self.framerate_test = framerate_test
        if video_bit_depth_test is not None:
            self.video_bit_depth_test = video_bit_depth_test
        if video_bit_rate_mode_test is not None:
            self.video_bit_rate_mode_test = video_bit_rate_mode_test
        if video_bitrate_test is not None:
            self.video_bitrate_test = video_bitrate_test
        if gop_length_test is not None:
            self.gop_length_test = gop_length_test
        if advanced_gop_length_test is not None:
            self.advanced_gop_length_test = advanced_gop_length_test
        if buffer_size_test is not None:
            self.buffer_size_test = buffer_size_test
        if closed_caps608_test is not None:
            self.closed_caps608_test = closed_caps608_test
        if closed_caps708_test is not None:
            self.closed_caps708_test = closed_caps708_test
        if dvb_subtitles_test is not None:
            self.dvb_subtitles_test = dvb_subtitles_test
        if teletext_test is not None:
            self.teletext_test = teletext_test
        if captions_test is not None:
            self.captions_test = captions_test
        if active_format_test is not None:
            self.active_format_test = active_format_test
        if file_bitrate_test is not None:
            self.file_bitrate_test = file_bitrate_test
        if file_duration_test is not None:
            self.file_duration_test = file_duration_test
        if audio_tracks_test is not None:
            self.audio_tracks_test = audio_tracks_test
        if use_start_timecode_test is not None:
            self.use_start_timecode_test = use_start_timecode_test
        if start_timecode_test is not None:
            self.start_timecode_test = start_timecode_test
        if dont_copy_av_delay_test is not None:
            self.dont_copy_av_delay_test = dont_copy_av_delay_test
        if container_drop_frame_test is not None:
            self.container_drop_frame_test = container_drop_frame_test
        if video_drop_frame_test is not None:
            self.video_drop_frame_test = video_drop_frame_test
        if timecode_continuity_test is not None:
            self.timecode_continuity_test = timecode_continuity_test

    @property
    def container_test(self):
        """Gets the container_test of this FileConfig.  # noqa: E501


        :return: The container_test of this FileConfig.  # noqa: E501
        :rtype: ContainerTest
        """
        return self._container_test

    @container_test.setter
    def container_test(self, container_test):
        """Sets the container_test of this FileConfig.


        :param container_test: The container_test of this FileConfig.  # noqa: E501
        :type: ContainerTest
        """

        self._container_test = container_test

    @property
    def mxf_op_test(self):
        """Gets the mxf_op_test of this FileConfig.  # noqa: E501


        :return: The mxf_op_test of this FileConfig.  # noqa: E501
        :rtype: MxfOpTest
        """
        return self._mxf_op_test

    @mxf_op_test.setter
    def mxf_op_test(self, mxf_op_test):
        """Sets the mxf_op_test of this FileConfig.


        :param mxf_op_test: The mxf_op_test of this FileConfig.  # noqa: E501
        :type: MxfOpTest
        """

        self._mxf_op_test = mxf_op_test

    @property
    def video_codec_test(self):
        """Gets the video_codec_test of this FileConfig.  # noqa: E501


        :return: The video_codec_test of this FileConfig.  # noqa: E501
        :rtype: VideoCodecTest
        """
        return self._video_codec_test

    @video_codec_test.setter
    def video_codec_test(self, video_codec_test):
        """Sets the video_codec_test of this FileConfig.


        :param video_codec_test: The video_codec_test of this FileConfig.  # noqa: E501
        :type: VideoCodecTest
        """

        self._video_codec_test = video_codec_test

    @property
    def container_essence_consistency_test(self):
        """Gets the container_essence_consistency_test of this FileConfig.  # noqa: E501


        :return: The container_essence_consistency_test of this FileConfig.  # noqa: E501
        :rtype: ContainerEssenceConsistencyTest
        """
        return self._container_essence_consistency_test

    @container_essence_consistency_test.setter
    def container_essence_consistency_test(self, container_essence_consistency_test):
        """Sets the container_essence_consistency_test of this FileConfig.


        :param container_essence_consistency_test: The container_essence_consistency_test of this FileConfig.  # noqa: E501
        :type: ContainerEssenceConsistencyTest
        """

        self._container_essence_consistency_test = container_essence_consistency_test

    @property
    def imf_conformance_test(self):
        """Gets the imf_conformance_test of this FileConfig.  # noqa: E501


        :return: The imf_conformance_test of this FileConfig.  # noqa: E501
        :rtype: ImfConformanceTest
        """
        return self._imf_conformance_test

    @imf_conformance_test.setter
    def imf_conformance_test(self, imf_conformance_test):
        """Sets the imf_conformance_test of this FileConfig.


        :param imf_conformance_test: The imf_conformance_test of this FileConfig.  # noqa: E501
        :type: ImfConformanceTest
        """

        self._imf_conformance_test = imf_conformance_test

    @property
    def netflix_photon_test(self):
        """Gets the netflix_photon_test of this FileConfig.  # noqa: E501


        :return: The netflix_photon_test of this FileConfig.  # noqa: E501
        :rtype: NetflixPhotonTest
        """
        return self._netflix_photon_test

    @netflix_photon_test.setter
    def netflix_photon_test(self, netflix_photon_test):
        """Sets the netflix_photon_test of this FileConfig.


        :param netflix_photon_test: The netflix_photon_test of this FileConfig.  # noqa: E501
        :type: NetflixPhotonTest
        """

        self._netflix_photon_test = netflix_photon_test

    @property
    def sps_pps_test(self):
        """Gets the sps_pps_test of this FileConfig.  # noqa: E501


        :return: The sps_pps_test of this FileConfig.  # noqa: E501
        :rtype: SpsPpsTest
        """
        return self._sps_pps_test

    @sps_pps_test.setter
    def sps_pps_test(self, sps_pps_test):
        """Sets the sps_pps_test of this FileConfig.


        :param sps_pps_test: The sps_pps_test of this FileConfig.  # noqa: E501
        :type: SpsPpsTest
        """

        self._sps_pps_test = sps_pps_test

    @property
    def mbaff_test(self):
        """Gets the mbaff_test of this FileConfig.  # noqa: E501


        :return: The mbaff_test of this FileConfig.  # noqa: E501
        :rtype: MbaffTest
        """
        return self._mbaff_test

    @mbaff_test.setter
    def mbaff_test(self, mbaff_test):
        """Sets the mbaff_test of this FileConfig.


        :param mbaff_test: The mbaff_test of this FileConfig.  # noqa: E501
        :type: MbaffTest
        """

        self._mbaff_test = mbaff_test

    @property
    def cabac_test(self):
        """Gets the cabac_test of this FileConfig.  # noqa: E501


        :return: The cabac_test of this FileConfig.  # noqa: E501
        :rtype: CabacTest
        """
        return self._cabac_test

    @cabac_test.setter
    def cabac_test(self, cabac_test):
        """Sets the cabac_test of this FileConfig.


        :param cabac_test: The cabac_test of this FileConfig.  # noqa: E501
        :type: CabacTest
        """

        self._cabac_test = cabac_test

    @property
    def enhanced_syntax_test(self):
        """Gets the enhanced_syntax_test of this FileConfig.  # noqa: E501


        :return: The enhanced_syntax_test of this FileConfig.  # noqa: E501
        :rtype: EnhancedSyntaxTest
        """
        return self._enhanced_syntax_test

    @enhanced_syntax_test.setter
    def enhanced_syntax_test(self, enhanced_syntax_test):
        """Sets the enhanced_syntax_test of this FileConfig.


        :param enhanced_syntax_test: The enhanced_syntax_test of this FileConfig.  # noqa: E501
        :type: EnhancedSyntaxTest
        """

        self._enhanced_syntax_test = enhanced_syntax_test

    @property
    def framesize_test(self):
        """Gets the framesize_test of this FileConfig.  # noqa: E501


        :return: The framesize_test of this FileConfig.  # noqa: E501
        :rtype: FramesizeTest
        """
        return self._framesize_test

    @framesize_test.setter
    def framesize_test(self, framesize_test):
        """Sets the framesize_test of this FileConfig.


        :param framesize_test: The framesize_test of this FileConfig.  # noqa: E501
        :type: FramesizeTest
        """

        self._framesize_test = framesize_test

    @property
    def chroma_subsampling_test(self):
        """Gets the chroma_subsampling_test of this FileConfig.  # noqa: E501


        :return: The chroma_subsampling_test of this FileConfig.  # noqa: E501
        :rtype: ChromaSubsamplingTest
        """
        return self._chroma_subsampling_test

    @chroma_subsampling_test.setter
    def chroma_subsampling_test(self, chroma_subsampling_test):
        """Sets the chroma_subsampling_test of this FileConfig.


        :param chroma_subsampling_test: The chroma_subsampling_test of this FileConfig.  # noqa: E501
        :type: ChromaSubsamplingTest
        """

        self._chroma_subsampling_test = chroma_subsampling_test

    @property
    def pixel_aspect_ratio_test(self):
        """Gets the pixel_aspect_ratio_test of this FileConfig.  # noqa: E501


        :return: The pixel_aspect_ratio_test of this FileConfig.  # noqa: E501
        :rtype: PixelAspectRatioTest
        """
        return self._pixel_aspect_ratio_test

    @pixel_aspect_ratio_test.setter
    def pixel_aspect_ratio_test(self, pixel_aspect_ratio_test):
        """Sets the pixel_aspect_ratio_test of this FileConfig.


        :param pixel_aspect_ratio_test: The pixel_aspect_ratio_test of this FileConfig.  # noqa: E501
        :type: PixelAspectRatioTest
        """

        self._pixel_aspect_ratio_test = pixel_aspect_ratio_test

    @property
    def frame_aspect_ratio_test(self):
        """Gets the frame_aspect_ratio_test of this FileConfig.  # noqa: E501


        :return: The frame_aspect_ratio_test of this FileConfig.  # noqa: E501
        :rtype: FrameAspectRatioTest
        """
        return self._frame_aspect_ratio_test

    @frame_aspect_ratio_test.setter
    def frame_aspect_ratio_test(self, frame_aspect_ratio_test):
        """Sets the frame_aspect_ratio_test of this FileConfig.


        :param frame_aspect_ratio_test: The frame_aspect_ratio_test of this FileConfig.  # noqa: E501
        :type: FrameAspectRatioTest
        """

        self._frame_aspect_ratio_test = frame_aspect_ratio_test

    @property
    def clean_aperture_test(self):
        """Gets the clean_aperture_test of this FileConfig.  # noqa: E501


        :return: The clean_aperture_test of this FileConfig.  # noqa: E501
        :rtype: CleanApertureTest
        """
        return self._clean_aperture_test

    @clean_aperture_test.setter
    def clean_aperture_test(self, clean_aperture_test):
        """Sets the clean_aperture_test of this FileConfig.


        :param clean_aperture_test: The clean_aperture_test of this FileConfig.  # noqa: E501
        :type: CleanApertureTest
        """

        self._clean_aperture_test = clean_aperture_test

    @property
    def i_tunes_compatibility_test(self):
        """Gets the i_tunes_compatibility_test of this FileConfig.  # noqa: E501


        :return: The i_tunes_compatibility_test of this FileConfig.  # noqa: E501
        :rtype: ITunesCompatibilityTest
        """
        return self._i_tunes_compatibility_test

    @i_tunes_compatibility_test.setter
    def i_tunes_compatibility_test(self, i_tunes_compatibility_test):
        """Sets the i_tunes_compatibility_test of this FileConfig.


        :param i_tunes_compatibility_test: The i_tunes_compatibility_test of this FileConfig.  # noqa: E501
        :type: ITunesCompatibilityTest
        """

        self._i_tunes_compatibility_test = i_tunes_compatibility_test

    @property
    def single_sample_description_test(self):
        """Gets the single_sample_description_test of this FileConfig.  # noqa: E501


        :return: The single_sample_description_test of this FileConfig.  # noqa: E501
        :rtype: SingleSampleDescriptionTest
        """
        return self._single_sample_description_test

    @single_sample_description_test.setter
    def single_sample_description_test(self, single_sample_description_test):
        """Sets the single_sample_description_test of this FileConfig.


        :param single_sample_description_test: The single_sample_description_test of this FileConfig.  # noqa: E501
        :type: SingleSampleDescriptionTest
        """

        self._single_sample_description_test = single_sample_description_test

    @property
    def framerate_test(self):
        """Gets the framerate_test of this FileConfig.  # noqa: E501


        :return: The framerate_test of this FileConfig.  # noqa: E501
        :rtype: FramerateTest
        """
        return self._framerate_test

    @framerate_test.setter
    def framerate_test(self, framerate_test):
        """Sets the framerate_test of this FileConfig.


        :param framerate_test: The framerate_test of this FileConfig.  # noqa: E501
        :type: FramerateTest
        """

        self._framerate_test = framerate_test

    @property
    def video_bit_depth_test(self):
        """Gets the video_bit_depth_test of this FileConfig.  # noqa: E501


        :return: The video_bit_depth_test of this FileConfig.  # noqa: E501
        :rtype: VideoBitDepthTest
        """
        return self._video_bit_depth_test

    @video_bit_depth_test.setter
    def video_bit_depth_test(self, video_bit_depth_test):
        """Sets the video_bit_depth_test of this FileConfig.


        :param video_bit_depth_test: The video_bit_depth_test of this FileConfig.  # noqa: E501
        :type: VideoBitDepthTest
        """

        self._video_bit_depth_test = video_bit_depth_test

    @property
    def video_bit_rate_mode_test(self):
        """Gets the video_bit_rate_mode_test of this FileConfig.  # noqa: E501


        :return: The video_bit_rate_mode_test of this FileConfig.  # noqa: E501
        :rtype: BitRateModeTest
        """
        return self._video_bit_rate_mode_test

    @video_bit_rate_mode_test.setter
    def video_bit_rate_mode_test(self, video_bit_rate_mode_test):
        """Sets the video_bit_rate_mode_test of this FileConfig.


        :param video_bit_rate_mode_test: The video_bit_rate_mode_test of this FileConfig.  # noqa: E501
        :type: BitRateModeTest
        """

        self._video_bit_rate_mode_test = video_bit_rate_mode_test

    @property
    def video_bitrate_test(self):
        """Gets the video_bitrate_test of this FileConfig.  # noqa: E501


        :return: The video_bitrate_test of this FileConfig.  # noqa: E501
        :rtype: VideoBitrateTest
        """
        return self._video_bitrate_test

    @video_bitrate_test.setter
    def video_bitrate_test(self, video_bitrate_test):
        """Sets the video_bitrate_test of this FileConfig.


        :param video_bitrate_test: The video_bitrate_test of this FileConfig.  # noqa: E501
        :type: VideoBitrateTest
        """

        self._video_bitrate_test = video_bitrate_test

    @property
    def gop_length_test(self):
        """Gets the gop_length_test of this FileConfig.  # noqa: E501


        :return: The gop_length_test of this FileConfig.  # noqa: E501
        :rtype: GopLengthTest
        """
        return self._gop_length_test

    @gop_length_test.setter
    def gop_length_test(self, gop_length_test):
        """Sets the gop_length_test of this FileConfig.


        :param gop_length_test: The gop_length_test of this FileConfig.  # noqa: E501
        :type: GopLengthTest
        """

        self._gop_length_test = gop_length_test

    @property
    def advanced_gop_length_test(self):
        """Gets the advanced_gop_length_test of this FileConfig.  # noqa: E501


        :return: The advanced_gop_length_test of this FileConfig.  # noqa: E501
        :rtype: AdvancedGopLengthTest
        """
        return self._advanced_gop_length_test

    @advanced_gop_length_test.setter
    def advanced_gop_length_test(self, advanced_gop_length_test):
        """Sets the advanced_gop_length_test of this FileConfig.


        :param advanced_gop_length_test: The advanced_gop_length_test of this FileConfig.  # noqa: E501
        :type: AdvancedGopLengthTest
        """

        self._advanced_gop_length_test = advanced_gop_length_test

    @property
    def buffer_size_test(self):
        """Gets the buffer_size_test of this FileConfig.  # noqa: E501


        :return: The buffer_size_test of this FileConfig.  # noqa: E501
        :rtype: BufferSizeTest
        """
        return self._buffer_size_test

    @buffer_size_test.setter
    def buffer_size_test(self, buffer_size_test):
        """Sets the buffer_size_test of this FileConfig.


        :param buffer_size_test: The buffer_size_test of this FileConfig.  # noqa: E501
        :type: BufferSizeTest
        """

        self._buffer_size_test = buffer_size_test

    @property
    def closed_caps608_test(self):
        """Gets the closed_caps608_test of this FileConfig.  # noqa: E501


        :return: The closed_caps608_test of this FileConfig.  # noqa: E501
        :rtype: TextStreamTest
        """
        return self._closed_caps608_test

    @closed_caps608_test.setter
    def closed_caps608_test(self, closed_caps608_test):
        """Sets the closed_caps608_test of this FileConfig.


        :param closed_caps608_test: The closed_caps608_test of this FileConfig.  # noqa: E501
        :type: TextStreamTest
        """

        self._closed_caps608_test = closed_caps608_test

    @property
    def closed_caps708_test(self):
        """Gets the closed_caps708_test of this FileConfig.  # noqa: E501


        :return: The closed_caps708_test of this FileConfig.  # noqa: E501
        :rtype: TextStreamTest
        """
        return self._closed_caps708_test

    @closed_caps708_test.setter
    def closed_caps708_test(self, closed_caps708_test):
        """Sets the closed_caps708_test of this FileConfig.


        :param closed_caps708_test: The closed_caps708_test of this FileConfig.  # noqa: E501
        :type: TextStreamTest
        """

        self._closed_caps708_test = closed_caps708_test

    @property
    def dvb_subtitles_test(self):
        """Gets the dvb_subtitles_test of this FileConfig.  # noqa: E501


        :return: The dvb_subtitles_test of this FileConfig.  # noqa: E501
        :rtype: TextStreamTest
        """
        return self._dvb_subtitles_test

    @dvb_subtitles_test.setter
    def dvb_subtitles_test(self, dvb_subtitles_test):
        """Sets the dvb_subtitles_test of this FileConfig.


        :param dvb_subtitles_test: The dvb_subtitles_test of this FileConfig.  # noqa: E501
        :type: TextStreamTest
        """

        self._dvb_subtitles_test = dvb_subtitles_test

    @property
    def teletext_test(self):
        """Gets the teletext_test of this FileConfig.  # noqa: E501


        :return: The teletext_test of this FileConfig.  # noqa: E501
        :rtype: TextStreamTest
        """
        return self._teletext_test

    @teletext_test.setter
    def teletext_test(self, teletext_test):
        """Sets the teletext_test of this FileConfig.


        :param teletext_test: The teletext_test of this FileConfig.  # noqa: E501
        :type: TextStreamTest
        """

        self._teletext_test = teletext_test

    @property
    def captions_test(self):
        """Gets the captions_test of this FileConfig.  # noqa: E501


        :return: The captions_test of this FileConfig.  # noqa: E501
        :rtype: CaptionsTest
        """
        return self._captions_test

    @captions_test.setter
    def captions_test(self, captions_test):
        """Sets the captions_test of this FileConfig.


        :param captions_test: The captions_test of this FileConfig.  # noqa: E501
        :type: CaptionsTest
        """

        self._captions_test = captions_test

    @property
    def active_format_test(self):
        """Gets the active_format_test of this FileConfig.  # noqa: E501


        :return: The active_format_test of this FileConfig.  # noqa: E501
        :rtype: ActiveFormatTest
        """
        return self._active_format_test

    @active_format_test.setter
    def active_format_test(self, active_format_test):
        """Sets the active_format_test of this FileConfig.


        :param active_format_test: The active_format_test of this FileConfig.  # noqa: E501
        :type: ActiveFormatTest
        """

        self._active_format_test = active_format_test

    @property
    def file_bitrate_test(self):
        """Gets the file_bitrate_test of this FileConfig.  # noqa: E501


        :return: The file_bitrate_test of this FileConfig.  # noqa: E501
        :rtype: FileBitrateTest
        """
        return self._file_bitrate_test

    @file_bitrate_test.setter
    def file_bitrate_test(self, file_bitrate_test):
        """Sets the file_bitrate_test of this FileConfig.


        :param file_bitrate_test: The file_bitrate_test of this FileConfig.  # noqa: E501
        :type: FileBitrateTest
        """

        self._file_bitrate_test = file_bitrate_test

    @property
    def file_duration_test(self):
        """Gets the file_duration_test of this FileConfig.  # noqa: E501


        :return: The file_duration_test of this FileConfig.  # noqa: E501
        :rtype: FileDurationTest
        """
        return self._file_duration_test

    @file_duration_test.setter
    def file_duration_test(self, file_duration_test):
        """Sets the file_duration_test of this FileConfig.


        :param file_duration_test: The file_duration_test of this FileConfig.  # noqa: E501
        :type: FileDurationTest
        """

        self._file_duration_test = file_duration_test

    @property
    def audio_tracks_test(self):
        """Gets the audio_tracks_test of this FileConfig.  # noqa: E501


        :return: The audio_tracks_test of this FileConfig.  # noqa: E501
        :rtype: AudioTracksTest
        """
        return self._audio_tracks_test

    @audio_tracks_test.setter
    def audio_tracks_test(self, audio_tracks_test):
        """Sets the audio_tracks_test of this FileConfig.


        :param audio_tracks_test: The audio_tracks_test of this FileConfig.  # noqa: E501
        :type: AudioTracksTest
        """

        self._audio_tracks_test = audio_tracks_test

    @property
    def use_start_timecode_test(self):
        """Gets the use_start_timecode_test of this FileConfig.  # noqa: E501


        :return: The use_start_timecode_test of this FileConfig.  # noqa: E501
        :rtype: UseStartTimecodeTest
        """
        return self._use_start_timecode_test

    @use_start_timecode_test.setter
    def use_start_timecode_test(self, use_start_timecode_test):
        """Sets the use_start_timecode_test of this FileConfig.


        :param use_start_timecode_test: The use_start_timecode_test of this FileConfig.  # noqa: E501
        :type: UseStartTimecodeTest
        """

        self._use_start_timecode_test = use_start_timecode_test

    @property
    def start_timecode_test(self):
        """Gets the start_timecode_test of this FileConfig.  # noqa: E501


        :return: The start_timecode_test of this FileConfig.  # noqa: E501
        :rtype: StartTimecodeTest
        """
        return self._start_timecode_test

    @start_timecode_test.setter
    def start_timecode_test(self, start_timecode_test):
        """Sets the start_timecode_test of this FileConfig.


        :param start_timecode_test: The start_timecode_test of this FileConfig.  # noqa: E501
        :type: StartTimecodeTest
        """

        self._start_timecode_test = start_timecode_test

    @property
    def dont_copy_av_delay_test(self):
        """Gets the dont_copy_av_delay_test of this FileConfig.  # noqa: E501


        :return: The dont_copy_av_delay_test of this FileConfig.  # noqa: E501
        :rtype: DontCopyAvDelayTest
        """
        return self._dont_copy_av_delay_test

    @dont_copy_av_delay_test.setter
    def dont_copy_av_delay_test(self, dont_copy_av_delay_test):
        """Sets the dont_copy_av_delay_test of this FileConfig.


        :param dont_copy_av_delay_test: The dont_copy_av_delay_test of this FileConfig.  # noqa: E501
        :type: DontCopyAvDelayTest
        """

        self._dont_copy_av_delay_test = dont_copy_av_delay_test

    @property
    def container_drop_frame_test(self):
        """Gets the container_drop_frame_test of this FileConfig.  # noqa: E501


        :return: The container_drop_frame_test of this FileConfig.  # noqa: E501
        :rtype: DropFrameTest
        """
        return self._container_drop_frame_test

    @container_drop_frame_test.setter
    def container_drop_frame_test(self, container_drop_frame_test):
        """Sets the container_drop_frame_test of this FileConfig.


        :param container_drop_frame_test: The container_drop_frame_test of this FileConfig.  # noqa: E501
        :type: DropFrameTest
        """

        self._container_drop_frame_test = container_drop_frame_test

    @property
    def video_drop_frame_test(self):
        """Gets the video_drop_frame_test of this FileConfig.  # noqa: E501


        :return: The video_drop_frame_test of this FileConfig.  # noqa: E501
        :rtype: DropFrameTest
        """
        return self._video_drop_frame_test

    @video_drop_frame_test.setter
    def video_drop_frame_test(self, video_drop_frame_test):
        """Sets the video_drop_frame_test of this FileConfig.


        :param video_drop_frame_test: The video_drop_frame_test of this FileConfig.  # noqa: E501
        :type: DropFrameTest
        """

        self._video_drop_frame_test = video_drop_frame_test

    @property
    def timecode_continuity_test(self):
        """Gets the timecode_continuity_test of this FileConfig.  # noqa: E501


        :return: The timecode_continuity_test of this FileConfig.  # noqa: E501
        :rtype: TimecodeContinuityTest
        """
        return self._timecode_continuity_test

    @timecode_continuity_test.setter
    def timecode_continuity_test(self, timecode_continuity_test):
        """Sets the timecode_continuity_test of this FileConfig.


        :param timecode_continuity_test: The timecode_continuity_test of this FileConfig.  # noqa: E501
        :type: TimecodeContinuityTest
        """

        self._timecode_continuity_test = timecode_continuity_test

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
        if not isinstance(other, FileConfig):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, FileConfig):
            return True

        return self.to_dict() != other.to_dict()