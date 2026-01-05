SELECT u.USER_ID, u.NICKNAME, concat(CITY, " ", STREET_ADDRESS1," ", STREET_ADDRESS2) as 전체주소, 
concat(substring(u.TLNO, 1, 3), '-',
substring(u.TLNO, 4, 4), '-',
substring(u.TLNO, 8, 4)) as 전화번호 

from USED_GOODS_BOARD b join USED_GOODS_USER u on b.WRITER_ID = u.USER_ID

group by b.WRITER_ID

having count(*) > 2

order by u.USER_ID desc;