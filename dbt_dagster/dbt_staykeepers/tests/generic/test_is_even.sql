{% test is_wrong_commission(model, column_name) %}

with validation as (

    select
        {{ column_name }} as commission

    from {{ model }}

),

validation_errors as (

    select
        commission

    from validation
    -- if this is true, then commission is actually odd!
    where commission between 0.0001 and 0.0099

)

select *
from validation_errors

{% endtest %}
