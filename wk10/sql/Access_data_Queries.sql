--Dar Wright SQL Basics PDX Code Guild SUmmer 2015

USE TSQL2012;

--Basic SELECT Clause
SELECT country FROM HR.Employees

--SELECT with DISTINCT
SELECT DISTINCT country from HR.Employees

--SELECT more that one column
SELECT empid, lastname
FROM HR.Employees;

-- ORDER the data 
SELECT empid, lastname
FROM HR.Employees--Query showing GROUP BY and HAVING clauses

USE TSQL2012;

--Basic SELECT Clause
SELECT country FROM HR.Employees

--SELECT with DISTINCT
SELECT DISTINCT country from HR.Employees

--SELECT more that one column
SELECT empid, lastname
FROM HR.Employees;

-- ORDER the data 
SELECT empid, lastname
FROM HR.Employees
ORDER BY empid;

--Concatentate data into one result
SELECT empid, firstname + ' ' + lastname
FROM HR.Employees;

--Column Alias
SELECT empid, firstname + ' ' + lastname AS fullname
FROM HR.Employees;

--Query order is important!
SELECT country, YEAR(hiredate) AS yearhired
FROM HR.Employees
WHERE yearhired >= 2003;

--Logical Query Processing Order
SELECT country, YEAR(hiredate) AS yearhired, COUNT(*) AS numemployees
FROM HR.Employees
WHERE hiredate >= '20030101'
GROUP BY country, YEAR(hiredate)
HAVING COUNT(*) > 1
ORDER BY country, yearhired DESC;

--Dar Wright SQL Basics PDX Code Guild SUmmer 2015