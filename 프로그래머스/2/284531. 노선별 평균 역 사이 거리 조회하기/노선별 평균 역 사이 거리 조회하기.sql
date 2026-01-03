select ROUTE, 
concat(round(sum(D_BETWEEN_DIST), 1), 'km') AS TOTAL_DISTANCE, 
concat(round(avg(D_BETWEEN_DIST), 2), 'km') AS AVERAGE_DISTANCE

from SUBWAY_DISTANCE

group by ROUTE

order by sum(D_BETWEEN_DIST) desc;