select i.ID, n.FISH_NAME, LENGTH from FISH_INFO i
join FISH_NAME_INFO n on i.FISH_TYPE = n.FISH_TYPE

where i.length = (select max(length) from FISH_INFO where FISH_TYPE = i.FISH_TYPE)

order by i.ID