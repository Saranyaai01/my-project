create database Amazon_DB;
drop database ai_saranya;
use Amazon_DB;
create table user_info
(user_id int not null primary key, first_name varchar(50) not null,
 middle_name varchar(50), 
last_name varchar(50) not null, 
dob date, 
phone_no long, 
user_name varchar(10) not null unique, 
passworld varchar(18) not null
);
create table user_login
(login_id int not null primary key,
user_name varchar(10) not null unique,
pasword varchar(18) not null,
new_password varchar(18),
user_id int not null, 
foreign key(user_id) references user_info(user_id)
);
create table order_details
(order_id int not null primary key,
product_id varchar(20),
product_name varchar(50) not null,
product_price double not null,
product_quantity int not null,
delivery_address varchar(200) not null,
order_date date,
shipping_date date,
shipping_fee double,
discount double,
total_amount double,
payment_mode varchar(30)
);
create table category
(product_category varchar(50)
);
create table product_details
(product_id int not null primary key,
product_category varchar(50),
product_name varchar(50),
brand_name varchar(50),
product_price double,
product_rating varchar(10)
);
show tables;
describe product_details;
insert into user_info values( 105, 'dharani',' ','arun','2001-01-21',9787317001,'dharani_01','dharani@21');
select * from user_info;
select * from user_login;
select * from order_details;
select * from product_details;
select * from category;
insert into user_info values(110,'dikshith',' kumar','krishnan','2001-01-12',9797971200,'dikskumar','dhikshi@12');
insert into user_login values(489, 'dikshkumar','dhikshi@12',' ',110);
insert into order_details values(10025,'esr502','shoes',2000,1, 'trichy','2005-11-18','2005-11-19',60,15,1910,'cash on delivery');
insert into product_details values('esr502','mens accessories','shoes','buma',2000,'3 *');
insert into category values('womens'),('mens'),('kids'),('home applience'),('womens accessories'),('mens accessories'),('electronic devices'),('computer devices');
select * from user_info right join user_login on user_info.user_id = user_login.user_id;
select * from product_details left join order_details on product_details . product_id = order_details . product_id;
alter table  product_details add column details_id int;


delete from product_details where product_id in (10021,10023,10024,10025);
alter table product_details drop column details_id; 
alter table order_details modify column details_id int not null;
update user_login set created_by = 
case login_id
when 480 then 'harini'
when 481 then 'priya'
when 482 then 'jothi'
when 483 then 'sankavi'
when 484 then 'dharani'
when 485 then 'janani'
when 486 then 'ramya'
when 487 then 'arun'
when 488 then 'nikkil'
when 489 then 'dikshith'
end ,
 modified_by =
 case login_id
when 480 then 'harini'
when 481 then 'priya'
when 482 then 'jothi'
when 483 then 'sankavi'
when 484 then 'dharani'
when 485 then 'janani'
when 486 then 'ramya'
when 487 then 'arun'
when 488 then 'nikkil'
when 489 then 'dikshith'
end,
created_on =
case login_id
when 480 then '2023-12-15 10:58:30'
when 481 then '2023-12-15 10:58:30'
when 482 then '2023-12-15 10:58:30'
when 483 then '2023-12-09 10:58:30'
when 484 then '2023-12-10 10:00:30'
when 485 then '2023-12-11 10:18:30'
when 486 then '2023-12-12 10:28:30'
when 487 then '2023-12-13 10:30:30'
when 488 then '2023-12-14 12:15:30'
when 489 then '2023-12-15 11:58:40'
end,
modified_on =
case login_id
when 480 then '2023-12-15 10:58:30'
when 481 then '2023-12-15 10:58:30'
when 482 then '2023-12-15 10:58:30'
when 483 then '2023-12-09 10:58:30'
when 484 then '2023-12-10 10:00:30'
when 485 then '2023-12-11 10:18:30'
when 486 then '2023-12-12 10:28:30'
when 487 then '2023-12-13 10:30:30'
when 488 then '2023-12-14 12:15:30'
when 489 then '2023-12-15 11:58:40'
end


 
alter table order_details add foreign key (details_id)  references  product_details (product_id);
select * from user_info u1 , user_login l2;
select * from user_info u1 outer join user_login l2 on u1.user_id= l2. user_id;
select * from product_details p1, order_details o1;
select * from order_details o1 left join product_details p1 on o1.order_id = p1.product_id;
alter table user_login add column created_by varchar(50), add column modified_by varchar(50), add column created_on datetime, add column modified_on datetime;
describe order_details;
describe product_details;
describe user_login;
alter table order_details modify column details_id int , add constraint foriegn key (details_id) references product_details(product_id);
alter table order_details drop column details_id;
alter table product_details  add constraint foreign key(details_id) references order_details(order_id) ;
alter table product_details add column details_id int;
update product_details set details_id = 
case product_id
when 'dsq254' then 10021
when 'esr502' then 10022
when 'kfs456' then 10023
when 'prq369' then 10024
when 'svc123400' then 10025
end 
create table ai_batch01
(
SNO int not null primary key,
first_Name varchar(50) not null, 
middle_Name varchar(50),
last_Name varchar(50),
DOB date ,
Aadhar_Number long ,
Biometric_ID long ,
Primary_Contact_No long ,
Secondary_Contact_No long ,
WhatsApp_No long ,
User_name varchar(50) not null,
Password varchar(50) not null,
UG varchar(50),
Subject_Group varchar(50),
PG varchar(50),
Subject varchar(50),
Year_of_Passing int,
AI_Batch_Email varchar(70),
Email varchar(70),
Address varchar(250),
District varchar(50),
Father_Name varchar(60),
 Husband_Name varchar(60),
 Mother_Name varchar(60));
insert into ai_batch01 values
(3,'Aysha sithika L',' ',' ','1988-11-01',784654756225	,54756225,	8124823036,	8610353074,	8124823036,	'TI2023F-C01E78D','Password@123',12	,'Computer science',' ',' ',2005,'aslamshabeen@gmail.com','aslamshabeen@gmail.com','LIGII 2801 BISMILLAH MANZIL Anna nagar phase 2 Navalpattu Trichy -26','Trichy',' ','Nazrul Islam',
	'Amthul jabeen'
);












