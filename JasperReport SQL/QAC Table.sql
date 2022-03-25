SELECT
    t.testguid,
    trq.product,
    trq.formulationid,
    br1.textresult AS number_of_boxes,
    br2.textresult AS quantity_per_box,
    br3.textresult AS total_quantity
FROM
    testrequest trq
    JOIN test t
        ON t.requestguid = trq.requestguid AND
        t.testgroup = 'COA' AND
        t.deletion = 'N'
    JOIN testresult br1
        ON br1.testguid = t.testguid AND
        br1.resultid = 'Number of boxes' AND
        br1.resultvaluation = 'OK' AND
        br1.deletion = 'N'
    JOIN testresult br2
        ON br2.testguid = t.testguid AND
        br2.resultid = 'Quantity per box' AND
        br2.resultvaluation = 'OK' AND
        br2.deletion = 'N'
    JOIN testresult br3
        ON br3.testguid = t.testguid AND
        br3.resultid = 'Total Quantity' AND
        br3.resultvaluation = 'OK' AND
        br3.deletion = 'N'
WHERE
    trq.batchnumber IS NOT NULL AND
    trq.product IS NOT NULL AND
    trq.formulationid IS NOT NULL

