"""Root pytest configuration.

StarRocks `date_trunc` only supports second-or-larger granularities, so tests that require
millisecond/sub-daily granularity cannot be rendered for StarRocks.
"""

from __future__ import annotations

import os

import pytest

_STARROCKS_UNSUPPORTED_TESTS = {
    "multiple_time_spines_in_query_for_cumulative_metric",
    "multiple_time_spines_in_query_for_join_to_time_spine_metric",
    "no_metric_custom_granularity_joined_to_non_default_grain",
    "simple_metric_with_multi_hop_custom_granularity",
    "join_to_time_spine_with_filter_smaller_than_group_by",
    "date_part_with_non_default_grain",
    "simple_metric_with_joined_sub_daily_dimension",
    "simple_metric_with_sub_daily_dimension",
    "sub_daily_dimension",
    "subdaily_cumulative_grain_to_date_metric",
    "subdaily_cumulative_window_metric",
    "subdaily_granularity_overrides_metric_default_granularity",
    "subdaily_join_to_time_spine_metric",
    "subdaily_offset_to_grain_metric",
    "subdaily_offset_window_metric",
    "subdaily_time_constraint_with_metric",
    "partitioned_join",
}


def pytest_collection_modifyitems(config: pytest.Config, items: list[pytest.Item]) -> None:
    """Skip sub-daily granularity tests when running against StarRocks."""
    if not os.environ.get("MF_SQL_ENGINE_URL", "").startswith("starrocks"):
        return
    skip = pytest.mark.skip(reason="StarRocks does not support millisecond/sub-daily granularity")
    for item in items:
        if item.name.removeprefix("test_") in _STARROCKS_UNSUPPORTED_TESTS:
            item.add_marker(skip)
