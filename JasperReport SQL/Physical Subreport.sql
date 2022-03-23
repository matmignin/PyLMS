SELECT tr.resultid AS testing,
  DECODE(tr.resulttype,NULL,NULL,DECODE(tr.requirement, NULL, t.requirement, tr.requirement)) AS specification_range,
  CASE
  WHEN tr.resulttype = 'NUMERIC' AND tr.status = 70 THEN
    tr.numericalresulttext||DECODE(tr.unit,NULL,NULL,' '||tr.unit)
  WHEN tr.resulttype IN ('LIST','TEXT') AND tr.status = 70 THEN
    tr.textresult||DECODE(tr.unit,NULL,NULL,' '||tr.unit)
  WHEN tr.status = 10 THEN
    'pending'
  WHEN tr.resulttype = 'FREETEXT' THEN
    tr.textresult
  ELSE
    'Not Tested'
  END AS result,
  sm.description AS method,
  tr.generic01   AS notebook_ref
FROM (
  SELECT DISTINCT ps.sampleguid, ps.batchnumber, ps.formulationid
  FROM physicalsample ps
  JOIN testresult tr ON tr.sampleguid = ps.sampleguid AND tr.deletion = 'N'
  JOIN test t ON t.testguid = tr.testguid AND UPPER(t.testgroup) = 'PHYSICAL' AND t.deletion = 'N'
  WHERE ps.batchnumber IS NOT NULL AND ps.deletion = 'N'
) psi
JOIN testresult tr ON tr.sampleguid = psi.sampleguid AND tr.deletion = 'N'
JOIN test t ON t.testguid = tr.testguid AND UPPER(t.testgroup) = 'PHYSICAL' AND t.deletion = 'N'
LEFT JOIN smmethod sm ON sm.methodid   = t.methodid AND sm.versionno = t.methodversionno AND sm.deletion  = 'N'
LEFT JOIN physicalsample ps ON ps.sampleguid = psi.sampleguid
LEFT JOIN specificationtestresult str ON str.specificationid = ps.specificationid AND str.versionno = ps.specificationversionno AND str.testid = t.testid AND str.resultid = tr.resultid AND str.deletion = 'N'
LEFT JOIN specificationtest st ON st.specificationid = str.specificationid AND st.versionno = str.versionno AND st.testguid = str.testguid
WHERE (st.deletion IS NULL OR (st.deletion IS NOT NULL AND st.deletion = 'N'))
AND $X{ EQUAL ,psi.batchnumber, PHYSBATCHNUMBER}
ORDER BY DECODE(st.seqno,NULL,t.seqno,NULL), DECODE(str.seqno,NULL,tr.sequencenumber,str.seqno)