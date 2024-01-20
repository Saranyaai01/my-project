use employees;
show tables;

insert into department values ('d140','software developer'),('d152','testing'),('d213','HR'),('d141','software developer');
alter table department modify dept_no varchar(4);
alter table salaries modify column to_date date;
describe employees_info;
describe dept_emp;
select * from titles;
show tables;
describe titles;
insert into dept_emp values(1552,'d141','2023-01-05','2023-01-30');
insert into employees_info values(1552,'1996-05-13','lavanya','marimuthu','female','2022-05-14');
insert into salaries values(1552,16000,'2023-01-05','2023-01-30');
insert into titles values(1150, 'software developer','2023-01-01','2023-01-30'),(1152,'software developer','2023-01-05','2023-01-30'),(4587,'testing','2023-01-03','2023-01-30'),(6381,'HR','2023-01-02','2023-01-30');
select * from employees_info;
select * from dept_emp;
select * from department; 
select * from salaries;
select * from titles;
alter table employees_info add column ph_no long;
describe employees_info;
update employees_info set ph_no = case emp_no when 1150 then 9856231470 when 1552 then 7896541230 when 4587 then 6541239870 when 6381 then 9230014500 end where emp_no in(1150,1552,4587,6381);
delimiter //
create procedure e1()
begin
select * from employees_info;
end //
delimiter //
create procedure e2()
begin 
select * from salaries;
end //
delimiter // 
create procedure  e5()
begin
select * from dept_emp;
end //
call e1();
call e2();
call e3();
call e4();
call e5();
use employees;




