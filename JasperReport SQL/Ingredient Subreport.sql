SELECT
    -- Ingredient info
    i.generic2 AS ingredient_group,
    i.ingredientid,
    i.generic1 AS label_claim,
   	-- Ingredient Test Result info
    ir.specification_range,
    ir.resultdate AS test_date,
    ir.method,
    ir.generic01 AS notebook_ref,
   	ir.status,
    -- Ingredient name/description
    CASE
        WHEN UPPER(i.ingredientid) LIKE 'MULTI-PART INGREDIENT LIST%'
        THEN
            (SELECT LISTAGG(i2.description) WITHIN GROUP (ORDER BY i2.ingredientid)
             FROM ingredient i2
             WHERE UPPER(i2.ingredientid) LIKE 'MULTI%' AND i2.formulationguid = i.formulationguid)
        WHEN UPPER(i.ingredientid) LIKE 'GENERIC INGREDIENT A%'
        THEN
            (SELECT LISTAGG(i2.description) WITHIN GROUP (ORDER BY i2.ingredientid)
             FROM ingredient i2
             WHERE UPPER(ingredientid) LIKE 'GENERIC INGREDIENT A%' AND i2.formulationguid = i.formulationguid)
        WHEN UPPER(i.ingredientid) LIKE 'GENERIC INGREDIENT B%'
        THEN
            (SELECT LISTAGG(i2.description) WITHIN GROUP (ORDER BY i2.ingredientid)
             FROM ingredient i2
             WHERE UPPER(ingredientid) LIKE 'GENERIC INGREDIENT B%' AND i2.formulationguid = i.formulationguid)
        WHEN UPPER(i.ingredientid) LIKE 'GENERIC INGREDIENT C%'
        THEN
            (SELECT LISTAGG(i2.description) WITHIN GROUP (ORDER BY i2.ingredientid)
             FROM ingredient i2
             WHERE UPPER(ingredientid) LIKE 'GENERIC INGREDIENT C%' AND i2.formulationguid = i.formulationguid)
        WHEN UPPER(i.ingredientid) LIKE 'GENERIC INGREDIENT D%'
        THEN
            (SELECT LISTAGG(i2.description) WITHIN GROUP (ORDER BY i2.ingredientid)
             FROM ingredient i2
             WHERE UPPER(ingredientid) LIKE 'GENERIC INGREDIENT D%' AND i2.formulationguid = i.formulationguid)
        WHEN UPPER(i.ingredientid) LIKE 'GENERIC INGREDIENT E%'
        THEN
            (SELECT LISTAGG(i2.description) WITHIN GROUP (ORDER BY i2.ingredientid)
             FROM ingredient i2
             WHERE UPPER(ingredientid) LIKE 'GENERIC INGREDIENT E%' AND i2.formulationguid = i.formulationguid)
        WHEN UPPER(i.ingredientid) LIKE 'GENERIC INGREDIENT F%'
        THEN
            (SELECT LISTAGG(i2.description) WITHIN GROUP (ORDER BY i2.ingredientid)
             FROM ingredient i2
             WHERE UPPER(ingredientid) LIKE 'GENERIC INGREDIENT F%' AND i2.formulationguid = i.formulationguid)
        WHEN UPPER(i.ingredientid) LIKE 'GENERIC INGREDIENT G%'
        THEN
            (SELECT LISTAGG(i2.description) WITHIN GROUP (ORDER BY i2.ingredientid)
             FROM ingredient i2
             WHERE UPPER(ingredientid) LIKE 'GENERIC INGREDIENT G%' AND i2.formulationguid = i.formulationguid)
        WHEN UPPER(i.ingredientid) LIKE 'GENERIC INGREDIENT H%'
        THEN
            (SELECT LISTAGG(i2.description) WITHIN GROUP (ORDER BY i2.ingredientid)
             FROM ingredient i2 WHERE UPPER(ingredientid) LIKE 'GENERIC INGREDIENT H%' AND i2.formulationguid = i.formulationguid)
        WHEN UPPER(i.ingredientid) LIKE 'GENERIC INGREDIENT I%'
        THEN
            (SELECT LISTAGG(i2.description) WITHIN GROUP (ORDER BY i2.ingredientid)
             FROM ingredient i2
             WHERE UPPER(ingredientid) LIKE 'GENERIC INGREDIENT I%' AND i2.formulationguid = i.formulationguid)
        WHEN UPPER(i.ingredientid) LIKE 'GENERIC INGREDIENT J%'
        THEN
            (SELECT LISTAGG(i2.description) WITHIN GROUP (ORDER BY i2.ingredientid)
             FROM ingredient i2
             WHERE UPPER(ingredientid) LIKE 'GENERIC INGREDIENT J%' AND i2.formulationguid = i.formulationguid)
        WHEN UPPER(i.ingredientid) LIKE 'GENERIC INGREDIENT K%'
        THEN
            (SELECT LISTAGG(i2.description) WITHIN GROUP (ORDER BY i2.ingredientid)
             FROM ingredient i2 WHERE UPPER(ingredientid) LIKE 'GENERIC INGREDIENT K%' AND i2.formulationguid = i.formulationguid)
        WHEN UPPER(i.ingredientid) LIKE 'GENERIC INGREDIENT L%'
        THEN
            (SELECT LISTAGG(i2.description) WITHIN GROUP (ORDER BY i2.ingredientid)
             FROM ingredient i2
             WHERE UPPER(ingredientid) LIKE 'GENERIC INGREDIENT L%' AND i2.formulationguid = i.formulationguid)
        WHEN UPPER(i.ingredientid) LIKE 'GENERIC INGREDIENT M%'
        THEN
            (SELECT LISTAGG(i2.description) WITHIN GROUP (ORDER BY i2.ingredientid)
             FROM ingredient i2
             WHERE UPPER(ingredientid) LIKE 'GENERIC INGREDIENT M%' AND i2.formulationguid = i.formulationguid)
        WHEN UPPER(i.ingredientid) LIKE 'GENERIC INGREDIENT N%'
        THEN
            (SELECT LISTAGG(i2.description) WITHIN GROUP (ORDER BY i2.ingredientid)
             FROM ingredient i2 WHERE UPPER(ingredientid) LIKE 'GENERIC INGREDIENT N%' AND i2.formulationguid = i.formulationguid)
        WHEN UPPER(i.ingredientid) LIKE 'GENERIC INGREDIENT O%'
        THEN
            (SELECT LISTAGG(i2.description) WITHIN GROUP (ORDER BY i2.ingredientid)
             FROM ingredient i2
             WHERE UPPER(ingredientid) LIKE 'GENERIC INGREDIENT O%' AND i2.formulationguid = i.formulationguid)
        WHEN UPPER(i.ingredientid) LIKE 'GENERIC INGREDIENT P%'
        THEN
            (SELECT LISTAGG(i2.description) WITHIN GROUP (ORDER BY i2.ingredientid)
             FROM ingredient i2
             WHERE UPPER(ingredientid) LIKE 'GENERIC INGREDIENT P%' AND i2.formulationguid = i.formulationguid)
        WHEN UPPER(i.ingredientid) LIKE 'GENERIC INGREDIENT Q%'
        THEN
            (SELECT LISTAGG(i2.description) WITHIN GROUP (ORDER BY i2.ingredientid)
             FROM ingredient i2
             WHERE UPPER(ingredientid) LIKE 'GENERIC INGREDIENT Q%' AND i2.formulationguid = i.formulationguid)
        ELSE i.description
    END AS ingredient,
    -- Result display value
    CASE
        WHEN ir.resulttype = 'NUMERIC'
            AND ir.status = 70
            AND (ir.resultvaluation <> 'SKIP LOT' OR ir.resultvaluation IS NULL)
        THEN
	        ir.prefix||TRIM(TO_CHAR(REGEXP_SUBSTR(REPLACE(ir.numericalresulttext,ir.prefix,''),'^\d+'),'999,999,999'))
             || (CASE
                    WHEN INSTR(ir.numericalresulttext,'.') > 0
                    THEN
                        SUBSTR(ir.numericalresulttext,INSTR(ir.numericalresulttext,'.'))
                    END)
            || DECODE(ir.unit,NULL,NULL,' '||ir.unit)
        WHEN ir.resulttype IN ('LIST','TEXT')
            AND ir.status = 70
            AND (ir.resultvaluation <> 'SKIP LOT' OR ir.resultvaluation IS NULL)
        THEN
            ir.textresult || DECODE(ir.unit,NULL,NULL,' ' || ir.unit)
        WHEN ir.status = 10
            AND (ir.resultvaluation <> 'SKIP LOT' OR ir.resultvaluation IS NULL)
        THEN
             'pending'
        ELSE
            CASE
                WHEN UPPER(i.ingredientid) LIKE 'INGREDIENT NOTE%'
                    OR UPPER(i.ingredientid) LIKE 'MULTI-PART INGREDIENT LIST%'
                    AND i.generic3 IS NULL
                THEN
                    ''
                WHEN UPPER(i.ingredientid) LIKE 'GENERIC INGREDIENT%'
                    AND i.generic3 IS NULL
                THEN
                    'Not Tested'
                WHEN i.generic3 IS NOT NULL
                THEN
                    i.generic3
                ELSE 'Not Tested'
            END
    END AS result
FROM
    -- Ingredients for this product/formulation
    ingredient i
    JOIN formulation f ON i.formulationguid = f.formulationguid
            AND f.productid =  $P{PRODUCTID}
            AND f.formulationid  =  $P{FORMULATIONID}
            AND f.deletion = 'N'
    -- Join test results to the ingredients
    LEFT JOIN
        (SELECT t.testid, t.testgroup,
                tr.resultid, tr.resultguid, tr.resulttype, tr.prefix, tr.numericalresulttext, tr.textresult, tr.unit,
                tr.requirement, tr.resultvaluation, tr.status, tr.resultdate,tr.generic01,
                trr.listvalue,
                -- Specification Range
                CASE
                    WHEN tr.resulttype = 'LIST'
                        AND (tr.resultvaluation <> 'SKIP LOT' OR tr.resultvaluation IS NULL)
                    THEN
                        DECODE(t.requirement, NULL, trr.listvalue, t.requirement)
                    WHEN tr.resulttype <> 'LIST'
                        AND (tr.resultvaluation <> 'SKIP LOT' OR tr.resultvaluation IS NULL)
                    THEN
                      DECODE(tr.resulttype,NULL,NULL,tr.requirement)
                    ELSE  ''
                 END AS specification_range,
                -- Method
                CASE
                    WHEN (tr.resultvaluation <> 'SKIP LOT'
                        OR tr.resultvaluation IS NULL)
                    THEN
                        sm.description
                    ELSE  ''
                END AS method
        FROM testresult tr
        JOIN test t ON t.testguid = tr.testguid
            AND t.deletion = 'N'
            AND t.requestguid IN
                -- All tests for the batch in one or more requests
                (SELECT requestguid
                 FROM testrequest
                 WHERE  batchnumber =  $P{BATCHNUMBER}
                 AND deletion = 'N')
        LEFT JOIN smmethod sm ON sm.methodid = t.methodid
                AND sm.versionno = t.methodversionno
                AND sm.deletion = 'N'
        LEFT JOIN testresultrequirement trr ON trr.resultguid = tr.resultguid
                AND trr.valuationcode = 1
        WHERE tr.deletion = 'N'
        AND tr.flagisfinalresult = 'Y' ) ir
    ON UPPER(i.ingredientid) = UPPER(ir.resultid)
WHERE i.deletion = 'N'
AND NOT(UPPER(i.ingredientid) LIKE 'MULTI%'
	AND SUBSTR(i.ingredientid,-1,1) <> 1)
	AND NOT(UPPER(i.ingredientid) LIKE 'GENERIC INGREDIENT%'
	AND SUBSTR(i.ingredientid,-1,1) <> 1)
ORDER BY i.position