select f.ID, n.FISH_NAME, f.LENGTH from FISH_INFO f join FISH_NAME_INFO n 
on f.FISH_TYPE = n.FISH_TYPE

where f.length = (select max(f2.length) from FISH_INFO f2
                   WHERE f2.FISH_TYPE = f.FISH_TYPE)

order by f.ID