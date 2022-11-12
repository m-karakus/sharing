#!/bin/bash
# dbt/staykeepers/models/
dbt run --models stk_data --target prod
