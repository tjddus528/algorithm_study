SELECT
    G.SCORE,
    E.EMP_NO,
    EMP_NAME,
    POSITION,
    EMAIL
FROM
    HR_EMPLOYEES E
    JOIN (
        SELECT
            EMP_NO,
            SUM(SCORE) AS SCORE
        FROM HR_GRADE
        GROUP BY EMP_NO
    ) G
    ON E.EMP_NO = G.EMP_NO
ORDER BY SCORE DESC
LIMIT 1
    
