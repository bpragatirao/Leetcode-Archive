# Write your MySQL query statement below
SELECT MAX(SALARY) as SecondHighestSalary from Employee where salary < (Select max(salary) from Employee);