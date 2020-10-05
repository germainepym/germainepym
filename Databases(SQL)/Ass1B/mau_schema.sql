-- Generated by Oracle SQL Developer Data Modeler 19.2.0.182.1216
--   at:        2020-05-13 13:52:49 MYT
--   site:      Oracle Database 11g
--   type:      Oracle Database 11g
-- id: 29797802
-- name: Germaine Pok 

set echo on
SPOOL mau_schema_output.txt


DROP TABLE artist CASCADE CONSTRAINTS;

DROP TABLE artwork CASCADE CONSTRAINTS;

DROP TABLE customer CASCADE CONSTRAINTS;

DROP TABLE exhibit CASCADE CONSTRAINTS;

DROP TABLE gallery CASCADE CONSTRAINTS;

DROP TABLE mediadesc CASCADE CONSTRAINTS;

DROP TABLE sale CASCADE CONSTRAINTS;

DROP TABLE status CASCADE CONSTRAINTS;

DROP TABLE style CASCADE CONSTRAINTS;

CREATE TABLE artist (
    artist_code            NUMBER(7) NOT NULL,
    artist_given_name      VARCHAR2(50) NOT NULL,
    artist_family_name     VARCHAR2(50) NOT NULL,
    artist_street          VARCHAR2(50) NOT NULL,
    artist_town            VARCHAR2(50) NOT NULL,
    artist_state           VARCHAR2(50) NOT NULL,
    artist_phone           CHAR(10),
    artist_no_of_artwork   NUMBER(7) NOT NULL
);

COMMENT ON COLUMN artist.artist_code IS
    'artist code';

COMMENT ON COLUMN artist.artist_given_name IS
    'given name of artist';

COMMENT ON COLUMN artist.artist_family_name IS
    'family name of artist';

COMMENT ON COLUMN artist.artist_street IS
    'street the artist lives in ';

COMMENT ON COLUMN artist.artist_town IS
    'town the artist lives in';

COMMENT ON COLUMN artist.artist_state IS
    'state the artist lives in';

COMMENT ON COLUMN artist.artist_phone IS
    'phone number of artist';

COMMENT ON COLUMN artist.artist_no_of_artwork IS
    'number of artwork that the artist have with MAU';

ALTER TABLE artist ADD CONSTRAINT artist_pk PRIMARY KEY ( artist_code );

CREATE TABLE artwork (
    artwork_no           NUMBER(7) NOT NULL,
    artist_code          NUMBER(7) NOT NULL,
    artwork_title        VARCHAR2(100) NOT NULL,
    artwork_date_added   DATE NOT NULL,
    artwork_min_price    NUMBER(7, 2) NOT NULL,
    style_artwork        VARCHAR2(50) NOT NULL,
    artwork_media_desc   NUMBER(7) NOT NULL
);

ALTER TABLE artwork ADD CONSTRAINT chk_artwork_min_price CHECK ( artwork_min_price > 0 );

COMMENT ON COLUMN artwork.artwork_no IS
    'artwork number';

COMMENT ON COLUMN artwork.artist_code IS
    'artist code';

COMMENT ON COLUMN artwork.artwork_title IS
    'title of artwork';

COMMENT ON COLUMN artwork.artwork_date_added IS
    'date the artwork was received';

COMMENT ON COLUMN artwork.artwork_min_price IS
    'minimum price the artist is willing to sell the artwork for';

COMMENT ON COLUMN artwork.style_artwork IS
    'style of artwork';

COMMENT ON COLUMN artwork.artwork_media_desc IS
    'lookup table for media description';

ALTER TABLE artwork ADD CONSTRAINT artwork_pk PRIMARY KEY ( artwork_no,
                                                            artist_code );

CREATE TABLE customer (
    cus_id              NUMBER(7) NOT NULL,
    cus_given_name      VARCHAR2(50) NOT NULL,
    cus_family_name     VARCHAR2(50) NOT NULL,
    cus_street          VARCHAR2(50) NOT NULL,
    cus_town            VARCHAR2(50) NOT NULL,
    cus_state           VARCHAR2(50) NOT NULL,
    cus_phone           CHAR(10) NOT NULL,
    cus_business_name   VARCHAR2(100)
);

COMMENT ON COLUMN customer.cus_id IS
    'customer id';

COMMENT ON COLUMN customer.cus_given_name IS
    'given name of customer';

COMMENT ON COLUMN customer.cus_family_name IS
    'family name of customer';

COMMENT ON COLUMN customer.cus_street IS
    'the street the customer lives';

COMMENT ON COLUMN customer.cus_town IS
    'the town the customer lives';

COMMENT ON COLUMN customer.cus_state IS
    'the state the customer lives';

COMMENT ON COLUMN customer.cus_phone IS
    'customer phone number';

COMMENT ON COLUMN customer.cus_business_name IS
    'customer business name';

ALTER TABLE customer ADD CONSTRAINT customer_pk PRIMARY KEY ( cus_id );

CREATE TABLE exhibit (
    exhibit_code               NUMBER(7) NOT NULL,
    exhibit_start_date         DATE NOT NULL,
    exhibit_end_date           DATE NOT NULL,
    exhibit_featured_catalog   VARCHAR2(3) NOT NULL,
    artwork_no                 NUMBER(7) NOT NULL,
    artist_code                NUMBER(7) NOT NULL,
    gallery_id                 NUMBER(7) NOT NULL
);

ALTER TABLE exhibit
    ADD CONSTRAINT chk_featured_catalog CHECK ( exhibit_featured_catalog IN (
        'No',
        'Yes'
    ) );

COMMENT ON COLUMN exhibit.exhibit_code IS
    'surrogate key';

COMMENT ON COLUMN exhibit.exhibit_start_date IS
    'the date the artwork is exhibited';

COMMENT ON COLUMN exhibit.exhibit_end_date IS
    'the date the artwork stops being exhibited';

COMMENT ON COLUMN exhibit.exhibit_featured_catalog IS
    'is the artwork featured in the catalog?';

COMMENT ON COLUMN exhibit.artwork_no IS
    'artwork number';

COMMENT ON COLUMN exhibit.artist_code IS
    'artist code';

COMMENT ON COLUMN exhibit.gallery_id IS
    'gallery id';

ALTER TABLE exhibit ADD CONSTRAINT exhibit_pk PRIMARY KEY ( exhibit_code );

ALTER TABLE exhibit
    ADD CONSTRAINT nk_exhibit UNIQUE ( artwork_no,
                                       artist_code,
                                       gallery_id,
                                       exhibit_start_date );

CREATE TABLE gallery (
    gallery_id              NUMBER(7) NOT NULL,
    gallery_name            VARCHAR2(100) NOT NULL,
    gallery_manager_gname   VARCHAR2(50) NOT NULL,
    gallery_manager_fname   VARCHAR2(50) NOT NULL,
    gallery_street          VARCHAR2(50) NOT NULL,
    gallery_town            VARCHAR2(50) NOT NULL,
    gallery_state           VARCHAR2(50) NOT NULL,
    gallery_open            DATE NOT NULL,
    gallery_close           DATE NOT NULL,
    gallery_phone           CHAR(10) NOT NULL,
    gallery_comission       NUMBER(7) NOT NULL
);

COMMENT ON COLUMN gallery.gallery_id IS
    'gallery id';

COMMENT ON COLUMN gallery.gallery_name IS
    'name of gallery';

COMMENT ON COLUMN gallery.gallery_manager_gname IS
    'given name of the manager of the gallery';

COMMENT ON COLUMN gallery.gallery_manager_fname IS
    'gallery manager family name';

COMMENT ON COLUMN gallery.gallery_street IS
    'street the gallery is on';

COMMENT ON COLUMN gallery.gallery_town IS
    'the town the gallery is located';

COMMENT ON COLUMN gallery.gallery_state IS
    'the state the gallery is located';

COMMENT ON COLUMN gallery.gallery_open IS
    'the time the gallery opens';

COMMENT ON COLUMN gallery.gallery_close IS
    'the time gallery closes';

COMMENT ON COLUMN gallery.gallery_phone IS
    'gallery phone number';

COMMENT ON COLUMN gallery.gallery_comission IS
    'the comission the gallery receives';

ALTER TABLE gallery ADD CONSTRAINT gallery_pk PRIMARY KEY ( gallery_id );

CREATE TABLE mediadesc (
    description_id     NUMBER(7) NOT NULL,
    description_name   VARCHAR2(100) NOT NULL
);

COMMENT ON COLUMN mediadesc.description_id IS
    'lookup table for media description';

COMMENT ON COLUMN mediadesc.description_name IS
    'description name';

ALTER TABLE mediadesc ADD CONSTRAINT mediadesc_pk PRIMARY KEY ( description_id );

CREATE TABLE sale (
    sale_id        NUMBER(7) NOT NULL,
    sale_date      DATE NOT NULL,
    sale_price     NUMBER(7, 2) NOT NULL,
    cus_id         NUMBER(7) NOT NULL,
    exhibit_code   NUMBER(7) NOT NULL
);

ALTER TABLE sale ADD CONSTRAINT chk_saleprice CHECK ( sale_price > 0 );

COMMENT ON COLUMN sale.sale_id IS
    'sale id';

COMMENT ON COLUMN sale.sale_date IS
    'the date the artwork was sold';

COMMENT ON COLUMN sale.sale_price IS
    'the price the artwork was sold for';

COMMENT ON COLUMN sale.cus_id IS
    'customer id';

COMMENT ON COLUMN sale.exhibit_code IS
    'surrogate key';

ALTER TABLE sale ADD CONSTRAINT sale_pk PRIMARY KEY ( sale_id );

CREATE TABLE status (
    status_no        NUMBER(7) NOT NULL,
    status_date      DATE NOT NULL,
    status_artwork   VARCHAR2(15) NOT NULL,
    artwork_no       NUMBER(7) NOT NULL,
    artist_code      NUMBER(7) NOT NULL,
    gallery_id       NUMBER(7)
);

ALTER TABLE status
    ADD CONSTRAINT chk_status_artwork CHECK ( status_artwork IN (
        'DISPLAY',
        'RETURNED',
        'SOLD',
        'TRANSIT',
        'WAREHOUSE'
    ) );

COMMENT ON COLUMN status.status_no IS
    'surrogate key';

COMMENT ON COLUMN status.status_date IS
    'the status of the artwork date';

COMMENT ON COLUMN status.status_artwork IS
    'the status of the artwork';

COMMENT ON COLUMN status.artwork_no IS
    'artwork number';

COMMENT ON COLUMN status.artist_code IS
    'artist code';

COMMENT ON COLUMN status.gallery_id IS
    'gallery id';

ALTER TABLE status ADD CONSTRAINT status_pk PRIMARY KEY ( status_no );

ALTER TABLE status
    ADD CONSTRAINT nk_status UNIQUE ( artwork_no,
                                      artist_code,
                                      status_date );

CREATE TABLE style (
    style_artwork    VARCHAR2(50) NOT NULL,
    style_artwork1   VARCHAR2(50) NOT NULL
);

COMMENT ON COLUMN style.style_artwork IS
    'style of artwork';

COMMENT ON COLUMN style.style_artwork1 IS
    'style of artwork';

ALTER TABLE style ADD CONSTRAINT style_pk PRIMARY KEY ( style_artwork );

ALTER TABLE artwork
    ADD CONSTRAINT artist_artwork FOREIGN KEY ( artist_code )
        REFERENCES artist ( artist_code );

ALTER TABLE exhibit
    ADD CONSTRAINT artwork_exhibit FOREIGN KEY ( artwork_no,
                                                 artist_code )
        REFERENCES artwork ( artwork_no,
                             artist_code );

ALTER TABLE status
    ADD CONSTRAINT artwork_status FOREIGN KEY ( artwork_no,
                                                artist_code )
        REFERENCES artwork ( artwork_no,
                             artist_code );

ALTER TABLE sale
    ADD CONSTRAINT customer_sale FOREIGN KEY ( cus_id )
        REFERENCES customer ( cus_id );

ALTER TABLE sale
    ADD CONSTRAINT exhibit_sale FOREIGN KEY ( exhibit_code )
        REFERENCES exhibit ( exhibit_code );

ALTER TABLE exhibit
    ADD CONSTRAINT gallery_exhibit FOREIGN KEY ( gallery_id )
        REFERENCES gallery ( gallery_id );

ALTER TABLE status
    ADD CONSTRAINT gallery_status FOREIGN KEY ( gallery_id )
        REFERENCES gallery ( gallery_id );

ALTER TABLE artwork
    ADD CONSTRAINT mediadesc_artwork FOREIGN KEY ( artwork_media_desc )
        REFERENCES mediadesc ( description_id );

ALTER TABLE artwork
    ADD CONSTRAINT style_artwork FOREIGN KEY ( style_artwork )
        REFERENCES style ( style_artwork );

ALTER TABLE style
    ADD CONSTRAINT style_parentchild FOREIGN KEY ( style_artwork1 )
        REFERENCES style ( style_artwork );

SPOOL off
set echo off

-- Oracle SQL Developer Data Modeler Summary Report: 
-- 
-- CREATE TABLE                             9
-- CREATE INDEX                             0
-- ALTER TABLE                             25
-- CREATE VIEW                              0
-- ALTER VIEW                               0
-- CREATE PACKAGE                           0
-- CREATE PACKAGE BODY                      0
-- CREATE PROCEDURE                         0
-- CREATE FUNCTION                          0
-- CREATE TRIGGER                           0
-- ALTER TRIGGER                            0
-- CREATE COLLECTION TYPE                   0
-- CREATE STRUCTURED TYPE                   0
-- CREATE STRUCTURED TYPE BODY              0
-- CREATE CLUSTER                           0
-- CREATE CONTEXT                           0
-- CREATE DATABASE                          0
-- CREATE DIMENSION                         0
-- CREATE DIRECTORY                         0
-- CREATE DISK GROUP                        0
-- CREATE ROLE                              0
-- CREATE ROLLBACK SEGMENT                  0
-- CREATE SEQUENCE                          0
-- CREATE MATERIALIZED VIEW                 0
-- CREATE MATERIALIZED VIEW LOG             0
-- CREATE SYNONYM                           0
-- CREATE TABLESPACE                        0
-- CREATE USER                              0
-- 
-- DROP TABLESPACE                          0
-- DROP DATABASE                            0
-- 
-- REDACTION POLICY                         0
-- 
-- ORDS DROP SCHEMA                         0
-- ORDS ENABLE SCHEMA                       0
-- ORDS ENABLE OBJECT                       0
-- 
-- ERRORS                                   0
-- WARNINGS                                 0