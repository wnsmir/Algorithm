select distinct d.id, d.email, d.first_name, d.last_name 
from developers d join skillcodes s
on s.name in ('Python', 'C#')
where (d.skill_code & s.code) > 0
order by d.id