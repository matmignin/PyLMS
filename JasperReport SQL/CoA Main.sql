SELECT
    DISTINCT trq.requestguid,
    p.productid,
    f.formulationid,
    p.tradename,
    p.alternateid1 AS product_code,
    DECODE(p.generic1, NULL, NULL, p.generic1 | | ':') AS vendor_code_label,
    p.alternateid2 AS vendor_code,
    p.generic2 AS micro_footnote,
    DECODE(f.generic5, NULL, NULL, f.generic5 | | ':') AS vendor_product_label,
    f.alternateid1 AS vendor_product_code,
    f.generic1 AS serving_size,
    f.generic2 AS shape_size,
    f.generic3 AS description_color,
    f.generic4 AS fill_weight_spec,
    trq.batchnumber AS mfg_lot,
    coa_primary.generic01 AS package_lot,
    coa_primary.generic04 AS blister_lot,
    coa_primary.generic02 AS ship_to,
    coa_primary.generic06 AS coated_lot,
    dv.description AS ship_to_parms,
    coa_results.customer_lot,
    -- Open request count
    (SELECT
    COUNT(1)
FROM
    testrequest trqc
    JOIN requestsample rqc
    ON rqc.requestguid = trqc.requestguid AND
    rqc.deletion = 'N'
    JOIN physicalsample psc
    ON psc.sampleguid = rqc.sampleguid
WHERE
    trqc.product = trq.product AND
    trqc.formulationid = trq.formulationid AND
    psc.batchnumber = ps.batchnumber AND ( (
            ps.generic01 IS NOT NULL AND
            psc.generic01 = ps.generic01
        ) OR
        ps.generic01 IS NULL
    ) AND ( (
            ps.generic04 IS NOT NULL AND
            psc.generic04 = ps.generic04
        ) OR
        ps.generic04 IS NULL
    ) AND
    trqc.status IN (1000, 500, 100)
) open_requests,
coa_results.testguid AS coa_testguid,
coa_sign.max_circulationid AS coa_version,
coa_results.manufacture_date,
coa_results.expiration_date,
coa_results.po_number,
coa_results.number_of_boxes,
coa_results.quantity_per_box,
coa_results.total_quantity,
coa_results.carton_lot,
coa_results.fill_weight,
-- CoA something ??
-- (SELECT
    -- COUNT(1)
-- FROM
    -- testresult tr
-- WHERE
    -- tr.testguid = coa_results.testguid AND
    -- tr.resultid = 'Number of boxes' AND
    -- tr.resultvaluation IS NOT NULL
-- ) boxes,
coa_results.approvedby AS coa_userid,
e.employeefirstname | | ' ' | | e.employeename AS coa_name,
e.employeetitle AS coa_title,
coa_results.approvaldate AS coa_date,
-- Report revision
CASE
    WHEN coa_results.approvaldate > $P{REPORT_REV1_DATE}
    THEN 'Y'
    ELSE 'N'
END AS IS_REPORT_REV1,
-- Report date format
(SELECT
    dv.description
FROM
    domainvalue dv
WHERE
    UPPER(dv.domainid) = 'REPORT PARAMETERS' AND
    UPPER(dv.value) = 'DATE FORMAT' AND
    dv.deletion = 'N'
) report_date_format
FROM
    testrequest trq --
    JOIN (
        SELECT
            DISTINCT t.requestguid,
            ts.sampleguid
        FROM
            testsample ts
            JOIN test t
            ON t.testguid = ts.testguid AND
            t.deletion = 'N'
        WHERE
            ts.deletion = 'N'
        UNION
        SELECT
            rs.requestguid,
            rs.sampleguid
        FROM
            requestsample rs
        WHERE
            rs.deletion = 'N'
    ) rs
    ON rs.requestguid = trq.requestguid --
    JOIN physicalsample ps
    ON ps.sampleguid = rs.sampleguid
    LEFT JOIN product p
    ON p.productid = trq.product AND
    p.deletion = 'N'
    LEFT JOIN formulation f
    ON f.productid = trq.product AND
    f.formulationid = trq.formulationid AND
    f.deletion = 'N'
    LEFT JOIN (
        SELECT
            trq1.requestguid,
            ps1.batchnumber,
            ps1.generic01,
            ps1.generic02,
            ps1.generic04,
            ps1.generic06,
            trq2.requestguid AS primary_requestguid,
            t.testgroup
        FROM
            testrequest trq1
            JOIN testrequest trq2
            ON trq2.batchnumber = trq1.batchnumber AND
            trq2.product = trq1.product AND
            trq2.formulationid = trq1.formulationid
            JOIN requestsample rs1
            ON rs1.requestguid = trq2.requestguid AND
            rs1.deletion = 'N'
            JOIN physicalsample ps1
            ON ps1.sampleguid = rs1.sampleguid
            JOIN test t
            ON t.requestguid = trq2.requestguid AND
            t.testgroup = 'COA' AND
            t.deletion = 'N'
        WHERE
            trq1.batchnumber IS NOT NULL AND
            trq1.product IS NOT NULL AND
            trq1.formulationid IS NOT NULL
    ) coa_primary
    ON coa_primary.requestguid = trq.requestguid AND
    coa_primary.batchnumber = ps.batchnumber AND ( (
            ps.generic01 IS NOT NULL AND
            coa_primary.generic01 = ps.generic01
        ) OR
        ps.generic01 IS NULL
    ) AND ( (
            ps.generic04 IS NOT NULL AND
            coa_primary.generic04 = ps.generic04
        ) OR
        ps.generic04 IS NULL
    ) --
    LEFT JOIN (
        SELECT
            trs.requestguid,
            MAX(trs.circulationid) AS max_circulationid
        FROM
            testrequestsign trs
            JOIN test t
            ON t.requestguid = trs.requestguid AND
            t.testgroup = 'COA' AND
            t.deletion = 'N'
        GROUP BY
            trs.requestguid
    ) coa_sign
    ON coa_sign.requestguid = coa_primary.primary_requestguid --
    LEFT JOIN (
        SELECT
            t.testguid,
            ps.batchnumber,
            ps.generic01,
            ps.generic04,
            trq.product,
            trq.formulationid,
            TO_CHAR(
                TO_DATE(SUBSTR(tr1.textresult, 1, 8), 'YYYYMMDD'),
                'DD-MON-YYYY'
            ) AS manufacture_date,
            TO_CHAR(
                TO_DATE(SUBSTR(tr2.textresult, 1, 8), 'YYYYMMDD'),
                DECODE(tr5.textresult, NULL, 'DD-MON-YYYY', tr5.textresult)
            ) AS expiration_date,
            tr3.textresult AS carton_lot,
            tr4.numericalresulttext | | ' ' | | DECODE(tr4.numericalresulttext, NULL, NULL, tr4.unit) AS fill_weight,
            tr6.textresult AS customer_lot,
            tr7.textresult AS po_number,
            tr8.textresult AS number_of_boxes,
            tr9.textresult AS quantity_per_box,
            tr10.textresult AS total_quantity,
            trq.approvedby,
            trq.approvaldate
        FROM
            testrequest trq
            JOIN requestsample rs
            ON rs.requestguid = trq.requestguid AND
            rs.deletion = 'N'
            JOIN physicalsample ps
            ON ps.sampleguid = rs.sampleguid
            JOIN test t
            ON t.requestguid = trq.requestguid AND
            t.testgroup = 'COA' AND
            t.deletion = 'N'
            JOIN testresult tr1
            ON tr1.testguid = t.testguid AND
            tr1.resultid = 'Manufacture Date' AND
            tr1.resultvaluation = 'OK' AND
            tr1.deletion = 'N'
            JOIN testresult tr2
            ON tr2.testguid = t.testguid AND
            tr2.resultid = 'Expiration Date' AND
            tr2.resultvaluation = 'OK' AND
            tr2.deletion = 'N'
            LEFT JOIN testresult tr3
            ON tr3.testguid = t.testguid AND
            tr3.resultid = 'Carton Lot' AND
            tr3.resultvaluation = 'OK' AND
            tr3.deletion = 'N'
            LEFT JOIN testresult tr4
            ON tr4.testguid = t.testguid AND
            tr4.resultid = 'Fill Weight' AND
            tr4.resultvaluation = 'OK' AND
            tr4.deletion = 'N'
            LEFT JOIN testresult tr5
            ON tr5.testguid = t.testguid AND
            tr5.resultid = 'Expiration Date Format' AND
            tr5.resultvaluation = 'OK' AND
            tr5.deletion = 'N'
            LEFT JOIN testresult tr6
            ON tr6.testguid = t.testguid AND
            tr6.resultid = 'Customer Lot' AND
            tr6.resultvaluation = 'OK' AND
            tr6.deletion = 'N'
            LEFT JOIN testresult tr7
            ON tr7.testguid = t.testguid AND
            tr7.resultid = 'PO' AND
            tr7.resultvaluation = 'OK' AND
            tr7.deletion = 'N'
            LEFT JOIN testresult tr8
            ON tr8.testguid = t.testguid AND
            tr8.resultid = 'Number of boxes' AND
            tr8.resultvaluation = 'OK' AND
            tr8.deletion = 'N'
            LEFT JOIN testresult tr9
            ON tr9.testguid = t.testguid AND
            tr9.resultid = 'Quantity per box' AND
            tr9.resultvaluation = 'OK' AND
            tr9.deletion = 'N'
            LEFT JOIN testresult tr10
            ON tr10.testguid = t.testguid AND
            tr10.resultid = 'Total Quantity' AND
            tr10.resultvaluation = 'OK' AND
            tr10.deletion = 'N'
        WHERE
            trq.batchnumber IS NOT NULL AND
            trq.product IS NOT NULL AND
            trq.formulationid IS NOT NULL
    ) coa_results
    ON coa_results.product = trq.product AND
    coa_results.formulationid = trq.formulationid AND
    coa_results.batchnumber = ps.batchnumber AND ( (
            ps.generic01 IS NOT NULL AND
            coa_results.generic01 = ps.generic01
        ) OR
        ps.generic01 IS NULL
    ) AND ( (
            ps.generic04 IS NOT NULL AND
            coa_results.generic04 = ps.generic04
        ) OR
        ps.generic04 IS NULL
    ) --
    LEFT JOIN employee e
    ON e.empid = coa_results.approvedby
    LEFT JOIN domainvalue dv
    ON dv.domainid = 'SM VQ Ship To' AND
    UPPER(dv.value) = UPPER(ps.generic02) AND
    dv.deletion = 'N'
WHERE
    $X{IN,
    trq.requestguid,
    REQUESTGUID}