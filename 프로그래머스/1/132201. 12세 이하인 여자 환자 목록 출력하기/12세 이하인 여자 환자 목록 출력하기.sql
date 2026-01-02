select PT_NAME, PT_NO, GEND_CD, AGE, ifnull(TLNO, 'NONE') AS TLNO from PATIENT

where AGE < 13 and GEND_CD = "W"

order by AGE desc, PT_NAME;