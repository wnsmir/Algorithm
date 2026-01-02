select count(*) as fish_count 
from FISH_INFO i join FISH_NAME_INFO n on i.FISH_TYPE = n.FISH_TYPE
where FISH_NAME = 'BASS' or FISH_NAME = 'SNAPPER';