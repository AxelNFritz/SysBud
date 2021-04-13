-- SQLite
-- SELECT * FROM dryck_utbud WHERE producent like '%Fuller%';
-- SELECT varugrupp, typ FROM dryck_utbud WHERE varugrupp='Öl' GROUP BY typ;
-- SELECT varugrupp, typ FROM dryck_utbud WHERE varugrupp='Vitt vin' GROUP BY typ;
SELECT varugrupp FROM dryck_utbud GROUP BY varugrupp;