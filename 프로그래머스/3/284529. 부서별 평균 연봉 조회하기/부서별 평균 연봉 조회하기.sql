select d.DEPT_ID, d.DEPT_NAME_EN, round(sum(SAL) / count(*), 0) as AVG_SAL from
HR_DEPARTMENT d join HR_EMPLOYEES e on d.DEPT_ID = e.DEPT_ID

GROUP BY d.DEPT_ID

order by AVG_SAL desc;