--****PLEASE ENTER YOUR DETAILS BELOW****
--Q1b-tds-dm.sql
--Student ID: 29797802
--Student Name: Germaine Pok Yi Min
--Tutorial No: Friday 11am

drop sequence off_seq;
SET SERVEROUTPUT ON;


/* Comments for your marker:




*/

/*
1b(i) Create a sequence 

(i) Create a sequence which will allow entry of data into the OFFENCE table - the
sequence must begin at 100 and go up in steps of 1 (i.e., the first value is 100, the
next 101, etc.) 

*/
--PLEASE PLACE REQUIRED SQL STATEMENT(S) FOR THIS PART HERE


CREATE SEQUENCE off_seq START WITH 100
INCREMENT BY 1;


/*
1b(ii) Take the necessary steps in the database to record data.

(ii) Lion Lawless of 72 Aberg Avenue Richmond South 3121 (Licence no.: 100389)
has been very inconsiderate of others on the road over the years and has
committed several offences that have been booked by highly vigilant TDS officers
at various different locations. Lion Lawless was riding the same motorbike, a 1994
Red Yamaha FZR600 (JYA3HHE05RA070562) at the time of committing these
offences. Lion Lawless has only committed the offences listed below. The details of
the bookings for Lion are as follows:
*/
--PLEASE PLACE REQUIRED SQL STATEMENT(S) FOR THIS PART HERE

/*
10-Aug-2019 08:04 AM booked for traffic offence “Blood alcohol charge” by
police officer Dolley Hedling (10000011) */


INSERT INTO offence values (off_seq.nextval, TO_DATE('10-Aug-2019 08:04', 'DD-MON-YYYY HH24:MI:SS'), 'Collins St, Melbourne, VIC 3000', 100, 10000011, 100389, 'JYA3HHE05RA070562');

/* On 16-Oct-2019 9:00 PM booked for traffic offence “Level crossing offence”
by police officer Geoff Kilmartin (10000015) */


INSERT INTO offence values (off_seq.nextval, TO_DATE('16-Oct-2019 21:00', 'DD-MON-YYYY HH24:MI:SS'), 'Morris St, South Melbourne, VIC 3205', 101, 10000015, 100389, 'JYA3HHE05RA070562');

/*On 7-Jan-2020 7:07 AM booked for traffic offences “Exceeding the speed
limit by 25 km/h or more” by police officer Geoff Kilmartin (10000015)*/


INSERT INTO offence values (off_seq.nextval, TO_DATE('7-Jan-2020 7:07', 'DD-MON-YYYY HH24:MI:SS'), 'Beacon Rd, Port Melbourne, VIC 3207', 99, 10000015, 100389, 'JYA3HHE05RA070562');

COMMIT;


/*
1b(iii) Take the necessary steps in the database to record changes. 

(iii) Lion Lawless of 72 Aberg Avenue Richmond South 3121 (Licence no.: 100389) had appealed against the “Exceeding the speed limit by 25 km/h or more” offence
he has been alleged to have committed on 07-Jan-2020 at 7:07 AM. 

After careful consideration and taking into account that speed guns at times are not very accurate, TDS has decided to lessen the offence to 
“Exceeding the speed limit by 10 km/h or more but less than 25 km/h" but has strongly warned Lion Lawless to be more careful in future. 
Take the necessary steps in the database to record this change.
*/
--PLEASE PLACE REQUIRED SQL STATEMENT(S) FOR THIS PART HERE


UPDATE offence SET dem_code = 127 WHERE off_no = 102;


COMMIT;



