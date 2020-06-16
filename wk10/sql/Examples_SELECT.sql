--Dar Wright SQL Basics PDX Code Guild SUmmer 2015

--Using CAST

USE SOSAMPLE;

SELECT Price FROM Item

SELECT CAST(Price AS INT) FROM Item

--NULLS

SELECT Description, ItemLookupCode, Notes FROM ITEM
WHERE Notes IS NULL

--Filtering Data with WHERE Clause

--Equal
SELECT Description, ItemLookupCode, Price, Quantity FROM ITEM
WHERE ItemLookupCode = '15100'

--Not Equal
SELECT Description, ItemLookupCode, Price, Quantity FROM ITEM
WHERE ItemLookupCode <> '15100'

--BETWEEN (inclusive)
SELECT Description, ItemLookupCode, Price, Quantity FROM ITEM
WHERE Price BETWEEN 5.00 AND 9.99

--LIKE
SELECT Description, ItemLookupCode, Price, Quantity FROM Item
WHERE Description LIKE 'foot%'

--IN
SELECT Description, ItemLookupCode, Price, Quantity FROM Item
WHERE Price IN (5.00, 149.99)

--AND 
SELECT Description, ItemLookupCode, Price, Quantity FROM ITEM
WHERE ItemLookupCode <> '15100' AND Price < 10

--OR
SELECT Description, ItemLookupCode, Price, Quantity FROM ITEM
WHERE ItemLookupCode = '15100' OR Description NOT LIKE 'Pajamas%'

--More combinations
SELECT Description, ItemLookupCode, Price, Quantity FROM ITEM
WHERE ItemLookupCode = '15100' OR 
	(Description NOT LIKE 'Pajamas%' AND Price < 10)

--Dar Wright SQL Basics PDX Code Guild SUmmer 2015