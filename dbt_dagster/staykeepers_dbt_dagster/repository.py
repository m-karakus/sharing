import os

from dagster_dbt import dbt_cli_resource
from staykeepers_dbt_dagster import assets
from staykeepers_dbt_dagster.assets import dbt_assets
import staykeepers_dbt_dagster.schedules as s
from dagster import (
    load_assets_from_package_module,
    repository,
    with_resources,
    define_asset_job,
    ScheduleDefinition,
)


@repository
def staykeepers_dbt_dagster():
    return [
        s.hourly_schedule,
        s.daily_schedule,
        dbt_assets,
    ]

