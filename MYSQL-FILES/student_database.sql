
use ai_saranya;
show tables;
create table demo(reg_no int  not null, name varchar(50) not null);
insert into   values ("jaya", "jay@123");
create table student_Database(ID int primary key auto_increment,name varchar(200) not null , language1 varchar(100), language2 varchar(120), mathematics varchar(120), science varchar(120), socialscience varchar(120));
insert into student_Database values (4,"lavanya",98,99,96,97,95);
select * from demo;
create table pymysql(book_id int not null primary key,book_name varchar(60) not null,author varchar(50) not null, edition varchar(50) not null,price int not null,quantity int not null);
create table studentmark_list(name varchar(50),age int,tamil varchar(50),english varchar(50),maths varchar(50),physics varchar(50),chemistry varchar(50),computer_science varchar(50));

select * from pymysql;
create table  borrow_record(book_id int not null primary key,book_name varchar(50) not null,student_roll varchar(50) not null,student_name varchar(50) not null, course varchar(50) not null,subject varchar(50) not null, issue_date date not null, return_date date not null);
select * from borrow_record;