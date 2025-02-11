/*
creating database  = create database name;
use database       = use databasename;

create table       = create table name(name char(30),age int,course char(30));
show table details = select * from tablename; or select column name from tablename;

insert values      = insert into name values("akshay",21,"data analyst"),("shiyas",21,"data science");
delete table values= truncate tablename;
aggregate functions = max , min  ,avg , sum , count
  max  =   select max(column name) from salaries;
           select max(totalpay) as tp,EmployeeName,id from salaries group by EmployeeName,id order by tp desc limit 1;
  min  =   select min(overtimepay)as op,employeename,id from salaries group by employeename,id order by op asc limit 1;
  sum  =   select sum(column name)from salaries;
  avg  =   select avg(column name)from salaries;
 count =   select count(column name)from salaries;
           select count(EmployeeName) from salaries where year=2011;
           select count(EmployeeName) from salaries where jobtitle like 'DEPUTY CHIEF%';
           select count(EmployeeName) from salaries where employeename like 'd%';
           select count(EmployeeName) from salaries where employeename like 'c%';
           select count(employeename) from salaries where employeename like '%CHIEF%';
           select count(EmployeeName) from salaries where basepay>15000;

count(distinct)filter multiple values = count(distinct columnname) from salaries;
*/