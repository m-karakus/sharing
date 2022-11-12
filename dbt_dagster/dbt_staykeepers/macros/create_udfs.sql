{% macro create_udfs() %}

create schema if not exists {{target.schema}};

{{ create_f_unpivot() }}

{{ create_f_cast_kv_array_to_date_float() }}

{% endmacro %}
