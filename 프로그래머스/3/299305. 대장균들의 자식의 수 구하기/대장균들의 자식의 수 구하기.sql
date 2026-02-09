select d.ID, count(s.PARENT_ID) as CHILD_COUNT from 
ECOLI_DATA d left join (select PARENT_ID from ECOLI_DATA) s on d.ID = s.PARENT_ID

group by ID

order by ID