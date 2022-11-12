{% macro create_f_unpivot() %}

CREATE OR REPLACE FUNCTION {{target.schema}}.unpivot(x ANY TYPE, col_regex STRING)
AS ((
  # https://medium.com/@hoffa/how-to-unpivot-multiple-columns-into-tidy-pairs-with-sql-and-bigquery-d9d0e74ce675
  SELECT
   ARRAY_AGG(STRUCT(
     REGEXP_EXTRACT(y, '[^"]*') AS key
   , REGEXP_EXTRACT(y, r':([^"]*)\"?[,}\]]') AS value
   ))
  FROM UNNEST((
    SELECT REGEXP_EXTRACT_ALL(json,col_regex||r'[^:]+:\"?[^"]+\"?') arr
    FROM (SELECT TO_JSON_STRING(x) json))) y
));

{% endmacro %}
