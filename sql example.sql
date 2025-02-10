create table employees(name char(20),age int);
insert into employees values ('john',25),('adam',27);
select * from employees;

select * from salaries;
#agg-max,min,avg,sum,count
select employeename,totalpay from salaries;
select max(totalpay) from salaries;
select max(totalpay) as tp,EmployeeName,id from salaries group by EmployeeName,id order by tp desc limit 1;
select min(overtimepay)as op,employeename,id from salaries group by employeename,id order by op asc limit 1;
select sum(totalpay)from salaries;
select avg(totalpay)from salaries;
select count(id)from salaries;
select max(totalpay) EmployeeName,id from salaries group by EmployeeName,id order by max(totalpay) desc limit 1;
select count(EmployeeName) from salaries;
select count(EmployeeName) from salaries where year=2011;
select count(EmployeeName) from salaries where jobtitle like 'DEPUTY CHIEF%';
select count(EmployeeName) from salaries where employeename like 'd%';
select count(EmployeeName) from salaries where employeename like 'c%';

select count(employeename) from salaries where employeename like '%CHIEF%';
use akshay;
select count(EmployeeName) from salaries where basepay>15000;


