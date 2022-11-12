from dagster_dbt import dbt_cli_resource, load_assets_from_dbt_project
from dagster import file_relative_path, with_resources


DBT_PROJECT_PATH = file_relative_path(__file__, "../../dbt_staykeepers")
DBT_PROFILES = file_relative_path(__file__, "../../dbt_staykeepers/config")
DBT_ENV = "prod"

# dbt_assets = load_assets_from_dbt_project(project_dir=DBT_PROJECT_PATH, profiles_dir=DBT_PROFILES, key_prefix=["dbt_staykeepers"])

dbt_assets = with_resources(
    load_assets_from_dbt_project(
        project_dir=DBT_PROJECT_PATH,
        profiles_dir=DBT_PROFILES,
        key_prefix=["dbt_assets"],
        source_key_prefix=["bigquery_assets"],
        ),
    {
        "dbt": dbt_cli_resource.configured(
            {
                "project_dir": DBT_PROJECT_PATH,
                "profiles_dir": DBT_PROFILES,
                "target": DBT_ENV,
            },
        ),
    },
)

