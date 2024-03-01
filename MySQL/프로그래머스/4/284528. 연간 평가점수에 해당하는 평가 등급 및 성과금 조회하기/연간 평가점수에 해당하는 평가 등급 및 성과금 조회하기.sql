SELECT
    E.EMP_NO,
    E.EMP_NAME,
    (CASE
        WHEN G.SCORE >= 96 THEN 'S'
        WHEN G.SCORE >= 90 THEN 'A'
        WHEN G.SCORE >= 80 THEN 'B'
        ELSE 'C'
    END) AS GRADE,
    (CASE
        WHEN G.SCORE >= 96 THEN SAL*0.2
        WHEN G.SCORE >= 90 THEN SAL*0.15
        WHEN G.SCORE >= 80 THEN SAL*0.1
        ELSE SAL*0
    END) AS BONUS
FROM HR_EMPLOYEES E
    JOIN (
        SELECT
            EMP_NO,
            AVG(SCORE) AS SCORE
        FROM HR_GRADE
        GROUP BY EMP_NO
        ) G
    ON E.EMP_NO = G.EMP_NO
ORDER BY E.EMP_NO