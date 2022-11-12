"""Collection of Cereal schedules"""

from dagster import (
    schedule,
    load_assets_from_package_module,
    repository,
    with_resources,
    define_asset_job,
    ScheduleDefinition,
    AssetSelection,
)

from staykeepers_dbt_dagster import assets
from staykeepers_dbt_dagster.assets import dbt_assets



# https://docs.dagster.io/concepts/partitions-schedules-sensors/schedules


daily_job = define_asset_job(
    name="daily_refresh",
    selection=AssetSelection.groups("*"),
    )

daily_schedule = ScheduleDefinition(
    name="daily_schedule",
    job=daily_job,
    cron_schedule="@daily",
    execution_timezone="Europe/London",
)

hourly_job = define_asset_job(
    name="hourly_refresh",
    selection=AssetSelection.groups("data"),
    )

hourly_schedule = ScheduleDefinition(
    name="hourly_schedule",
    job=hourly_job,
    cron_schedule="0 8-17 * * 1-5",
    execution_timezone="Europe/London",
)
