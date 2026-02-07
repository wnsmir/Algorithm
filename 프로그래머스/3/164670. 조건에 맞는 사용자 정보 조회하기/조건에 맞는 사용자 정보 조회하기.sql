SELECT u.USER_ID, u.NICKNAME, concat(u.CITY, ' ', u.STREET_ADDRESS1, ' ', u.STREET_ADDRESS2) as 전체주소, 
CONCAT(SUBSTRING(TLNO, 1, 3), '-', SUBSTRING(TLNO, 4, 4), '-', SUBSTRING(TLNO, 8, 4)) as 전화번호
from USED_GOODS_BOARD g 
join USED_GOODS_USER u on g.WRITER_ID = u.USER_ID

group by g.WRITER_ID

having count(*) > 2

order by g.WRITER_ID desc