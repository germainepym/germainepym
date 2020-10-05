--****PLEASE ENTER YOUR DETAILS BELOW****
--Q4-tds-plsql.sql
--Student ID: 29797802
--Student Name: Germaine Pok Yi Min
--Tutorial No: Friday 11am

/* Comments for your marker:




*/

/* (i) Write a trigger which will, from this point forward, automatically maintain the total number of times each police officer 
has booked a driver for a traffic offence attribute you added in Task 3. 
*/
/*Please copy your trigger code and any other necessary SQL statements after this line*/


CREATE OR REPLACE TRIGGER NUM_BOOK
AFTER INSERT OR DELETE ON OFFENCE 
FOR EACH ROW 
BEGIN
    IF INSERTING THEN 
        UPDATE OFFICER
        SET POLICE_BOOK_NUM = POLICE_BOOK_NUM + 1
        WHERE officer_id = :new.officer_id;
    END IF;
    IF DELETING THEN
        UPDATE OFFICER
        SET POLICE_BOOK_NUM = POLICE_BOOK_NUM - 1
        WHERE officer_id = :old.officer_id;
    END IF;
END;
/


---- test harness ----
---- initial data ----
SELECT * FROM OFFICER;
SELECT * FROM OFFENCE;

---- test insert OFFENCE ----
INSERT INTO offence values (103, TO_DATE('23-APR-2020 13:32', 'DD-MON-YYYY HH24:MI:SS'), 'Collins St, Melbourne, VIC 3000', 99, 10000010, 100114, 'SALSF2D42BA702925', 'No');

-- test output --
SELECT * FROM OFFENCE;
SELECT * FROM OFFICER;

-- test delete OFFENCE --
DELETE FROM offence 
WHERE off_no = 103;

-- test output --

SELECT * FROM OFFENCE;
SELECT * FROM OFFICER;

rollback;

/* (ii) Write a trigger which will, from this point forward, make sure that driver and police have at least one name before their data is added into the database. 
The trigger must prevent the insertion if both names are nulls. 
*/
/*Please copy your trigger code and any other necessary SQL statements after this line*/




CREATE OR REPLACE TRIGGER DRIVER_NAME
BEFORE INSERT OR UPDATE ON DRIVER 
FOR EACH ROW 
BEGIN
    IF INSERTING THEN 
        
        IF :NEW.LIC_FNAME IS NOT NULL  AND :NEW.LIC_LNAME IS NOT NULL THEN
        UPDATE DRIVER
        SET LIC_FNAME = :NEW.LIC_FNAME , LIC_LNAME = :NEW.LIC_LNAME
        WHERE LIC_NO = :NEW.LIC_NO;
        
        ELSE raise_application_error (-2000,'At least one name must be provided');
        
    END IF;
    END IF;
END;
/



CREATE OR REPLACE TRIGGER OFFICER_NAME
BEFORE INSERT OR UPDATE ON OFFICER 
FOR EACH ROW 
BEGIN
    IF INSERTING THEN 
        IF :NEW.OFFICER_FNAME IS NOT NULL OR :NEW.OFFICER_LNAME IS NOT NULL THEN
        UPDATE OFFICER
        SET OFFICER_FNAME = :NEW.OFFICER_FNAME , OFFICER_LNAME = :NEW.OFFICER_LNAME
        WHERE OFFICER_ID = :NEW.OFFICER_ID;
        
        ELSE raise_application_error (-2000,'At least one name must be provided');
    END IF;
    END IF;
END;
/

-- test harness --
-- initial data --
SELECT * FROM DRIVER;
SELECT * FROM OFFICER;


-- test insert DRIVER and OFFICER (insert normally) --
INSERT INTO driver VALUES ('108123', 'Dalt', 'Hehe' , '0465216315', '7 Scoville Alley', 'Melbourne', '3000', TO_DATE('24-Sep-1989', 'DD-MON-YYYY'), TO_DATE('5-Jun-2026', 'DD-MON-YYYY'));
INSERT INTO officer VALUES (10000030, 'Germaine', 'Pok', 0);

-- test output -- 
SELECT * FROM DRIVER;
SELECT * FROM OFFICER;


-- test insert DRIVER and OFFICER (both null) --
INSERT INTO driver VALUES ('108124', NULL, NULL, '0425216917', '7 Scoville Alley', 'Melbourne', '3000', TO_DATE('24-Sep-1989', 'DD-MON-YYYY'), TO_DATE('5-Jun-2026', 'DD-MON-YYYY'));
INSERT INTO officer VALUES (10000031, NULL, NULL, 0);

ROLLBACK;


/* (iii) The local government wants to maintain a history of all drivers’ license expiry dates. 
Write a trigger to record the current and new lic_expiry date of a driver’s license whenever there is a change in a driver’s license expiry date. 
The trigger must check if the new licence expiry date is at least 30 months (2.5 years) later than current license expiry date, otherwise it must prevent the change.
Hint: to carry out this task, you need to create another table where the history of all drivers’ license expiry dates is recorded.
In the table, include the licence number, the current expiry date, the new expiry date and the date when the update is done.
*/
/*Please copy your trigger code and any other necessary SQL statements after this line*/

DROP TABLE license_history cascade constraints PURGE;


CREATE TABLE license_history (
    lic_no         CHAR(10) NOT NULL,
    curr_lic_expiry     DATE NOT NULL,
    new_lic_expiry DATE NOT NULL,
    update_date DATE NOT NULL
);

ALTER TABLE license_history ADD CONSTRAINT license_history_pk PRIMARY KEY ( lic_no );


CREATE OR REPLACE TRIGGER LICENSE_EXPIRY
BEFORE INSERT OR UPDATE ON LICENSE_HISTORY
FOR EACH ROW 
BEGIN
IF INSERTING THEN 
   IF  ADD_MONTHS(:NEW.CURR_LIC_EXPIRY, 30) <= :NEW.NEW_LIC_EXPIRY THEN 
       UPDATE DRIVER
       SET LIC_EXPIRY = :NEW.NEW_LIC_EXPIRY
       WHERE LIC_NO = :NEW.LIC_NO;

    ELSE raise_application_error (-2000,'licence expiry date is not at least 30 months (2.5 years) later than current license expiry date');
   END IF;
END IF;
END;
/


-- test harness --
-- initial data --
SELECT * FROM LICENSE_HISTORY;
SELECT * FROM DRIVER;

-- test insert LICENSE_HISTORY (insert date less then 2.5 years) --
INSERT INTO license_history VALUES (100001, TO_DATE('5-Jun-2026', 'DD-MON-YYYY'), TO_DATE('5-August-2026', 'DD-MON-YYYY'), sysdate);

-- test output -- 
SELECT * FROM LICENSE_HISTORY;
SELECT * FROM DRIVER;

-- test insert LICENSE_HISTORY (insert date more or equal then 2.5 years) --
INSERT INTO license_history VALUES (100002, TO_DATE('9-Feb-2029', 'DD-MON-YYYY'), TO_DATE('9-August-2031', 'DD-MON-YYYY'), sysdate);

-- test output -- 
SELECT * FROM LICENSE_HISTORY;
SELECT * FROM DRIVER;


rollback;





