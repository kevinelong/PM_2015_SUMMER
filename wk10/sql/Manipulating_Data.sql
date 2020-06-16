--Dar Wright SQL Basics PDX Code Guild SUmmer 2015

--Create table to show DML
USE TSQL2012;
IF OBJECT_ID(N'Sales.MyOrders', N'U') IS NOT NULL DROP TABLE Sales.MyOrders;
GO

CREATE TABLE Sales.MyOrders
(
  orderid INT NOT NULL IDENTITY(1, 1)
    CONSTRAINT PK_MyOrders_orderid PRIMARY KEY,
  custid  INT NOT NULL,
  empid   INT NOT NULL,
  orderdate DATE NOT NULL
    CONSTRAINT DFT_MyOrders_orderdate DEFAULT (CAST(SYSDATETIME() AS DATE)),
  shipcountry NVARCHAR(15) NOT NULL,
  freight MONEY NOT NULL
);

--INSERT row
INSERT INTO Sales.MyOrders(custid, empid, orderdate, shipcountry, freight)
  VALUES(2, 19, '20120620', N'USA', 30.00);

--See the table data
SELECT * FROM Sales.MyOrders

--INSERT Default by not listing column 
INSERT INTO Sales.MyOrders(custid, empid, shipcountry, freight)
  VALUES(3, 11, N'USA', 10.00);

--See the table data
SELECT * FROM Sales.MyOrders

--INSERT Excplict DEFAULT value
INSERT INTO Sales.MyOrders(custid, empid, orderdate, shipcountry, freight)
  VALUES(3, 17, DEFAULT, N'USA', 30.00);

--See the table data
SELECT * FROM Sales.MyOrders

--INSERT multiple rows
INSERT INTO Sales.MyOrders(custid, empid, orderdate, shipcountry, freight) VALUES
  (2, 11, '20120620', N'USA', 50.00),
  (5, 13, '20120620', N'USA', 40.00),
  (7, 17, '20120620', N'USA', 45.00);

--See the table data
SELECT * FROM Sales.MyOrders

--INSERT SELECT
INSERT INTO Sales.MyOrders(custid, empid, orderdate, shipcountry, freight)
	SELECT custid, empid, orderdate, shipcountry, freight 
	FROM Sales.Orders
	WHERE shipcountry = N'Norway';

--See the table data
SELECT * FROM Sales.MyOrders

--SELECT INTO
IF OBJECT_ID(N'Sales.MyOrders', N'U') IS NOT NULL DROP TABLE Sales.MyOrders;

SELECT orderid, custid, orderdate, shipcountry, freight
INTO Sales.MyOrders
FROM Sales.Orders
WHERE shipcountry = N'Norway';

--See the table data
SELECT * FROM Sales.MyOrders

--UPDATE -------------------

-- sample data for UPDATE and DELETE sections
IF OBJECT_ID(N'Sales.MyOrderDetails', N'U') IS NOT NULL
  DROP TABLE Sales.MyOrderDetails;
IF OBJECT_ID(N'Sales.MyOrders', N'U') IS NOT NULL
  DROP TABLE Sales.MyOrders;
IF OBJECT_ID(N'Sales.MyCustomers', N'U') IS NOT NULL
  DROP TABLE Sales.MyCustomers;

SELECT * INTO Sales.MyCustomers FROM Sales.Customers;
ALTER TABLE Sales.MyCustomers
  ADD CONSTRAINT PK_MyCustomers PRIMARY KEY(custid);

SELECT * INTO Sales.MyOrders FROM Sales.Orders;
ALTER TABLE Sales.MyOrders
  ADD CONSTRAINT PK_MyOrders PRIMARY KEY(orderid);

SELECT * INTO Sales.MyOrderDetails FROM Sales.OrderDetails;
ALTER TABLE Sales.MyOrderDetails
  ADD CONSTRAINT PK_MyOrderDetails PRIMARY KEY(orderid, productid);

--SELECT some data to look at before updating
SELECT * FROM Sales.MyOrderDetails
WHERE orderid = 10251;

--UPDATE Data (add 5% discount
UPDATE Sales.MyOrderDetails
	SET discount += 0.05
WHERE orderid = 10251;

--UPDATE data (undo the 5% disocunt)
UPDATE Sales.MyOrderDetails
	SET discount -= 0.05
WHERE orderid = 10251;

--UPDATE without a WHERE clause is a R.G.E. (Resume Generating Event) 


----- DELETE ----------------------------------------------

--DELETE without a WHERE clause is a R.G.E. (Resume Generating Event) 

--DELETE rows from a table
SELECT * FROM Sales.MyOrderDetails WHERE productid BETWEEN 10 AND 12 --ORDER BY productid ASC
DELETE FROM Sales.MyOrderDetails
WHERE productid = 11;


---------------TRUNCATE --------------------------------
TRUNCATE TABLE Sales.MyOrderDetails


--Dar Wright SQL Basics PDX Code Guild SUmmer 2015