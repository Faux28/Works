CREATE DATABASE:

1)

CREATE DATABASE suppliers;

---------------------------------------------------------------------------------------------------------------------------

CREATE TABLES:

1)

CREATE TABLE vendors (
            vendor_id SERIAL PRIMARY KEY,
            vendor_name VARCHAR(255) NOT NULL)
            
            
2)

CREATE TABLE parts (
                part_id SERIAL PRIMARY KEY,
                part_name VARCHAR(255) NOT NULL)
                
   
3)

CREATE TABLE part_drawings (
                part_id INTEGER PRIMARY KEY,
                file_extension VARCHAR(5) NOT NULL,
                drawing_data BYTEA NOT NULL,
                FOREIGN KEY (part_id)
                REFERENCES parts (part_id)
                ON UPDATE CASCADE ON DELETE CASCADE)
                
   
4)

CREATE TABLE vendor_parts (
                vendor_id INTEGER NOT NULL,
                part_id INTEGER NOT NULL,
                PRIMARY KEY (vendor_id , part_id),
                FOREIGN KEY (vendor_id)
                    REFERENCES vendors (vendor_id)
                    ON UPDATE CASCADE ON DELETE CASCADE,
                FOREIGN KEY (part_id)
                    REFERENCES parts (part_id)
                    ON UPDATE CASCADE ON DELETE CASCADE)
		    
----------------------------------------------------------------------------------------------------------------------------		    
                    
                    
 CREATE FUNCTION:
 
1)

CREATE OR REPLACE FUNCTION get_vendor_by_parts(
	id integer)
    RETURNS TABLE(vendor_id integer, vendor_name character varying) 

AS $$
BEGIN
 RETURN QUERY

 SELECT vendors.vendor_id,vendors.vendor_name FROM vendors where vendors.vendor_id not in
 (select distinct vendor_parts.vendor_id from vendor_parts where vendor_parts.part_id=id)
 order by vendors.vendor_id;

END; 
$$

LANGUAGE plpgsql;
    
  
  
  
2)

CREATE OR REPLACE FUNCTION get_parts_by_vendor(id integer)
  RETURNS TABLE(part_id INTEGER, part_name VARCHAR) AS
$$
BEGIN
 RETURN QUERY

 SELECT parts.part_id, parts.part_name
 FROM parts
 INNER JOIN vendor_parts on vendor_parts.part_id = parts.part_id
 WHERE vendor_id = id;

END; $$

LANGUAGE plpgsql;
