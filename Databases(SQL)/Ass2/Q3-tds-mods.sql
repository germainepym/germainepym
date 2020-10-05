--****PLEASE ENTER YOUR DETAILS BELOW****
--Q3-tds-mods.sql
--Student ID: 29797802
--Student Name: Germaine Pok Yi Min
--Tutorial No: Friday 11am

DROP TABLE REVOKE_OFF cascade constraints PURGE;
/* Comments for your marker:




*/


/*
3(i) Changes to live database 1
TDS would like to be able to easily determine the total number of times each police officer has booked a driver for a traffic offence. 
Add a new attribute which will record the number of times each officer has booked drivers.
This attribute must be initialised to the correct current number of times each officer has booked drivers based on the data which is currently stored in the system.

*/
--PLEASE PLACE REQUIRED SQL STATEMENTS FOR THIS PART HERE


ALTER TABLE officer 
ADD POLICE_BOOK_NUM NUMBER(3);

UPDATE
    officer 
set
    POLICE_BOOK_NUM =
    (
        select
            count(officer_id)
        from
            offence 
        where
            officer.officer_id = offence.officer_id
    );


/*
3(ii) Changes to live database 2
*/
--PLEASE PLACE REQUIRED SQL STATEMENTS FOR THIS PART HERE




ALTER TABLE offence 
ADD REVOKE_CHECK VARCHAR(3)
DEFAULT 'No';

CREATE TABLE REVOKE_OFF (

    when_revoke DATE NOT NULL,
    officer_revoke VARCHAR(30) NOT NULL,
    reason_revoke VARCHAR(3) NOT NULL);

ALTER TABLE REVOKE_OFF
     add constraint reason_revoke_chk CHECK ( reason_revoke in ('FOS', 'FEU', 'DOU', 'COH', 'EIP'));

ALTER TABLE REVOKE_OFF ADD CONSTRAINT revoke_off_pk PRIMARY KEY ( when_revoke);
     











































