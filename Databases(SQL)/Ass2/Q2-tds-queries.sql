--****PLEASE ENTER YOUR DETAILS BELOW****
--Q2-tds-queries.sql
--Student ID: 29797802
--Student Name: Germaine Pok Yi Min
--Tutorial No: Friday 11am

/* Comments for your marker:




*/


/*
2(i) Query 1

*/

--PLEASE PLACE REQUIRED SQL STATEMENT FOR THIS PART HERE


SELECT dem_points AS "Demerit Points", dem_description AS "Demerit Description"
FROM demerit
WHERE (dem_description LIKE 'Exceed%' OR dem_description LIKE '%heavy%' OR dem_description LIKE '%Heavy%')
ORDER BY dem_points;


/*
2(ii) Query 2
*/
--PLEASE PLACE REQUIRED SQL STATEMENT FOR THIS PART HERE

SELECT VEH_MAINCOLOR AS "Main colour", VEH_VIN AS VIN, to_char(VEH_YRMANUF, 'YYYY') as "Year Manufactured"
FROM VEHICLE
WHERE VEH_MODNAME = 'Range Rover' OR VEH_MODNAME = 'Range Rover Sport' 
GROUP BY veh_vin,veh_maincolor, veh_yrmanuf
HAVING to_char(VEH_YRMANUF, 'YYYY') between '2012' AND '2014' 
ORDER BY VEH_YRMANUF DESC, VEH_MAINCOLOR;


/*
2(iii) Query 3

*/
--PLEASE PLACE REQUIRED SQL STATEMENT FOR THIS PART HERE

SELECT d.lic_no AS "Licence No.",
        d.lic_fname || ' ' || d.lic_lname AS "Driver Fullname", 
        to_char(d.lic_dob,'DD-MON-YYYY') AS DOB, 
        d.lic_street || ' ' || d.lic_town || ' ' || d.lic_postcode AS "Driver Address", 
        s.sus_date AS "Suspended On", 
        s.sus_enddate AS "Suspended Till"
FROM driver d join suspension s on d.lic_no = s.lic_no
WHERE sus_date between ADD_MONTHS(sysdate, -30) and sysdate
ORDER BY d.lic_no;


/*
2(iv) Query 4
*/
--PLEASE PLACE REQUIRED SQL STATEMENT FOR THIS PART HERE

SELECT d.dem_code AS "Demerit Code", d.dem_description AS "Demerit Description", count(o.dem_code) AS "Total Offences (All Months)",
        sum(case when TO_CHAR(o.off_datetime, 'MON') ='JAN' then 1 else 0 end) AS "Jan",
        sum(case when TO_CHAR(o.off_datetime, 'MON') ='FEB' then 1 else 0 end) AS "Feb",
        sum(case when TO_CHAR(o.off_datetime, 'MON') ='MAR' then 1 else 0 end) AS "Mar",
        sum(case when TO_CHAR(o.off_datetime, 'MON') ='APR' then 1 else 0 end) AS "Apr",
        sum(case when TO_CHAR(o.off_datetime, 'MON') ='MAY' then 1 else 0 end) AS "May",
        sum(case when TO_CHAR(o.off_datetime, 'MON') ='JUN' then 1 else 0 end) AS "Jun",
        sum(case when TO_CHAR(o.off_datetime, 'MON') ='JUL' then 1 else 0 end) AS "Jul",
        sum(case when TO_CHAR(o.off_datetime, 'MON') ='AUG' then 1 else 0 end) AS "Aug",
        sum(case when TO_CHAR(o.off_datetime, 'MON') ='SEP' then 1 else 0 end) AS "Sep",
        sum(case when TO_CHAR(o.off_datetime, 'MON') ='OCT' then 1 else 0 end) AS "Oct",
        sum(case when TO_CHAR(o.off_datetime, 'MON') ='NOV' then 1 else 0 end) AS "Nov",
        sum(case when TO_CHAR(o.off_datetime, 'MON') ='DEC' then 1 else 0 end) AS "Dec"

        
FROM demerit d left outer join offence o on d.dem_code = o.dem_code
GROUP BY d.dem_code, d.dem_description
ORDER BY count(o.dem_code) DESC, d.dem_code;

/*
2(v) Query 5
*/
--PLEASE PLACE REQUIRED SQL STATEMENT FOR THIS PART HERE


SELECT v.veh_manufname AS "Manufacturer Name", count(o.dem_code) AS "Total Number of Offences"
FROM ((vehicle v join offence o on v.veh_vin = o.veh_vin) join demerit d on d.dem_code = o.dem_code)
WHERE d.dem_code > 1
GROUP BY v.veh_manufname
ORDER BY count(o.dem_code) DESC, v.veh_manufname;


/*
2(vi) Query 6

*/
--PLEASE PLACE REQUIRED SQL STATEMENT FOR THIS PART HERE

SELECT o.lic_no AS "Licence No.", d.lic_fname || ' ' || d.lic_lname AS "Driver Name", o.officer_id AS "Officer ID", 
f.officer_fname || ' ' || f.officer_lname AS "Officer Name"
FROM ((driver d join offence o on d.lic_no = o.lic_no) join officer f on o.officer_id = f.officer_id)
WHERE d.lic_lname = f.officer_lname
GROUP BY o.lic_no, d.lic_fname, d.lic_lname, o.officer_id, f.officer_fname, f.officer_lname
HAVING count(o.dem_code) > 1
ORDER BY o.lic_no;



/*
2(vii) Query 7
*/
--PLEASE PLACE REQUIRED SQL STATEMEN FOR THIS PART HERE

SELECT d.dem_code AS "Demerit Code", d.dem_description AS "Demerit Description", dr.lic_no AS "Licence No.", 
dr.lic_fname || ' ' || dr.lic_lname AS "Driver Name", count(d.dem_code) AS "Total Times Booked"
FROM ((demerit d join offence o on d.dem_code = o.dem_code) join driver dr on o.lic_no = dr.lic_no)

GROUP BY d.dem_code, d.dem_description, dr.lic_no, dr.lic_fname, dr.lic_lname
                         
ORDER BY d.dem_code, dr.lic_no;


/*

2(viii) Query 8

*/
--PLEASE PLACE REQUIRED SQL STATEMENT FOR THIS PART HERE


SELECT (CASE
        WHEN v.veh_vin >= 'A' and v.veh_vin < 'D' THEN
            'Africa'
        WHEN v.veh_vin >= 'J' and v.veh_vin < 'S' THEN
            'Asia'
        WHEN v.veh_vin >= 'S' and v.veh_vin < 'Z' OR v.veh_vin LIKE 'Z%' THEN
            'Europe'
        WHEN v.veh_vin > '0' and v.veh_vin < '6' THEN
            'North America'
        WHEN v.veh_vin LIKE '6%' OR v.veh_vin LIKE '7%' THEN
            'Oceania'
        WHEN v.veh_vin LIKE '8%' OR v.veh_vin LIKE '9%' THEN
            'South America'
        ELSE
            'Unknown'
    END) AS Region,
   
    count(v.veh_manufname) AS "Total Vehicles Manufactured" ,
                       
    TO_CHAR((count(v.veh_manufname) / countt*100), '90.99') || '%'  AS "Percentage of Vehicle Manufactured"
               
FROM Vehicle v , (select count(v.veh_manufname) as countt from Vehicle v)
   


GROUP BY (CASE
        WHEN v.veh_vin >= 'A' and v.veh_vin < 'D' THEN
            'Africa'
        WHEN v.veh_vin >= 'J' and v.veh_vin < 'S' THEN
            'Asia'
         WHEN v.veh_vin >= 'S' and v.veh_vin < 'Z' OR v.veh_vin LIKE 'Z%' THEN
            'Europe'
         WHEN v.veh_vin > '0' and v.veh_vin < '6' THEN
            'North America'
         WHEN v.veh_vin LIKE '6%' OR v.veh_vin LIKE '7%' THEN
            'Oceania'
         WHEN v.veh_vin LIKE '8%' OR v.veh_vin LIKE '9%' THEN
            'South America'
        ELSE
            'Unknown'
    END ), countt


   
UNION
       
       SELECT 'Total', count(v.veh_manufname), to_char((count(v.veh_manufname) / countt*100) , '990.99') || '%'
       
        FROM Vehicle v, (select count(v.veh_manufname) as countt from Vehicle v)
       
        GROUP BY countt 

ORDER BY 2,3;



