-- SQLite
CREATE TABLE dryck_utbud(
    Nr INT(10) NOT NULL,
    namn1 VARCHAR(50) NOT NULL,
    namn2 VARCHAR(60),
    pris DOUBLE(20) NOT NULL,
    volym INT(10) NOT NULL,
    prisperliter DOUBLE(10) NOT NULL,
    varugrupp VARCHAR(20) NOT NULL,
    typ VARCHAR(25),
    stil VARCHAR(25),
    land VARCHAR(20) NOT NULL,
    producent VARCHAR(20) NOT NULL,
    alk DOUBLE(10) NOT NULL,
    PRIMARY KEY(Nr)
);