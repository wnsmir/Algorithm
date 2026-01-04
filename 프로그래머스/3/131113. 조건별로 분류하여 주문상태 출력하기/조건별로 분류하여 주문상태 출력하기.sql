SELECT ORDER_ID, PRODUCT_ID, date_format(OUT_DATE, "%Y-%m-%d") as OUT_DATE,
case when OUT_DATE is null then '출고미정'
when out_date <= '2022-05-01' then '출고완료'
else '출고대기'
end AS 출고여부 
from FOOD_ORDER;