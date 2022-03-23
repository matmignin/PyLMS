SELECT
    tr.resultid,
    tr.requirement,
    tr.numericalresultraw,
    CASE
        WHEN UPPER(tr.resultvaluation) = 'OK'
        THEN 'Pass'
        ELSE 'Fail'
    END AS valuation
FROM
    testresult tr
WHERE
    $X{EQUAL,
    tr.testguid,
    TESTGUID}AND
    UPPER(tr.resultid) LIKE 'QAC%' AND
    tr.resultvaluation IS NOT NULL
ORDER BY
    tr.sequencenumber