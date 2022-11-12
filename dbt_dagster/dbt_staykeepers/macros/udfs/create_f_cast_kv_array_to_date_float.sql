{% macro create_f_cast_kv_array_to_date_float() %}

CREATE OR REPLACE FUNCTION {{target.schema}}.cast_kv_array_to_date_float(arr ANY TYPE, date_format STRING)
AS ((
  # https://medium.com/@hoffa/how-to-unpivot-multiple-columns-into-tidy-pairs-with-sql-and-bigquery-d9d0e74ce675
  SELECT ARRAY_AGG(STRUCT(SAFE.PARSE_DATE(date_format, key) AS date, SAFE_CAST(value AS FLOAT64) AS value))
  FROM UNNEST(arr)
));

{% endmacro %}
