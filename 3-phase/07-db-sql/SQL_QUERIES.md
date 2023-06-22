# SQL Queries


## Keywords

SELECT (args=> names of the columns or * which means all)

FROM  (table_name)

CREATE TABLE <IF NOT EXISTS> (new_table_name) (
  column_name column_type, (repeat)
)

<!-- CHANGE SCHEMA OF TABLE -->
ALTER TABLE (change the structure of the table)
ADD COLUMN column_name column_type (can only add one column at a time)

ALTER TABLE table
DROP COLUMN column_name;


WHERE (boolean) 
WHERE name = "Something"
WHERE column_name like "%term%"/"%term"/"term%"
LIKE => the REGEX of SQL

=   ; == ; IS ; are all the same thing
!=  ; IS NOT; 

<!-- ADDING TO THE db -->

INSERT INTO table (columns)
VALUES (column_values...), (column_values...);

<!-- UPDATING a row in the db -->
UPDATE table
SET column_name = new_value
WHERE (conditional to find row, usually with an id)

<!-- DELETE -->
DROP TABLE table_name

<!-- DELETE a row -->
DELETE FROM table WHERE (find the row)


## Relationships


SELECT (all columns we want from BOTH tables)
FROM table_A
JOIN table_B
ON table_A.table_A_id == table_B.table_A_id;