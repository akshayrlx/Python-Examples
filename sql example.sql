create table employees(name char(20),age int);
insert into employees values ('john',25),('adam',27);
select * from employees;

select * from salaries;
#agg-max,min,avg,sum,count
select employeename,totalpay from salaries;
select max(basepay) from salaries;
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
select count(distinct jobtitle) from salaries;
select * from example1;

select count(a) from example1;
select sum(a) from example1;
select max(a) b,c from example1 group by b,c order by max(a) desc limit 1;
select max(a) from example1 where c>5;
select * from banklist;
select * from salaries;

select  distinct jobtitle, count(employeename)jobtitle from salaries group by jobtitle order by count(employeename) desc;

select count(employeename) from salaries where basepay>10000 and overtimepay<1000;

select count(employeename)from salaries where totalpay>100000 and totalpay<200000;
select count(employeename)from salaries where totalpay between 100000 and 200000;
