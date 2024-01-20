create database ai_saranya;
use ai_saranya;
create table batch01_details 
(
SNO int not null primary key,
first_Name varchar(50) not null, 
middle_Name varchar(50) not null,
last_Name varchar(50) not null,
DOB date not null,
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
 
 create table system_info(
SNO int not null primary key,
details_id int not null,
Name varchar(50),
System_no int,	
ERROR varchar(50),	
OS_Name varchar(50),	
RAM	varchar(50),	
PROCESSOR varchar(70),	
Mouse_Condition varchar(50),	
Keyboard_Condition varchar(50),
foreign key (details_id) references batch01_details (sno)) ;

insert into system_info values(13 ,13,'Kayalvizhi M  ',1,'visual C++2019 ','Windows 7 Ultimate ','4.00 GB ','INTEL CORE i3 ','Working ', 'working ');
insert into system_info values(22 ,22,'Sangari S  ',2,'Working ','windows 8.1 pro ','2.00 GB ','INTEL Pentium ','working ', 'Working ');
insert into system_info values(10 ,10,'Jayalakshmi R  ',3,'working ','windows 8.1 pro ','4.00 GB ','INTEL CORE i3 ','working ', 'working ');
insert into system_info values(5 ,5,'Fathima M  ',4,'visual C++ 2019 ','windows 7 ultimate  ','2.00GB ','Intel Core  i3 ','working ', 'working ');
insert into system_info values(15 ,15,'LAVANYA M   ',5,'visual C++ 2019 ','Windows 7 Ultimate ','4.00 GB ','Intel Core i3 ','Working ', 'Working ');
insert into system_info values(4 ,4,'Bhavani R  ',8,'working ','windows 10 pro ','4.00 GB ','Intel Core i3 ','working ', 'working ');
insert into system_info values(19 ,19,'Punithavathi D  ',9,'visual C++ 2019 ','windows 8.1 pro ','2.00 GB ','Intel Core 2 Duo ','working ', 'working ');
insert into system_info values(26 ,26,'Snega D  ',10,'working ','windows 10 pro ','4.00 GB ','intel core i3 ','working ', 'working ');
insert into system_info values(28 ,28,'Tamil V  ',11,'visual C++2019 ','windows 8.1 ','4.00 GB ','INTEL CORE i3 ','working ', 'working ');
insert into system_info values(27 ,27,'Srinidhi S  ',12,'visual C++2019 ','windows 8.1 ','2.00 GB ','INTEL CORE i3 ','working ', 'working ');
insert into system_info values(23 ,23,'Santhiya S  ',13,'not supported by this processor type ','windows 10 pro ','4.00 GB ','Intel Core 2 Duo ','working ', 'Working ');
insert into system_info values(7 ,7,'Gnanagowsalya K  ',14,'working ','windows 10 ProN ','8.00 GB ','INTEL CORE i5 ','working ', 'working ');
insert into system_info values(11 ,11,'Jothika J  ',15,'working ','Windows 8.1 Pro ','4.00 GB ','INTEL CORE i3 ','working ', 'working ');
insert into system_info values(8 ,8,'Hajeera Sithika L  ',16,'working ','windows 8.1 ','2GB ','Intel Core 2 Duo ','working ', 'working ');
insert into system_info values(6 ,6,'Ghouse bi S  ',18,'working ','Windows 8.1 Pro ','4GB ','INTEL CORE i3 ',' working ', 'working ');
insert into system_info values(29 ,29,'Vinu Andrews S  ',33,'working ','windows 8.1 ','2gb ','Intel Core 2 Duo ',' working ', 'working ');
insert into system_info values(21 ,21,'Roobankumar  K  ',34,'processor not supported ','windows 7 ultimate ','2.00GB ','intel core 2 duo ','working ', 'working ');
insert into system_info values(3 ,3,'Aysha sithika L  ',17,'WORKING ','windows 10 pro ','2GB ','INTEL CORE i3 ','working ', 'working ');
insert into system_info values(18 ,18,'Priya S  ',23,'not  support by this processer tryp ','windows 7 proffessional ','4.00GP ','INTEL CORE i3 ','working ', 'working ');
insert into system_info values(14 ,14,'Komaladevi. S  ',7,'visualc++2019 ','Windows 8.1 Pro ','4.00  GB ','Intel Pentium ','Working ', 'Working ');
insert into system_info values(12 ,12,'Kalaiarasan A  ',32,'working ','Windows 8.1 Pro ','4.00 GB ','INTEL CORE i3 ','working ', 'working ');
insert into system_info values(1 ,1,'Abdul Rahman  B  ',42,'working ','windows 8.1 pro ','2 Gb ','Intel Pentium ','working ', 'workimg ');
insert into system_info values(2 ,2,'Arun T',43,'working ','windows8.1 ','2GB ','IntelCore2Duo ','working ', 'working ');
insert into system_info values(17 ,17,'Prasanth P  ',35,'C++2019 ','Windows 10 Pro ','2.00 GB ','Intel Pentium ','Working ', 'working ');
insert into system_info values(30 ,30,'Yogarajan K  ',36,'Not supported by the processor ','windows 10 pro ','2 GB RAM  ','Intel Pentium ','working ', 'working ');
insert into system_info values(25 ,25,'Saravanan M  ',37,'Working ','Windows 8.1 Pro ','4.00 GB ','INTEL CORE i3 ','Working ', 'Working ');
insert into system_info values(9 ,9,'HARIHARAN A  ',38,'working ','windows 8.1 pro ','4.00 GB ','INTEL CORE i3 ','working ', 'working ');
insert into system_info values(20 ,20,'Raghul S  ',39,'not supported by the processor ','windows 7 ','2.00 GB ','Intel Pentium ','Working ', 'working ');
insert into system_info values(16 ,16,'Narayanan S  ',19,'Working ','windows 8.1 ','4.00GB ','INTEL CORE i3 ','working ', 'working ');


 insert into batch01_details values(1,'Abdul Rahman  B',' ', ' ','2001-01-15',669092087983,92087983,9952630126,6369696359,9952630126,'TI2023M-C01E438
','Password@123','BSC','Computer science',' ',' ',2022,'','abdulrahman001007@gmail.com','No 3/1-76 Indra street Keela ambikaburam Trichy-04','Trichy','Badhusha',' ','Noorjahan');
insert into batch01_details values(2,'Arun T',' ',' ','2001-01-16',341246643302,46643302,8525880306,6382506148,8525880306,'PU2023M-C01E488
','Password@123','BSC','Computer science',' ',' ',2023,' arunaathi41@gmail.com','arunaathi41@gmail.com','3/4 Thirupur Thirupur (po) Kulathur(tk)Senaiyakuti Pudukkottai (Dt) 622502
', 'pudukkottai',' ','Tamil selvam
','Suppu laxmi
');
insert into batch01_details values(3,'Aysha sithika L',' ',' ' ,'1988-01-11',784654756225,54756225,8124823036,8610353074,8124823036,'TI2023F-C01E78D','password@123','12th','computer science',' ', ' ',2010 ,' ',' ','Navalpattu Trichy -26','Trichy',' ','Nazrul Islam','Amthul jabeen');

insert into batch01_details values(4,'Bhavani R',' ',' ','2002-10-13',935775705642,75705642,6380185097,9659871377,6380185097,'Pu2023F-C01E44D','Password@123','BSC','Computer science',' ',' ',2023,'bhavanirai01@gmail.com','bb464490@gmail.com','Melakkottai Kovilur (p)Alangudi Tk Pudukkottai (dt)','Pudukkottai','C.Ramachandran
',' ','R.Thenmozhi
');



insert into batch01_details values(5,'Fathima M',' ',' ','2002-12-17',622631324614,31324614,6374041818,9791676433,6374041818,'TI2023F-C01E43B','Password@123','B.Com','Commerce',' ',' ',2024,'Ray0488faths@gmail.com','Ray0488faths@gmail.com','5/249 20th cross vasancity vayalur road trichy-620102','Trichy','Mohamed Ibrahi',' ','Saira banu');

insert into batch01_details values(6,'Ghouse bi S',' ',' ','1989-08-14',818393990050,93990050,9994286043,7708475065,9994286043,'TI2023F-C01E46D','Password@123','B.A.
','English',' ',' ',2010,'happydhillu@gmail.com','happydhillu@gmail.com','MIG 49 Phase 1 Anna nagarTNUDP trichy-620026','Trichy',' ','Juber khan B','Zarina Begum
');


insert into batch01_details values(7,'Gnanagowsalya K',' ',' ','2003-04-29',418718821662,18821662,7094373123,9965452410,7094373123,'TI2023F-C01E474','Password@123','Bsc ','Computer science',' ',' ',2023,'kkowsalyaai01@gmail.com','kowsalyakannan29@gmail.com','26/1 College roadSri Ram theatre near MusiriTrichy(Dt)','Trichy','Kannan A',' ','Sundhari K');


insert into batch01_details values(8,'Hajeera Sithika L',' ',' ','1992-06-11',430341868981,41868981,8056447098,9751471799,8056447098,'TI2023F-C01E796
','Password@123','BA','English',' ',' ',2013,'hajeerasithka2021@gmail.com','hajeerasithka2021@gmail.com','3 murugesan street M K kottai trichy
','Trichy',' ','Syed Azarudeen','Amthul jabeen');

insert into batch01_details values(9,'HARIHARAN A',' ',' ','2001-10-11',304765424440,65424440,9363649175,9363649175,9363649175,'PE2023M-C01E437','Password@123','BE','EEE',' ',' ',2023,'hariharananbu2001@gmail.com','hariharananbu2001@gmail.com','2/225 North st keelapuliyur po Kunnam tk Perambalur dt 621115','Perambalur','ANBALAGAN D',' ','Anjalai A');

insert into batch01_details values(10,'Jayalakshmi R',' ',' ','1997-02-06',432445616668,45616668,9500628375,6385632493,6385632493,'TI2023F-C01E444','Password@123','BCA','Computer application','MCA','Computer Application',2019,'jayalakshmiai01@gmail.com','jasperjeevi@gmail.com','28-A bharathiyar Street west ambigapuram trichy-4','Trichy','Ravikumar',' ','Geetha');

insert into batch01_details values(11,'Jothika J',' ',' ','2003-01-08',693941180387,41180387,9585607631,9843412199,9585607631,'TI2023F-C01E555','Password@123','BSC','Mathematics',' ',' ',2023,'jothikajai01@gmail.com','jothikajagan8@gmail.com','H/5 Housing Unit Parvathipuram,Musiri Trichy DT','Trichy','Jegatharatchagan K',' ','Manjula J');

insert into batch01_details values(12,'Kalaiarasan A',' ',' ','1987-07-29',447595386464,95386464,9600330846,9994057344,9600330846,'TI2023M-C01E78B','Password@123','B.com','Commerce',' ',' ',2009,'Kalaiarasanayyavooai0@gmail.com','Kalai29.7@gmail.com','2/337 navalpattu burma colony oft po trichy 16','Trichy','K Ayyavoo',' ','A Vasanthi');

insert into batch01_details values(13,'Kayalvizhi M',' ',' ','1998-09-13',67104815,48153395,7339221973,9698821473,7339221973,'TI2023F-C01E475','Password@123','BE','Mechanical engineering',' ',' ',2020,'mkayalai01@gmail.com','kayalmahe123@gmail.com','Door No 2/125A Koothur colony Koothur post  mannachanallur Tk Trichy  621216','Trichy','MahendhranN',' ','Vijayaragini M');

insert into batch01_details values (14,'Komaladevi S',' ',' ','2003-07-29',460205744637,05744637,8940898862,7904257743,8940898862,'PU2023F-C01E466','Password@123','BSC','Computer science',' ',' ',2023,' komaladevi2003@gmail.com','komaladevi2003@gmail.com','Gandharvakkottai pudukottai','Pudukottai','M Subramaniyan',' ','Kalaiselvi S');

insert into batch01_details values(15,'LAVANYA M ',' ',' ','2001-02-26',629731226643,31226643,7904460924,8248554770,7904460924,'TI2023F-C01EA43','Password@123','BSC ','Mathematics',' ',' ',2021,'mlavanyam37@gmail.com','mlavanyam37@gmail.com','33/66 Kamala Nehru Nagar EB Road','Trichy','Aravind samy R', ' ','Avadaiyammal');

insert into batch01_details values(16,'Narayanan S',' ',' ','1999-06-14',282903912214,03912214,9361015928,8122648085,9361015928,'TI2023M-C01E78C','Password@123','BA','History',' ',' ',2019,'Naveenkds82@gmail.com','Naveenkds82@gmail.com','3/141 Sivan kovil street allithurai somarampettai post trichy 620102','Trichy','Sivaprakasam',' ','Sumathi');

insert into batch01_details values(17,'Prasanth P',' ',' ','2000-07-27',983315540255,15540255,9361216766,9626922317,9361216766,'PU2023M-C01E445','Password@123','BE','ECE','','',2022,'prasanth27ai01@gmail.com','aryanprasanth163@gmail.com','No 105 Maruthampatti Vilapatti(post) Ilupur (Taluk) Pudukkottai-622504','Pudukkottai','Palanisamy M',' ','Ponnazhagu P');
insert into batch01_details values(18,'Priya S',' ',' ','2002-05-05',920343048388,43048388,9626940557,9626940557,8508332712,'TI2023F-C01EC0E','Password@123','B.SC','Physics',' ',' ',2023,'lpriyaai01@gmail.com','lakshmipriya5522@gmail.com','10 Mettu street Wouraiyur Trichy-3','Trichy','SenthilKumar M
',' ','Elangiyam S');

insert into batch01_details values(19,'Punithavathi D',' ',' ','1997-05-22',762578126673,78126673,6369782863,9715451286,6369782863,'TI2023F-C01E8C2
','Password@123','B.Com','Commerce',' ',' ',2025,'Punithavathid1997@gmail.com','Punithavathid1997@gmail.com','2/275 NPS colony OFT Main Road HAPF Town Suriyur Post Trichy-620025','Trichy','V. Devaraj',' ','D Santhamani');

insert into batch01_details  values(20,'Raghul S',' ',' ','2000-06-07',871736862600,36862600,7010107069,8680827179,8680827179,'TI2023M-C01E4E6','Password@123','BE','MECHANICAL ENGINEERING',' ',' ',2022 ,'rockstarraghul55@gmail.com','rockstarraghul55@gmail.com','3/443 mgr rajaveethi Vs colony Kattur Trichy 620019','Trichy','Senthil Kumar p',' ','Sumathi S');

insert into batch01_details  values(21,'Roobankumar  K',' ',' ','1992-11-22',612231264958,31264958,7904255453,9486645960,7904255453,'TI2023M-C01E8CB','Password@123','BE','ECE',' ',' ',2015,'roobanai01@gmail.com','vroobank92@gmail.com','L1 chandradhayam, Shankar abodes, near krt motors, chennai trunk road, Thiruvanaikovil trichy','Trichy','Kumaravel',' ','Valli');
insert into batch01_details  values(22,'Sangari S',' ',' ','1998-01-19',360158896738,58896738,9787264394,9751721397,9787264394,'TH2023F-C01E43E','Password@123','BE','ECE',' ',' ',2019,'sangarisai01@gmail.com','sangarisaminathan@gmail.com','1/44 Agraharam North budalur Thanjavur (Dt) 613602','Thanjavur','Saminathan M',' ','Latha S');


insert into batch01_details  values(23,'Santhiya S',' ',' ','2003-04-29',842296226066,96226066,8940937523,9842021095,8940937522,'TI2023F-C01E43D','Password@123','Bsc ','Information technology
',' ',' ',2023,'ssanthiyaai01@gmail.com','santhiyasakthivel37@gmail.com','No 57 3rd street gandhinagar college road musiri trichy(dt)','Trichy','Sakthivel T
',' ','Chitra S');
insert into batch01_details  values(24,'Saranya N',' ',' ','1994-07-28',971123726105,23726105,8248879007,9585031787,8248879007,'TI2023F-C01EA19
','Password@123','BE','CSE',' ',' ',2015,'saranyanarayananai01@gmail.com','saranyanarayananai01@gmail.com','No3a Balaji Avenue 1st cross Old karur road Melachinthamani Trichy 620002','Trichy',' ','S Narayanan','A Marikkannu');
insert into batch01_details  values(25,'Saravanan M',' ',' ','2003-05-20',385868916470,68916470,8838011266,7603972485,8838011266,'TH2023M-C01E44A','Password@123','BSC','Computer Science
',' ',' ',2023,'Saravananmai01@gmail.com','saravanasaro1435@gmail.com','1/88 Vallabramankadu Sornakadu (Post) Peravurani(Taluk),Thanjavur (District)-614804','Thanjavur','Malaiyarasan V
',' ','Ganamani M');

insert into batch01_details  values(26,'Snega D',' ',' ','2003-04-05',546307861816,07861816,9047648856,8072885475,9047648856,'TI2023F-C01E446','Password@123','BSC','IT',' ',' ',2023,'snegadai01@gmail.com','Stdsnega.it@cauverycollege.ac.in','1-130 / A perumal Kovil street Reddi mangudi Trichy','Trichy','R.Durai raj',' ','D Bhuvaneswari');

insert into batch01_details  values(27,'Srinidhi S',' ',' ','2001-12-19',733557069525,57069525,9360728585,9500868943,9360728585,'TI2023F-C01EA34','Password@123','BSC','IT',' ',' ',2023,'srinidhiai01@gmail.com','Srinidhisrinidhi233@gmail.com','45/B East street melur srirangam','Trichy','Sundarrajan B',' ','Shanthi S');

insert into batch01_details  values(28,'Tamil V',' ',' ','2003-05-09',277289901567,89901567,7904761471,7904761471,7904761471,'TI2023F-C01EA44','Password@123','BSC','IT','NIL','NIL',2023,'tamilvai01@gmail.com','venktesantamil@gmail.com','45/B East street Melur Srirangam Trichy','Trichy','Venktesan B',' ','Lalitha V');

insert into batch01_details  values(29,'Vinu Andrews S',' ',' ','1999-11-24',543353698598,53698598,8428908488,8428908488,8428908488,'TI2023M-C01F2A8','Password@123','Bba','business administration','MBA','Safety',2022,'vinuandrewsai01@gmail.com','vinuandrews10@gmail.com','66 muslim street varaganeri Trichy','Trichy','Selvaraj A
',' ','Mercy s');

insert into batch01_details  values(30,'Yogarajan K',' ',' ','2001-12-15',241602457541,02457541,6379275571,8056724735,6379275571,'TH2023M-C01E455','Password@123','BCA','Computer Application
',' ',' ',2022,'Yogarajanai01@gmail.com','yogiraja2001@gmail.com','44,agraharam north Budalur Budalur Thanjavur (dt) Pincode 613602','Thanjavur','M Kaliyamoorthy
',' ','K Uma maheswari');
show tables;



drop table system_info;
select * from batch01_details;
create table sample_table (
user_id int not null primary key auto_increment,
name varchar(50),
qualification varchar(50)
);
delimiter &&
create procedure insert_table (
in nameparameter varchar(50),
in qualificationparameter varchar(50)
)
begin
insert into sample_table(name,qualification) values (nameparameter, qualificationparameter);
end &&
delimiter ;
call insert_table('saranay','BE');
select * from sample_table;
delimiter ##
drop procedure if exists mycode;##
create procedure mycode(
in tablename varchar(255),
in columnname varchar(255),
in valuechange varchar(255),
in idname varchar(255),
in idparam int 
)
begin
set @statement=concat("update ",tablename," set ",columnname, "=\'",valuechange,'\'',' where ',idname,'=',idparam);

prepare stmt from @statement;
execute stmt;
end ##
 delimiter ;   
 
select * from sample_table;
describe sample_table;
call mycode('sample_table','name','jaya','user_id',1);
drop table sys_info;
select * from system_info;
select * from batch01_details;
create table student_details(
Student_Name varchar(70),	
Gender varchar(70),
Class_Level varchar(70),
Home_State varchar(60),	
Major varchar(70),	
Extracurricular_Activity varchar(70));
insert into student_details values ('Alexandra','Female ','4. Senior  ','CA  ','English  ','Drama Club  '),
('Andrew','Male ','1. Freshman  ','SD  ','Math  ','Lacrosse  '),
('Anna','Female ','1. Freshman  ','NC  ','English  ','Basketball  '),
('Becky','Female ','2. Sophomore  ','SD  ','Art  ','Baseball  '),
('Benjamin','Male ','4. Senior  ','WI  ','English  ','Basketball  '),
('Carl','Male ','3. Junior  ','MD  ','Art  ','Debate  '),
('Carrie','Female ','3. Junior  ','NE  ','English  ','Track & Field  '),
('Dorothy','Female ','4. Senior  ','MD  ','Math  ','Lacrosse  '),
('Dylan','Male ','1. Freshman  ','MA  ','Math  ','Baseball  '),
('Edward','Male ','3. Junior  ','FL  ','English  ','Drama Club  '),
('Ellen','Female ','1. Freshman  ','WI  ','Physics  ','Drama Club  '),
('Fiona','Female ','1. Freshman  ','MA  ','Art  ','Debate  '),
('John','Male ','3. Junior  ','CA  ','Physics  ','Basketball  '),
('Jonathan','Male ','2. Sophomore  ','SC  ','Math  ','Debate '),
('Joseph','Male ','1. Freshman  ','AK  ','English  ','Drama Club '),
('Josephine','Female ','1. Freshman  ','NY  ','Math  ','Debate '),
('Karen','Female ','2. Sophomore  ','NH  ','English  ','Basketball '),
('Kevin','Male ','2. Sophomore ','NE','Physics ','Drama Club'),
('Lisa','Female ','3. Junior ','SC  ','Art  ','Lacrosse  '),
('Mary','Female ','2. Sophomore  ','AK  ','Physics  ','Track & Field  '),
('Maureen','Female ','1. Freshman  ','CA  ','Physics  ','Basketball  '),
('Nick','Male ','4. Senior  ','NY  ','Art  ','Baseball  '),
('Olivia','Female ','4. Senior  ','NC  ','Physics  ','Track & Field  '),
('Pamela','Female ','3. Junior  ','RI  ','Math  ','Baseball  '),
('Patrick','Male ','1. Freshman  ','NY  ','Art  ','Lacrosse  '),
('Robert','Male ','1. Freshman  ','CA  ','English  ','Track & Field  '),
('Sean','Male ','1. Freshman  ','NH  ','Physics  ','Track & Field  '),
('Stacy','Female ','1. Freshman  ','NY  ','Math  ','Baseball  '),
('Thomas','Male ','2. Sophomore  ','RI  ','Art  ','Lacrosse  '),
('Will','Male ','4. Senior  ','FL  ','Math  ','Debate  ');
show tables;
select * from batch01_details;
select * from system_info;
select * from sample_table;
select * from student_details;
call insert_table('snegha','Bsc');
call mycode('sample_table','qualification','Msc','user_id',1);
select first_name from batch01_details where first_name like 'j%';
select first_name as name from batch01_details;
select * from system_info as info;
select first_name,UG,subject_group from batch01_details;
call insert_table('arun T','BSC');
backup database ai_saranya to disk = 'C:\backups\ai_saranya.bak'
select first_name from batch01_details where UG = 'BE';
select * from batch01_details;
select * from batch01_details a1, system_info s1;
select * from  batch01_details a1 right join system_info s1 on a1.sno =s1.details_id;
select name,details_id,system_no from batch01_details a1 left join system_info s1 on a1.sno =s1.details_id;
select * from batch01_details order by year_of_passing;
select * from batch01_details where district ='trichy' or first_name like 's%';
select * from batch01_details where not district ='trichy';
select * from batch01_details where not sno > 15;




