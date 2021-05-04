-- SQLite
-- SELECT * FROM dryck_utbud WHERE producent like '%Fuller%';
-- SELECT varugrupp, typ FROM dryck_utbud WHERE varugrupp='Öl' GROUP BY typ;
-- SELECT varugrupp, typ FROM dryck_utbud WHERE varugrupp='Vitt vin' GROUP BY typ;
-- SELECT * FROM dryck_utbud WHERE land='Portugal' AND varugrupp='Rött vin' AND namn1 LIKE '%D%';
-- SELECT * FROM dryck_utbud ORDER BY prisperliter DESC LIMIT 10;


SELECT * FROM dryck_utbud WHERE namn1 LIKE '%%' ORDER BY alk DESC LIMIT 20; -- TOP 10


--SELECT * FROM dryck_utbud WHERE namn1 LIKE '%Da%' (AND varugrupp='Rött vin') (ORDER BY alk DESC);


SELECT * FROM dryck_utbud WHERE namn1 LIKE '%()%' (AND varugrupp='Rött vin') ... (ORDER BY alk DESC) (LIMIT 20);