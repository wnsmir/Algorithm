SELECT u.USER_ID, u.NICKNAME, sum(price) as TOTAL_SALES from
USED_GOODS_BOARD b left join USED_GOODS_USER u on b.WRITER_ID = u.USER_ID

where status = "DONE"

group by u.USER_ID

having sum(price) >= 700000

order by TOTAL_SALES;