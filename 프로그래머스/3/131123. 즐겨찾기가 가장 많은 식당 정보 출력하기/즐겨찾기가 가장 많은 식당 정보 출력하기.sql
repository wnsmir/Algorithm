select i.FOOD_TYPE, i.REST_ID, i.REST_NAME, i.FAVORITES from REST_INFO i
join (select FOOD_TYPE, max(FAVORITES) as max_fav from REST_INFO
     group by FOOD_TYPE) m
     on i.FOOD_TYPE = m.FOOD_TYPE
     and i.FAVORITES = m.max_fav
     order by i.FOOD_TYPE desc