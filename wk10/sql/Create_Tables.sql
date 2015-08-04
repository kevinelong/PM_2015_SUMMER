--Dar Wright SQL Basics PDX Code Guild SUmmer 2015

--Basic Create
CREATE TABLE Item_Categories (
	categoryid INT IDENTITY(1,1) NOT NULL,
	-- in MS SQL IDENTITY makes the column auto increment, it can take a starting value and an increment amount
	-- in Other SQL Engines the command might look like: ID INT NOT NULL AUTO_INCREMENT
	categoryname NVARCHAR(15) NOT NULL,
	description NVARCHAR(200) NOT NULL
	)
GO

-- Check if tables exists and drop it
IF OBJECT_ID('Item_Categories', 'U') IS NOT NULL
  DROP TABLE Item_Categories;

-- Create Table with Default Values
CREATE TABLE Item_Categories (
	categoryid INT IDENTITY(1,1) NOT NULL,
	categoryname NVARCHAR(15) NOT NULL,
	description NVARCHAR(200) NOT NULL DEFAULT ('')
	)

INSERT INTO Item_Categories (categoryname)
VALUES ('Name here!')
SELECT * FROM Item_Categories

INSERT INTO Item_Categories (categoryname, description)
VALUES ('Name here!', 'Description goes here')
SELECT * FROM Item_Categories

-- ALTER TABLE ADD Column
ALTER TABLE Item_Categories
	ADD extended_Description NVARCHAR(1000) NULL;
GO

SELECT * FROM Item_Categories

-- Check if tables exists and drop it
IF OBJECT_ID('Item_Categories', 'U') IS NOT NULL
  DROP TABLE Item_Categories;

--CREATE TABLE With PRIMARY KEY CONSTRAINT
CREATE TABLE Item_Categories (
	categoryid INT IDENTITY(1,1) NOT NULL,
	categoryname NVARCHAR(15) NOT NULL,
	description NVARCHAR(200) NOT NULL DEFAULT (''),
	deptid INT NOT NULL,
	CONSTRAINT PK_Categories PRIMARY KEY (categoryid)
	)

-- ALTER TABLE ADD Unique CONSTRAINT
ALTER TABLE Item_Categories
	ADD CONSTRAINT UC_Categories UNIQUE (categoryname);
GO

--ALTER TABLE ADD FOREIGN KEY CONSTRAINT
ALTER TABLE Item_Categories
	ADD CONSTRAINT FK_Deptments FOREIGN KEY(deptid)
	REFERENCES Department (ID)

--Query showing PK and FK to return JOINED Data
SELECT Item.Description, Item.Price, Item.DepartmentID,
	Department.ID, Department.Name
FROM Item
	INNER JOIN Department
		ON Item.DepartmentID = Department.ID

--Better Query
SELECT I.Description, I.Price, I.DepartmentID AS DeptID,
	D.ID, D.Name AS [Dept Name]
FROM Item AS I
	INNER JOIN Department AS D
		ON I.DepartmentID = D.ID
WHERE I.Price < 100
ORDER BY Price DESC

--Dar Wright SQL Basics PDX Code Guild SUmmer 2015