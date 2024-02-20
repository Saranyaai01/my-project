
use ai_saranya;
show tables;
create table Loginpage(user_name varchar(50) not null, password varchar(50) not null);
insert into  loginpage  values ("jaya", "jay@123");
create table student_Database(ID int primary key auto_increment,name varchar(200) not null , language1 varchar(100), language2 varchar(120), mathematics varchar(120), science varchar(120), socialscience varchar(120));
insert into student_Database values (4,"lavanya",98,99,96,97,95);
select * from student_Database;


