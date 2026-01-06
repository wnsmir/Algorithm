select d.id, case when s.PARENT_ID is null then 0 else count(*) end as CHILD_COUNT

from ECOLI_DATA d left join (select PARENT_ID from ECOLI_DATA where PARENT_ID is not null) s on d.ID = s.PARENT_ID

group by d.id

order by d.id