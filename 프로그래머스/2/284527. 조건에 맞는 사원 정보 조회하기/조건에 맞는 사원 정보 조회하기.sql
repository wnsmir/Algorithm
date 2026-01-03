select g.SCORE, e.EMP_NO, e.EMP_NAME, e.POSITION, e.EMAIL from HR_EMPLOYEES e
join (select emp_no, sum(score) as SCORE from HR_GRADE
where year = 2022
group by EMP_NO) g
on e.EMP_NO = g.EMP_NO

where g.SCORE = (select max(t.score) from
(select emp_no, sum(score) as SCORE from HR_GRADE
where year = 2022
group by EMP_NO) t);