SELECT * FROM Employee

SELECT * FROM Employee
WHERE Title LIKE 'Sales Support Agent'

UPDATE Employee 
SET FirstName = 'Hello'
WHERE Employee.LastName = 'Adams';

SELECT * FROM Employee;

DELETE FROM Employee
WHERE Employee.LastName = 'King';

SELECT * FROM Employee;

--INSERT INTO Employee(EmployeeID, LastName, FirstName, Title, ReportsTo, BirthDate, HireDate, Address, City, State, Country, PostalCode, Phone, Fax, Email)
--VALUES ('9', 'samadhiya', 'bhoomi', 'software engineer trainee', '4', '2000-07-06', '2024-1-02', 'Indore', 'M.P.', '452001', '9765543145', '652534', 'bhomi@cubexo.com');

--INSERT INTO Employee
--VALUES ('9', 'samadhiya', 'bhoomi', 'software engineer trainee', '4', '2000-07-06', '2024-1-02', 'Indore', 'M.P.', '452001', '9765543145', '652534', 'bhomi@cubexo.com');

SELECT MIN(Employee.LastName)
FROM Employee

SELECT *
FROM Employee
ORDER BY Title ASC 

SELECT HireDate 
FROM Employee
ORDER BY Title DESC 

SELECT COUNT(*)
FROM Employee
WHERE EMPLOYEE.HireDate = '2003-10-17 00:00:00';

SELECT AVG(EmployeeId)
from Employee

