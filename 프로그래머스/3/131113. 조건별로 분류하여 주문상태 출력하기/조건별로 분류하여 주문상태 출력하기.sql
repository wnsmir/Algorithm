select ORDER_ID, PRODUCT_ID, DATE_FORMAT(OUT_DATE, '%Y-%m-%d') AS OUT_DATE,
case when OUT_DATE <= DATE '2022-05-01' then '출고완료'
when OUT_DATE > DATE '2022-05-01' then '출고대기'
else '출고미정' end as 출고여부

from FOOD_ORDER

order by ORDER_ID