# coding: utf-8

"""
    Qc API

    Qc API  # noqa: E501

    The version of the OpenAPI document: 3.0.0
    Contact: cloudsupport@telestream.net
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import telestream_cloud_qc
from telestream_cloud_qc.models.video_config import VideoConfig  # noqa: E501
from telestream_cloud_qc.rest import ApiException

class TestVideoConfig(unittest.TestCase):
    """VideoConfig unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test VideoConfig
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = telestream_cloud_qc.models.video_config.VideoConfig()  # noqa: E501
        if include_optional :
            return VideoConfig(
                track_select_test = telestream_cloud_qc.models.track_select_test.track_select_test(
                    selector = 56, 
                    selector_type = 'TrackIndex', 
                    checked = True, ), 
                track_id_test = telestream_cloud_qc.models.track_id_test.track_id_test(
                    track_id = 56, 
                    reject_on_error = True, 
                    checked = True, ), 
                ignore_vbi_test = telestream_cloud_qc.models.ignore_vbi_test.ignore_vbi_test(
                    reject_on_error = True, 
                    checked = True, ), 
                force_color_space_test = telestream_cloud_qc.models.force_color_space_test.force_color_space_test(
                    color_space = 'CSUnknown', 
                    checked = True, ), 
                video_segment_detection_test = telestream_cloud_qc.models.video_segment_detection_test.video_segment_detection_test(
                    black_level_default_or_custom = 'Default', 
                    black_level = 56, 
                    percentage_of_frame = 56, 
                    min_duration_required = 1.337, 
                    min_duration_required_secs_or_frames = 'Seconds', 
                    require_digital_silence = True, 
                    reject_on_error = True, 
                    checked = True, ), 
                video_layout_test = telestream_cloud_qc.models.layout_test.layout_test(
                    layout_type = 'LayoutTypeFixedIgnoreStartAndEnd', 
                    start_duration = 1.337, 
                    start_duration_secs_or_frames = 'Seconds', 
                    end_duration = 1.337, 
                    end_duration_secs_or_frames = 'Seconds', 
                    start_enabled = True, 
                    start_hours = 56, 
                    start_minutes = 56, 
                    start_seconds = 56, 
                    start_frames = 56, 
                    end_enabled = True, 
                    end_hours = 56, 
                    end_minutes = 56, 
                    end_seconds = 56, 
                    end_frames = 56, 
                    checked = True, ), 
                letterboxing_test = telestream_cloud_qc.models.letterboxing_test.letterboxing_test(
                    ratio_or_lines = 'Ratio', 
                    ratio_horizontal = 56, 
                    ratio_vertical = 56, 
                    lines_top_and_bottom = 56, 
                    lines_left_and_right = 56, 
                    tolerance = 56, 
                    black_level_default_or_custom = 'Default', 
                    black_level = 56, 
                    reject_on_error = True, 
                    checked = True, ), 
                blanking_test = telestream_cloud_qc.models.blanking_test.blanking_test(
                    black_level_default_or_custom = 'Default', 
                    black_level = 56, 
                    checked = True, ), 
                loss_of_chroma_test = telestream_cloud_qc.models.loss_of_chroma_test.loss_of_chroma_test(
                    level_default_or_custom = 'Default', 
                    level = 56, 
                    tolerance = 56, 
                    reject_on_error = True, 
                    checked = True, ), 
                chroma_level_test = telestream_cloud_qc.models.chroma_level_test.chroma_level_test(
                    y_level_default_or_custom = 'Default', 
                    y_level_lower = 56, 
                    y_level_upper = 56, 
                    y_level_max_outside_range = 1.337, 
                    y_level_tolerance_low = 1.337, 
                    y_level_tolerance_high = 1.337, 
                    u_vlevel_default_or_custom = 'Default', 
                    u_vlevel_lower = 56, 
                    u_vlevel_upper = 56, 
                    u_vlevel_max_outside_range = 1.337, 
                    low_pass_filter = 'NoFilter', 
                    reject_on_error = True, 
                    do_correction = True, 
                    checked = True, ), 
                black_level_test = telestream_cloud_qc.models.black_level_test.black_level_test(
                    level_default_or_custom = 'Default', 
                    level = 56, 
                    level_max_outside_range = 1.337, 
                    reject_on_error = True, 
                    do_correction = True, 
                    checked = True, ), 
                rgb_gamut_test = telestream_cloud_qc.models.rgb_gamut_test.rgb_gamut_test(
                    level_default_or_custom = 'Default', 
                    level_lower = 56, 
                    level_upper = 56, 
                    level_max_outside_range = 1.337, 
                    level_tolerance = 1.337, 
                    low_pass_filter = 'NoFilter', 
                    reject_on_error = True, 
                    do_correction = True, 
                    checked = True, ), 
                hdr_test = telestream_cloud_qc.models.hdr_test.hdr_test(
                    hdr_standard = 'GenericHdr', 
                    max_fall_max_enabled = True, 
                    max_fall_max = 56, 
                    max_fall_error_enabled = True, 
                    max_fall_error = 56, 
                    max_cll_max_enabled = True, 
                    max_cll_max = 56, 
                    max_cll_error_enabled = True, 
                    max_cll_error = 56, 
                    always_calculate = True, 
                    always_report = True, 
                    reject_on_error = True, 
                    checked = True, ), 
                colour_bars_test = telestream_cloud_qc.models.colour_bars_test.colour_bars_test(
                    color_bar_standard = 'AnyColorBars', 
                    tolerance = 56, 
                    time_range_enabled = True, 
                    start_time = 1.337, 
                    end_time = 1.337, 
                    range_tolerance = 1.337, 
                    time_secs_or_frames = 'Seconds', 
                    not_at_any_other_time = True, 
                    reject_on_error = True, 
                    do_correction = True, 
                    checked = True, ), 
                black_frame_test = telestream_cloud_qc.models.black_frame_test.black_frame_test(
                    level_default_or_custom = 'Default', 
                    level = 56, 
                    percentage_of_frame = 56, 
                    start_range_enabled = True, 
                    start_time = 1.337, 
                    end_time = 1.337, 
                    start_range_tolerance = 1.337, 
                    time_secs_or_frames = 'Seconds', 
                    end_range_enabled = True, 
                    end_range = 1.337, 
                    end_range_tolerance = 1.337, 
                    end_secs_or_frames = 'Seconds', 
                    not_at_any_other_time = True, 
                    max_time_allowed = 1.337, 
                    max_time_allowed_secs_or_frames = 'Seconds', 
                    max_time_at_start = True, 
                    max_time_allowed_at_start = 1.337, 
                    max_time_allowed_at_start_secs_or_frames = 'Seconds', 
                    max_time_at_end = True, 
                    max_time_allowed_at_end = 1.337, 
                    max_time_allowed_at_end_secs_or_frames = 'Seconds', 
                    reject_on_error = True, 
                    do_correction = True, 
                    checked = True, ), 
                single_color_test = telestream_cloud_qc.models.single_color_test.single_color_test(
                    max_time_allowed = 1.337, 
                    time_secs_or_frames = 'Seconds', 
                    percentage_of_frame = 1.337, 
                    ignore_below = 56, 
                    reject_on_error = True, 
                    checked = True, ), 
                freeze_frame_test = telestream_cloud_qc.models.freeze_frame_test.freeze_frame_test(
                    sensitivity = 'Low', 
                    time_range_enabled = True, 
                    start_time = 1.337, 
                    end_time = 1.337, 
                    start_range_tolerance = 1.337, 
                    time_secs_or_frames = 'Seconds', 
                    end_range_enabled = True, 
                    end_range = 1.337, 
                    end_range_duration = 1.337, 
                    end_range_tolerance = 1.337, 
                    end_secs_or_frames = 'Seconds', 
                    not_at_any_other_time = True, 
                    max_time_allowed = 1.337, 
                    max_time_allowed_secs_or_frames = 'Seconds', 
                    reject_on_error = True, 
                    checked = True, ), 
                blockiness_test = telestream_cloud_qc.models.blockiness_test.blockiness_test(
                    quality_level = 56, 
                    max_time_below_quality = 1.337, 
                    max_time_below_quality_secs_or_frames = 'Seconds', 
                    reject_on_error = True, 
                    checked = True, ), 
                field_order_test = telestream_cloud_qc.models.field_order_test.field_order_test(
                    flagged_field_order = 'UnknownFieldOrder', 
                    baseband_enabled = True, 
                    simple = True, 
                    baseband_field_order = 'UnknownFieldOrder', 
                    reject_on_error = True, 
                    checked = True, ), 
                cadence_test = telestream_cloud_qc.models.cadence_test.cadence_test(
                    check_cadence = True, 
                    cadence_required = 'CadenceUnknown', 
                    check_cadence_breaks = True, 
                    report_cadence = True, 
                    check_for_poor_cadence = True, 
                    reject_on_error = True, 
                    checked = True, ), 
                dropout_test = telestream_cloud_qc.models.dropout_test.dropout_test(
                    sensitivity = 'Low', 
                    reject_on_error = True, 
                    do_correction = True, 
                    checked = True, ), 
                digital_dropout_test = telestream_cloud_qc.models.digital_dropout_test.digital_dropout_test(
                    sensitivity = 'Low', 
                    reject_on_error = True, 
                    checked = True, ), 
                stripe_test = telestream_cloud_qc.models.stripe_test.stripe_test(
                    sensitivity = 'Low', 
                    reject_on_error = True, 
                    do_correction = True, 
                    checked = True, ), 
                corrupt_frame_test = telestream_cloud_qc.models.corrupt_frame_test.corrupt_frame_test(
                    sensitivity = 'Low', 
                    reject_on_error = True, 
                    do_correction = True, 
                    checked = True, ), 
                flash_test = telestream_cloud_qc.models.flash_test.flash_test(
                    check_type = 'PSEStandard', 
                    check_for_extended = True, 
                    check_for_red = True, 
                    check_for_patterns = True, 
                    reject_on_error = True, 
                    do_correction = True, 
                    checked = True, ), 
                media_offline_test = telestream_cloud_qc.models.media_offline_test.media_offline_test(
                    reject_on_error = True, 
                    checked = True, )
            )
        else :
            return VideoConfig(
        )

    def testVideoConfig(self):
        """Test VideoConfig"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
