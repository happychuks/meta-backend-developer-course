--Select Statement
SELECT column1, column2 FROM your_table_name WHERE your_condition;

--Insert statement
INSERT INTO your_table_name (column1, column2) VALUES (value1, value2);

--Update statement
UPDATE your_table_name SET column1 = value1 WHERE your_condition;

--Delete statement
DELETE FROM your_table_name WHERE your_condition;

--Create Table statement
CREATE TABLE your_table_name (
    column1 datatype1,
    column2 datatype2,
    ...
);

CREATE TABLE Students (
    StudentID INT PRIMARY KEY,
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    Age INT
);

--Alter Table statement
ALTER TABLE your_table_name ADD COLUMN new_column datatype;

--Drop Table statement
DROP TABLE your_table_name;

--Orderby clause
SELECT * FROM your_table_name ORDER BY column_name ASC;

--Groupby clause
SELECT column1, COUNT(column2) FROM your_table_name GROUP BY column1;

