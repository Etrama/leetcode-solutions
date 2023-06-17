# Write your MySQL query statement below
select 
    product_id, 
    round(sum(units*price)/sum(units),2) as average_price
from 
    (select 
        unitssold.product_id,
        unitssold.units,
        prices.price
    from 
        unitssold
    left join
        prices
    on 
        unitssold.product_id = prices.product_id
        and
        unitssold.purchase_date >= prices.start_date
        and
        unitssold.purchase_date <= prices.end_date
    ) as temp
group by
    product_id