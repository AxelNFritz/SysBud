-- SQLite
-- SELECT * FROM dryck_utbud WHERE producent like '%Fuller%';
-- SELECT varugrupp, typ FROM dryck_utbud WHERE varugrupp='Öl' GROUP BY typ;
-- SELECT varugrupp, typ FROM dryck_utbud WHERE varugrupp='Vitt vin' GROUP BY typ;
SELECT * FROM dryck_utbud WHERE land='Portugal' AND varugrupp='Rött vin' AND namn1 LIKE '%D%'; -- AND land='Potrugal'; -- AND varugrupp='Rött vin';