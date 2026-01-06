SELECT p.ID, p.NAME, p.HOST_ID from PLACES p left join 
(select ID, HOST_ID from PLACES group by HOST_ID

having count(*) >= 2) h on p.HOST_ID = h.HOST_ID

where h.HOST_ID is not null

order by ID;